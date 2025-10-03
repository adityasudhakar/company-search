from openai import OpenAI

client = OpenAI()

vector_store_id = "vs_68df5c252900819199b75e8a8453ceaa"
file_ids = [
    "file-REixFdmZsc4JWUDmCVoVTu",
    "file-Ty99w6TLx21qSAbVZiqKbq"
]

# Attach each file
for fid in file_ids:
    resp = client.beta.vector_stores.files.create(
        vector_store_id=vector_store_id,
        file_id=fid
    )
    print(f"Attached {fid}: {resp}")
