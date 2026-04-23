import asyncio
import os

from dotenv import load_dotenv
from langchain_groq import ChatGroq
from mcp_use import MCPAgent, MCPClient


async def run_memory_chat():
    load_dotenv()

    groq_key = os.getenv("GROQ_API_KEY") or os.getenv("GROQAPI_KEY")
    if not groq_key:
        raise RuntimeError("Missing GROQ API key. Set GROQ_API_KEY in your .env file.")
    os.environ["GROQ_API_KEY"] = groq_key

    # Keep model configurable to avoid future deprecation breakages.
    model_name = os.getenv("GROQ_MODEL", "qwen/qwen3-32b")

    config_file = "brower_mcp.json"
    print("Initializing Chat...")
    print(f"Using model: {model_name}")

    client = MCPClient.from_config_file(config_file)
    llm = ChatGroq(model=model_name)

    agent = MCPAgent(
        llm=llm,
        client=client,
        max_steps=15,
        memory_enabled=True,
    )

    print("\n===== Interactive MCP Chat Session =====")
    print("Enter 'exit' or 'quit' to end the session.")
    print("Type 'clear' to clear the chat history.")
    print("==========================================\n")

    try:
        while True:
            user_input = input("\nYou: ")
            if user_input.lower() in ["exit", "quit"]:
                print("\nGoodbye! Thank you for using the MCP Chat.")
                break
            if user_input.lower() == "clear":
                agent.clear_conversation_history()
                print("\nChat history cleared.")
                continue

            print("\nAssistant:", end="", flush=True)

            try:
                response = await agent.run(user_input)
                print(response)
            except Exception as e:
                print(f"\nError: {e}")

    finally:
        if client and client.sessions:
            await client.close_all_sessions()


if __name__ == "__main__":
    asyncio.run(run_memory_chat())