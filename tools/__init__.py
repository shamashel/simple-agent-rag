"""Module for all tools to be used by the assistant"""

from langchain_core.language_models import BaseLLM
from langchain_core.tools import Tool
from env import ENV
from tools.arxiv_search import ArxivSearch
from tools.google_search import GoogleSearch
from tools.knowledgebase_search import KnowledgebaseSearch

def get_all_tools(llm: BaseLLM) -> list[Tool]:
    tools = [
        ArxivSearch(llm).build(),
        KnowledgebaseSearch(llm).build()
    ]
    if ENV.GOOGLE_API_KEY != "":
        tools.append(GoogleSearch(llm).build())
    return tools