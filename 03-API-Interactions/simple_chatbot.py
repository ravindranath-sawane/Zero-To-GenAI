"""
Simple Chatbot with Conversation Memory
========================================

This script demonstrates how to build a chatbot using the OpenAI API directly.
The key concept here is CONVERSATION HISTORY - without it, the model has NO memory!

Key Concepts:
- LLMs are STATELESS: Each API call is independent
- To create "memory", we must send the ENTIRE conversation history with each request
- The conversation_history list accumulates all messages (user + assistant)

Author: Zero-To-GenAI Course
"""

import os
from dotenv import load_dotenv
from openai import OpenAI

# ===========================================
# SETUP
# ===========================================

# Load API key from .env file
load_dotenv()

# Initialize the OpenAI client
client = OpenAI()  # Automatically uses OPENAI_API_KEY from environment

# ===========================================
# THE CRUCIAL PART: CONVERSATION HISTORY
# ===========================================

# This list stores the entire conversation.
# WITHOUT THIS, THE MODEL HAS NO MEMORY OF PREVIOUS MESSAGES!
# 
# Why? Because:
# 1. Each API call to OpenAI is completely independent (stateless)
# 2. The model doesn't "remember" what you said before
# 3. We must send ALL previous messages with each new request
# 4. This is how ChatGPT works behind the scenes too!

conversation_history = [
    {
        "role": "system",
        "content": "You are a helpful, friendly AI assistant. Keep responses concise but informative."
    }
]


def chat(user_message: str) -> str:
    """
    Send a message to the AI and get a response.
    
    This function:
    1. Adds the user's message to conversation_history
    2. Sends the ENTIRE history to the API
    3. Gets the response and adds it to history
    4. Returns the response
    
    Args:
        user_message: What the user typed
        
    Returns:
        The AI's response
    """
    
    # Step 1: Add the user's message to history
    conversation_history.append({
        "role": "user",
        "content": user_message
    })
    
    # Step 2: Send the ENTIRE conversation history to OpenAI
    # This is what gives the model "memory" - it sees all previous messages!
    response = client.chat.completions.create(
        model="gpt-4o-mini",  # Cost-effective model for learning
        messages=conversation_history,  # <-- THE ENTIRE HISTORY!
        temperature=0.7
    )
    
    # Step 3: Extract the assistant's response
    assistant_message = response.choices[0].message.content
    
    # Step 4: Add the assistant's response to history (for future turns)
    conversation_history.append({
        "role": "assistant",
        "content": assistant_message
    })
    
    return assistant_message


def main():
    """Main function to run the chatbot loop."""
    
    print("=" * 60)
    print("🤖 Simple Chatbot with Memory")
    print("=" * 60)
    print("This chatbot remembers your conversation!")
    print("Try telling it your name, then ask 'What is my name?' later.")
    print("Type 'quit' or 'exit' to end the conversation.")
    print("Type 'history' to see the full conversation history.")
    print("=" * 60)
    print()
    
    # Main conversation loop
    while True:
        # Get user input
        try:
            user_input = input("👤 You: ").strip()
        except (KeyboardInterrupt, EOFError):
            print("\n\n👋 Goodbye!")
            break
        
        # Check for exit commands
        if user_input.lower() in ['quit', 'exit', 'q']:
            print("\n👋 Goodbye! Thanks for chatting!")
            break
        
        # Check for empty input
        if not user_input:
            print("💭 (Please type something...)\n")
            continue
        
        # Special command: show conversation history
        if user_input.lower() == 'history':
            print("\n📜 Conversation History:")
            print("-" * 40)
            for i, msg in enumerate(conversation_history):
                role = msg['role'].upper()
                content = msg['content'][:100] + "..." if len(msg['content']) > 100 else msg['content']
                print(f"{i+1}. [{role}]: {content}")
            print("-" * 40)
            print()
            continue
        
        # Get AI response
        try:
            response = chat(user_input)
            print(f"🤖 AI: {response}\n")
        except Exception as e:
            print(f"❌ Error: {e}\n")
            print("Make sure your OPENAI_API_KEY is set correctly in .env\n")


# ===========================================
# WHAT HAPPENS WITHOUT CONVERSATION HISTORY?
# ===========================================
#
# If we sent ONLY the current user message (not the history), this would happen:
#
# User: "My name is Alice"
# AI: "Nice to meet you, Alice!"
#
# User: "What is my name?"
# AI: "I don't know your name. You haven't told me."  <-- NO MEMORY!
#
# By maintaining conversation_history and sending it with each request,
# the model can "see" that you previously said your name was Alice.
#
# This is a FUNDAMENTAL concept in building LLM applications!


if __name__ == "__main__":
    main()
