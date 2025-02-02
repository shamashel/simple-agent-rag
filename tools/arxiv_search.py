import textwrap
from langchain.retrievers.web_research import WebResearchRetriever
from langchain.tools.retriever import create_retriever_tool
from langchain_core.tools import Tool
import os

from tools.base_tool import BaseTool
from utils import VECTOR_DBS_PATH, build_chroma_db

__CHROMA_PATH = os.path.join(VECTOR_DBS_PATH, "arxiv_search_chromadb")

class ArxivSearch(BaseTool):
    def name(self) -> str:
        return "arXiv Research Paper Search"

    def description(self) -> str:
        return textwrap.dedent("""
        Used to search for research papers posted on Cornell's arXiv platform.

        arXiv contains research related to the following subjects:
            - Physics
            - Mathematics
            - Computer Science
            - Quantitative Biology
            - Quantitative Finance
            - Statistics
            - Electrical Engineering and Systems Science
            - Economics
        """)

    def build(self) -> Tool:
        store = build_chroma_db
        retriever = WebResearchRetriever.from_llm(
            vectorstore=store,
            llm=self.llm
        )
        return create_retriever_tool(retriever, self.name, self.description)
