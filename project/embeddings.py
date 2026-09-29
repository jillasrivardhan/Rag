from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings
import os

from chunking import spilts

load_dotenv()

# Convert Document objects -> strings
texts = [doc.page_content for doc in spilts]

print(type(texts))
print(type(texts[0]))
print(texts[0])

embeddings_client = OpenAIEmbeddings(
    model="jina-embeddings-v3",
    api_key=os.getenv("JINA_API_KEY"),
    base_url="https://api.jina.ai/v1",
)

embeddings = embeddings_client.embed_documents(texts)

print("Number of chunks:", len(texts))
print("Number of embeddings:", len(embeddings))

print("First embedding:")
print(embeddings[0])

print("Embedding dimension:", len(embeddings[0]))