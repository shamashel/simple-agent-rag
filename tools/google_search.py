from langchain.retrievers.web_research import WebResearchRetriever
from langchain.tools.retriever import create_retriever_tool
from langchain_core.tools import Tool
import os
import textwrap

from tools.base_tool import BaseTool
from utils import VECTOR_DBS_PATH, build_chroma_db

__CHROMA_PATH = os.path.join(VECTOR_DBS_PATH, "google_search_chromadb")

class GoogleSearch(BaseTool):
    def name(self) -> str:
        return "Google Search"

    def description(self) -> str:
        return textwrap.dedent("""
        Used for searching arbitrary information via the Google search engine.
        This should be used as a last resort, when other tools are unlikely to retrieve the requested information.
        """)

    def build(self) -> Tool:
        store = build_chroma_db(__CHROMA_PATH)
        retriever = WebResearchRetriever.from_llm(
            vectorstore=store,
            llm=self.llm
        )
        return create_retriever_tool(retriever, self.name, self.description)

