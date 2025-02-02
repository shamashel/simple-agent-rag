from abc import ABC, abstractmethod
from langchain_core.language_models import BaseLLM
from langchain_core.tools import Tool


class BaseTool(ABC):
    llm: BaseLLM

    def __init__(self, llm: BaseLLM):
        self.llm = llm

    @abstractmethod
    @property
    def name(self) -> str:
        """The name of the tool. Setting this as an abstract property so ruff will yell when not set"""
        pass

    @abstractmethod
    @property
    def description(self) -> str:
        """The description of the tool. Setting this as an abstract property so ruff will yell when not set.
        
        Given that multiline strings with hanging indents are likely to occur, use of `textwrap.dedent` is recommended.
        """
        pass

    @abstractmethod
    def build(self) -> Tool:
        pass