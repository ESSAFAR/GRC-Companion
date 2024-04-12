from langchain_community.document_loaders import DirectoryLoader
import os
import shutil
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores.chroma import Chroma
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.schema import Document

resources = "resources"
CHROMA_PATH = "chroma"
key = "MY_SECRET_KEY"

def load_documents():
    """
    Load documents from resources directory.
    Returns:
        list: A list of loaded documents.
    """
    loader = DirectoryLoader(resources, glob="*.md")

    print("Hello")

    documents = loader.load()

    return documents


def split_text(documents: list[Document]):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=300,
        chunk_overlap=100,
        length_function=len,
        add_start_index=True,
    )
    chunks = text_splitter.split_documents(documents)
    print(f"Split {len(documents)} documents into {len(chunks)} chunks.")

    document = chunks[10]
    print(document.page_content)
    print(document.metadata)

    return chunks


def save_to_chroma(chunks: list[Document]):
    # Clear out the database first.
    if os.path.exists(CHROMA_PATH):
        shutil.rmtree(CHROMA_PATH)

    # Create a new DB from the documents.
    db = Chroma.from_documents(
        chunks, OpenAIEmbeddings(openai_api_key=key), persist_directory=CHROMA_PATH
    )
    db.persist()
    print(f"Saved {len(chunks)} chunks to {CHROMA_PATH}.")


save_to_chroma(split_text(load_documents()))
