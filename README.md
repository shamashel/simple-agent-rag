# Simple Agent RAG

A simple agent with the ability to search arXiv papers, Google (with an API key), and a knowledgebase of local PDF files.

**Why was \<tool\> included?**

- The local knowledgebase was included to showcase an example commonly found in real-world chatbots
- The Google tool was included to showcase integration with third party sources
- The arXiv tool was included as a backup for the Google tool, in case whoever runs this project does not have a Google API key

## Setup

1. Ensure Python 3.12 is available on your system (`pyenv` recommended)
2. Ensure [poetry is install on your system](https://python-poetry.org/docs/)
3. Run `poetry install`
4. Set up a `.env` file using `.env.example` as an example
    - An OpenAI API key is required for general functionality
    - A Google API key is required for Google Search

## How to run

- Run `poetry run streamlit run app.py`
