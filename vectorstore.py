from openai import OpenAI

client = OpenAI()

# Create a vector store
vector_store = client.beta.vector_stores.create(
    name="company_knowledge"
)

print("Vector Store ID:", vector_store.id)
