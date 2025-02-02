from typing import TypedDict
from langchain.agents.agent import AgentExecutor
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.agents.format_scratchpad.openai_tools import format_to_openai_tool_messages
from langchain.agents.output_parsers.openai_tools import OpenAIToolsAgentOutputParser
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.runnables import RunnableWithMessageHistory
from langchain_openai import ChatOpenAI
from tools import get_all_tools


class ExpectedResponse(TypedDict):
    input: str
    intermediate_steps: list
    chat_history: list

def _parse_input(res: ExpectedResponse):
    return res["input"]
def _parse_scratchpad(res: ExpectedResponse):
    return format_to_openai_tool_messages(res["intermediate_steps"])
def _parse_history(res: ExpectedResponse):
    return res["chat_history"]

def build_agent(verbose: bool = True):
    tools = get_all_tools()
    llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0).bind_tools(tools)

    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a helpful assistant"),
        MessagesPlaceholder(variable_name="chat_history", optional=True),
        ("user", "{input}"),
        MessagesPlaceholder(variable_name="agent_scratchpad", optional=True)
    ])

    agent = (
        {
            "input": _parse_input,
            "agent_scratchpad": _parse_scratchpad,
            "chat_history": _parse_history
        }
        | prompt
        | llm
        | OpenAIToolsAgentOutputParser()
    )
    history = ChatMessageHistory()
    agent_with_history = RunnableWithMessageHistory(agent, lambda s: history, input_messages_key="input", history_messages_key="chat_history")
    return AgentExecutor(agent=agent_with_history, tools=tools, verbose=verbose)

AGENT = build_agent()