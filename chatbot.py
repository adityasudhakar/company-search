import json
import requests
from openai import OpenAI
import os

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

# --- Vanna API call ---
def call_vanna(message, user_email="adi@vanna.ai"):
    url = "https://app.vanna.ai/api/v0/chat_sse"
    headers = {
        "Content-Type": "application/json",
        "VANNA-API-KEY": os.environ.get("VANNA_API_KEY")
    }
    payload = {
        "message": message,
        "user_email": os.environ.get("VANNA_USER_EMAIL"),   # always override with your email
        "acceptable_responses": ["text"]
    }
    resp = requests.post(url, headers=headers, json=payload)
    return resp.text


# --- Chatbot with tool handling ---
def chat(query: str):
    response = client.responses.create(
        model="gpt-4.1",
        input=f"Route this question to the right tool.\n\nUser asked: {query}",
        tools=[
            {
                "type": "file_search",
                "vector_store_ids": ["vs_68df5c252900819199b75e8a8453ceaa"]
            },
            {
                "type": "function",
                "name": "query_vanna",
                "description": (
                    "Use this when the user asks about usage, analytics, metrics, "
                    "counts, questions, or other structured data. "
                    "Do NOT try to answer from documents. Always use this for analytics."
                ),
                "parameters": {
                    "type": "object",
                    "properties": {
                        "message": {"type": "string"},
                        "user_email": {"type": "string"}
                    },
                    "required": ["message"]
                }
            }
        ]
    )

    # 🔎 Debug: show what the model returned
    for item in response.output:
        print("\nDEBUG ITEM:", item)

        if item.type == "function_call" and item.name == "query_vanna":
            # Parse arguments from JSON string
            args = json.loads(item.arguments)
            print("➡️ Model requested Vanna call with args:", args)

            # Always force correct email
            vanna_result = call_vanna(args["message"], "adi@vanna.ai")

            # Send result back to GPT to get a polished answer
            followup = client.responses.create(
                model="gpt-4.1",
                input=f"User asked: {query}\n\nHere’s the result from Vanna:\n{vanna_result}\n\nPlease integrate this into your final answer."
            )
            return followup.output_text

    # Default: no function call, return model’s normal answer
    return response.output_text


# --- Run chatbot ---
if __name__ == "__main__":
    q = input("Ask me something: ")
    answer = chat(q)
    print("\n🤖 Chatbot says:\n", answer)
