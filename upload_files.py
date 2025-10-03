from openai import OpenAI

client = OpenAI()

# Local file path
file_path = "/Users/adityasudhakar/Downloads/AecorSoft Support and Maintenance Agreement.pdf"

# Upload the file
with open(file_path, "rb") as f:
    result = client.files.create(
        file=f,
        purpose="assistants"
    )

print("Uploaded file_id:", result.id)
