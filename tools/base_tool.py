from abc import ABC, abstractmethod
from langchain_core.language_models import BaseLLM
from langchain_core.tools import Tool


class BaseTool(ABC):
    llm: BaseLLM

    def __init__(self, llm: BaseLLM):
        self.llm = llm

    @abstractmethod
    def build(self) -> Tool:
        pass