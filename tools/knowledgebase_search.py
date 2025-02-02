from langchain.tools.retriever import create_retriever_tool
from langchain_core.documents import Document
from langchain_core.tools import Tool
from langchain_chroma import Chroma
from langchain_community.document_loaders.pdf import PyMuPDFLoader
import os
import textwrap

from env import ENV
from tools.base_tool import BaseTool
from utils import ROOT_DIR, VECTOR_DBS_PATH, build_chroma_db

__CHROMA_PATH = os.path.join(VECTOR_DBS_PATH, "knowledgebase_search_chromadb")
__KNOWLEDGEBASE_PATH = os.path.join(ROOT_DIR, "knowledgebase")

class KnowledgebaseSearch(BaseTool):
    def name(self) -> str:
        return f"Knowledgebase Search for {ENV.COMPANY_NAME}"

    def description(self) -> str:
        return textwrap.dedent(f"""
        Used to search the internal documents of {ENV.COMPANY_NAME}.
        If a user asks about {ENV.COMPANY_NAME} or any products related to {ENV.COMPANY_NAME}, this is the first place to look.
        Current available information includes:
            - Product information
            - Earnings Reports
            - Divisions
        """)

    def build(self) -> Tool:
        store = self.__setup_datastore()
        return create_retriever_tool(store.as_retriever(), self.name, self.description)

    def __setup_datastore(self):
        """Set up ChromaDB and populate with PDF documents if needed."""
        if os.path.exists(__CHROMA_PATH):
            store = build_chroma_db(__CHROMA_PATH, retain=True)
        else:
            store = build_chroma_db(__CHROMA_PATH, retain=True)
            self.__add_knowledgebase_to_store(store)
    
    def __add_knowledgebase_to_store(self, store: Chroma) -> None:
        loader = PyMuPDFLoader(file_path=__KNOWLEDGEBASE_PATH, extract_tables="markdown")
        docs: list[Document] = []
        for doc in loader.lazy_load():
            docs.append(doc)
            if len(docs) > ENV.DOCUMENT_BATCH_COUNT:
                store.add_documents(docs)
                docs = []
