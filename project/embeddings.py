
import os
from dotenv import load_dotenv

#data ingestion libraries
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

#embeddings

from langchain_community.embeddings import JinaEmbeddings

from chunking import spilts

from langchain_community.vectorstores import FAISS


jina_key = os.getenv("JINA_API_KEY")

vectors = JinaEmbeddings(jina_key=jina_key, model_name="jina-embedding-v2-base-en")

print("Generating embeddings for chunks...", vectors.model_name)

store = FAISS.from_documents(
   spilts,vectors
)

