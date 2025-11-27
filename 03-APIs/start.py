"""
Basic API Call Demo using OpenAI and python-dotenv

This script demonstrates how to:
1. Load environment variables from a .env file
2. Initialize the OpenAI client
3. Make a basic API call to generate text

Prerequisites:
- Create a .env file in the project root with your API key:
  OPENAI_API_KEY=your-api-key-here
- Install dependencies: pip install -r requirements.txt
"""

import os
import sys
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables from .env file
load_dotenv()

# Get API key from environment
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    print("Error: OPENAI_API_KEY not found in environment variables.")
    print("Please create a .env file with your API key:")
    print("  OPENAI_API_KEY=your-api-key-here")
    sys.exit(1)

# Initialize the OpenAI client
client = OpenAI(api_key=api_key)

# Make a basic API call
try:
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Hello! What is Generative AI in one sentence?"}
        ],
        max_tokens=100
    )
    
    # Print the response
    print("Response from OpenAI:")
    print(response.choices[0].message.content)

except Exception as e:
    print(f"Error making API call: {e}")
