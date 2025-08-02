from util import llm
from util import send_email  # Use your improved send_email tool
from langgraph.prebuilt import create_react_agent

def run_interactive_agent():
    """Interactive chat loop for testing"""
    tools = [send_email]
    model = llm 
    
    system_message = """You are a helpful AI assistant. Dont make tool calls for the answers u can answer directly"""
    
    agent = create_react_agent(
        model=model,
        tools=tools,
        system_message=system_message
    )
    
    print("Chat with the agent (type 'quit' to exit):")
    
    while True:
        user_input = input("\nYou: ").strip()
        if user_input.lower() in ['quit', 'exit', 'bye']:
            print("Goodbye!")
            break
            
        try:
            res = agent.invoke(
                {"messages": [{"role": "user", "content": user_input}]}
            )
            print("Agent:", res['messages'][-1].content)
        except Exception as e:
            print(f"Error: {str(e)}")

if __name__ == "__main__":
    # Test with simple greeting first
    print("=== Testing simple greeting ===")
    run_interactive_agent()
