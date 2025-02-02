"""Module for all tools to be used by the assistant"""

from langchain_core.tools import Tool
from tools.arxiv_search import ArxivSearch
from tools.google_search import GoogleSearch
from tools.knowledgebase_search import KnowledgebaseSearch

def get_all_tools() -> list[Tool]:
    return [
        ArxivSearch().build(),
        GoogleSearch().build(),
        KnowledgebaseSearch().build()
    ]