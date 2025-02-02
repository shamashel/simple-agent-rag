import textwrap
from langchain.retrievers import ArxivRetriever
from langchain.tools.retriever import create_retriever_tool
from langchain_core.tools import Tool

from tools.base_tool import BaseTool

class ArxivSearch(BaseTool):
    @property
    def name(self) -> str:
        return "arXiv Research Paper Search"

    @property
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
        retriever = ArxivRetriever(
            load_max_docs=10,
            get_full_documents=True
        )
        return create_retriever_tool(retriever, self.name, self.description)
