from openai import OpenAI

client = OpenAI()

vector_store_id = "vector_store_id"

status = client.beta.vector_stores.files.list(
    vector_store_id=vector_store_id
)

for f in status.data:
    print(f"File: {f.id}, Status: {f.status}")
