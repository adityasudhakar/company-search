from openai import OpenAI

client = OpenAI()

# Local file path
file_path = "your local file path"

# Upload the file
with open(file_path, "rb") as f:
    result = client.files.create(
        file=f,
        purpose="assistants"
    )

print("Uploaded file_id:", result.id)
