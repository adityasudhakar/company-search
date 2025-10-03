from openai import OpenAI

client = OpenAI()

vector_store_id = "vector_store_id"
file_ids = [
    "file-1-id",
    "file-2-id"
]

# Attach each file
for fid in file_ids:
    resp = client.beta.vector_stores.files.create(
        vector_store_id=vector_store_id,
        file_id=fid
    )
    print(f"Attached {fid}: {resp}")
