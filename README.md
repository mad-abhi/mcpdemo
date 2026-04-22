# Multi-Agent AI Assistant (MCP + Groq + PostgreSQL)

This repository contains an end-to-end AI Assistant built using the **Model Context Protocol (MCP)**, **LangChain**, and the high-speed **Groq API**. The system is designed to act as a central "brain" that can interact with various external "servers"—specifically a PostgreSQL database for data retrieval and search/browser tools for real-time information.



## Overview

Unlike traditional AI agents that require manual tool-calling definitions for every new integration, this project utilizes the **MCP Protocol**. This allows the agent to dynamically connect to standardized servers:
- **PostgreSQL Server**: Queries structured medical/equipment data directly.
- **Web Search/Browser**: Performs real-time search via DuckDuckGo or browser automation via Playwright.
- **Groq Inference**: Utilizes Llama-3 or Mixtral models via Groq for near-instant response times.

## Tech Stack

* **Language:** Python 3.10+
* **LLM Provider:** [Groq API](https://console.groq.com/)
* **Framework:** LangChain & LangGraph
* **Protocol:** Model Context Protocol (MCP)
* **Database:** PostgreSQL (Supabase/Local)
* **Environment Management:** `uv` (Fast Python package manager)

## Prerequisites

1.  **Groq API Key**: Get it from the Groq Cloud Console.
2.  **Node.js**: Required to run certain MCP servers (like Playwright).
3.  **UV**: Recommended for high-speed dependency management.
    ```bash
    pip install uv
    ```

## Setup & Installation

1.  **Clone the Repository**:
    ```bash
    git clone [https://github.com/your-username/ai-mcp-assistant.git](https://github.com/your-username/ai-mcp-assistant.git)
    cd ai-mcp-assistant
    ```

2.  **Initialize Environment**:
    ```bash
    uv venv
    source .venv/bin/activate  # On Windows: .venv\Scripts\activate
    ```

3.  **Install Dependencies**:
    ```bash
    uv add langchain-groq mcp-use python-dotenv
    ```

4.  **Configure Environment Variables**:
    Create a `.env` file:
    ```env
    GROQ_API_KEY=your_groq_api_key_here
    POSTGRES_URL=your_postgres_connection_string
    ```

5.  **Configure MCP Servers**:
    Define your servers in `mcp_config.json`:
    ```json
    {
      "mcpServers": {
        "postgres": {
          "command": "npx",
          "args": ["-y", "@modelcontextprotocol/server-postgres", "postgresql://user:pass@host:5432/db"]
        },
        "duckduckgo": {
          "command": "npx",
          "args": ["-y", "@modelcontextprotocol/server-duckduckgo"]
        }
      }
    }
    ```

## Usage

Run the main application:
```bash
uv run app.py