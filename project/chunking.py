
from langchain_text_splitters import RecursiveCharacterTextSplitter

from data_loading import docs

chunks = RecursiveCharacterTextSplitter(
   chunk_size = 1000,
   chunk_overlap = 200
)

spilts = chunks.split_documents(docs)

# print(spilts)

for i,chunk in enumerate(spilts):
   print("="*60)
   print(f"{i} : {chunk.page_content}")
   print("="*60)