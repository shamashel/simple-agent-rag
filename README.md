# Simple Agent RAG

A simple agent with the ability to search arXiv papers, Google (with an API key), and a knowledgebase of local PDF files.

Note that this defaults to using gpt3.5, which means the LLM is *not* RL'd into knowing how to handle tools.

This means tool calls will be significantly less effective than ones done via a purpose-built tool calling LLM (GPT4o, Claude 3.5 family, etc)

## Important Note

All documents included in the knowledgebase of this repository were access via publicly available means. They were included in good faith. If you would like to request these documents be taken down, please raise an issue or PR with a message stating such and I will remove them ASAP.

## Setup

1. Ensure Python 3.12 is available on your system (`pyenv` recommended)
2. Ensure [poetry is install on your system](https://python-poetry.org/docs/)
3. Run `poetry install`
4. Set up a `.env` file using `.env.example` as an example
    - An OpenAI API key is required for general functionality
    - A Google API key is required for Google Search

## How to run

- Run `poetry run streamlit run app.py`
- Try asking SS&C's financial report, Black Diamond platform, or GlobeOp division

## Choices made

### Tool Choice

- The local knowledgebase was included to showcase an example commonly found in real-world chatbots
- The Google tool was included to showcase integration with third party sources
- The arXiv tool was included as a backup for the Google tool, in case whoever runs this project does not have a Google API key

### Use of LangChain

At my job, we ended up creating our own solution for managing agent orchestration rather than using something like LangChain.

That being said, I've been curious how things could have gone if we had gone full LangChain, so I wanted to try it out here. Please forgive any weird conventions, this was done as part of a learning experience, so I didn't make use of any AI development tools that could have likely made this closer to a standard approach.
