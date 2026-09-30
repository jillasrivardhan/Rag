
from embeddings import vectors

query = "What are the projects?"

top_match = vectors.similarity_search(query, k=2)

print(top_match)