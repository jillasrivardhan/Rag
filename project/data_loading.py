
from langchain_community.document_loaders import TextLoader
# from langchain_core.document_loaders import TextLoader

document = TextLoader(
    "M:/Rag/Data/about_me_sri_vardhan.txt",
    encoding="utf-8"
)

docs = document.load()

print(docs[0].page_content)