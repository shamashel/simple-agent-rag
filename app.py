from typing import Literal, TypedDict
from langchain_core.messages import AIMessage, HumanMessage
import streamlit as st

from agent import AGENT

class Message(TypedDict):
    role: Literal["user", "assistant"]
    content: str

def messages_to_chat_history(messages: list[Message]) -> list[HumanMessage | AIMessage]:
    return [
        HumanMessage(m["content"]) if m["role"] == "user" else AIMessage(m["content"])
        for m in messages
    ]

st.title("Simple chat")
if "messages" not in st.session_state:
    st.session_state.messages: list[Message] = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"].replace("$", "\$")) # Stupid hack to avoid latex formatting

if prompt := st.chat_input("Message RAGBot"):
    with st.chat_message("user"):
        st.markdown(prompt.replace("$", "\$")) # Stupid hack to avoid latex formatting
    st.session_state.messages.append(Message(role="user", content=prompt))
    with st.chat_message("assistant"):
        with st.spinner("Generating response..."):
            raw_response = AGENT.invoke(
                {"input": prompt, "chat_history": messages_to_chat_history(st.session_state.messages)},
            )
        response = str(raw_response["output"])
        st.markdown(response.replace("$", "\$")) # Stupid hack to avoid latex formatting without influencing the bot via chat_history
    st.session_state.messages.append({"role": "assistant", "content": response})
    st.rerun()