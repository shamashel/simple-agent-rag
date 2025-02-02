import os
from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings

ROOT_DIR = os.path.dirname(os.path.abspath(__file__)) # Yoinking this from flask
VECTOR_DBS_PATH = os.path.join(ROOT_DIR, "vector_dbs")
assert (
    os.path.isdir(VECTOR_DBS_PATH)
), "Unable to locate `vector_dbs` directory. Please ensure `utils.py` has not been moved from the root of the project"

def build_chroma_db(path: str, retain=False):
    """Build/Rebuild an instance of ChromaDB in the given path with OpenAI embeddings"""
    if not retain and os.path.exists(path):
        os.remove(path)
    return Chroma(persist_directory=path, embedding_function=OpenAIEmbeddings)