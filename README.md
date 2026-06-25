# Agent

A ReAct-based intelligent agent that combines RAG retrieval & summarization, tool calling, and middleware, served through a Streamlit web UI.

## Architecture Overview

```
User ──▶ app.py (Streamlit web UI)
            │
            ▼
      ReactAgent (react_agent.py)
            │  create_agent(...) + execute_stream
            ├──▶ agent_tools.py   (tool set: weather / location / RAG summary ...)
            ├──▶ middleware.py     (monitoring, pre-model logging, prompt-switch reporting)
            └──▶ factory.py        (chat_model / embed_model)
                       │
            RagSummarizeService (rag_service.py)
                       │  retrieve_docs + chain
                       ▼
            VectorStoreService (vector_store.py)
                       │  load_document + get_retriever
                       ▼
                  Vector store / Retriever
```

## Project Structure

```
.
├── agent/                      # Agent core
│   ├── tools/
│   │   ├── agent_tools.py      # Tools the agent can call
│   │   └── middleware.py       # Middleware: monitoring / logging / prompt switching
│   └── react_agent.py          # ReAct agent entry class
├── config/                     # Configuration files
├── data/                       # Data / documents
├── model/
│   ├── factory.py              # Model factory (chat_model / embed_model)
│   └── prompts/                # Prompt templates
├── rag/
│   ├── rag_service.py          # RAG summarization service
│   └── vector_store.py         # Vector store service
├── utils/
│   ├── chain_debug.py          # Chain debugging tool
│   ├── config_handler.py       # Config file handling
│   ├── file_handler.py         # File handling utilities
│   ├── logger_handler.py       # Logging utilities
│   ├── path_tools.py           # Path utilities
│   └── prompt_loader.py        # Prompt loading utilities
├── .gitignore
├── README.md
└── app.py                      # Streamlit web entry point
```

## Modules

### agent — Agent core

**`agent/react_agent.py` · `class ReactAgent`**
- `self.agent = create_agent(...)` — builds the ReAct agent
- `execute_stream(...)` — streams the reasoning and tool-calling process

**`agent/tools/agent_tools.py`** — agent tool set
- `rag_summarize` — calls the RAG service for retrieval + summarization
- `get_weather` — fetch weather
- `get_user_location` — fetch the user's location
- `get_user_id` — fetch the user ID
- `get_current_month` — get the current month
- `generate_external_data` — generate / fetch external data

**`agent/tools/middleware.py`** — middleware
- `monitor_tool` — monitor tool calls
- `log_before_model` — log before each model call
- `report_prompt_switch` — report prompt switching

### rag — Retrieval-augmented generation

**`rag/rag_service.py` · `class RagSummarizeService`**
- Attributes: `vector_store` / `retriever` / `prompt_template` / `prompt_text` / `model` / `chain`
- `rag_summarize` — main RAG summarization flow
- `_init_chain` — initialize the processing chain
- `retrieve_docs` — retrieve relevant documents
- `_load_prompt_text` — load prompt text

**`rag/vector_store.py` · `class VectorStoreService`**
- Attributes: `vector_store` / `spliter`
- `load_document` — load and split documents
- `get_retriever` — get a retriever

### model — Model factory

**`model/factory.py`**
- `chat_model` — chat model
- `embed_model` — embedding model

### utils — Utilities

| File | Purpose |
| --- | --- |
| `config_handler.py` | Config file handling |
| `path_tools.py` | Path utilities |
| `file_handler.py` | File handling utilities |
| `prompt_loader.py` | Prompt loading utilities |
| `logger_handler.py` | Logging utilities |
| `chain_debug.py` | Chain debugging tool |

### app.py — Web entry point

A Streamlit web interface that serves as the entry point for users to interact with `ReactAgent`.

## Quick Start

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Launch the web UI
streamlit run app.py
```
