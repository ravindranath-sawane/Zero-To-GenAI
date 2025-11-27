"""
CLI Research Assistant
======================

A command-line tool that uses AI to research and summarize any topic.
Results are saved as a Markdown file for easy reading and sharing.

Usage:
    python cli_researcher.py --topic "Black Holes"
    python cli_researcher.py --topic "Quantum Computing" --bullets 5
    python cli_researcher.py -t "Machine Learning" -b 3

Author: Zero-To-GenAI Course
"""

import argparse
import os
import re
import sys
from datetime import datetime
from typing import Optional

from dotenv import load_dotenv
from openai import OpenAI, OpenAIError


# ===========================================
# CONFIGURATION
# ===========================================

# Load API key from .env file
load_dotenv()

# Verify API key exists
if not os.getenv("OPENAI_API_KEY"):
    print("❌ ERROR: OPENAI_API_KEY not found!")
    print("Please create a .env file with your API key:")
    print("  OPENAI_API_KEY=sk-your-key-here")
    sys.exit(1)

# Initialize OpenAI client
client = OpenAI()


# ===========================================
# SYSTEM PROMPT
# ===========================================

SYSTEM_PROMPT = """You are an expert researcher with deep knowledge across many fields.

Your task is to provide a clear, accurate, and well-structured summary of the given topic.

Follow this EXACT output format:

# [Topic Name]

## Summary
[A 2-3 sentence overview of the topic]

## Key Points
- [Bullet point 1: A key fact or concept]
- [Bullet point 2: Another important aspect]
- [Bullet point 3: A third significant point]
[Add more bullets if requested]

## Why It Matters
[1-2 sentences on the significance or applications of this topic]

## Learn More
[Suggest 1-2 areas for further exploration]

Guidelines:
- Be concise but informative
- Use simple language accessible to beginners
- Include specific facts, numbers, or examples where relevant
- Avoid jargon unless you explain it
"""


# ===========================================
# CORE FUNCTIONS
# ===========================================

def research_topic(topic: str, num_bullets: int = 3) -> Optional[str]:
    """
    Use AI to research and summarize a topic.
    
    Args:
        topic: The topic to research
        num_bullets: Number of key points to generate
    
    Returns:
        Markdown-formatted research summary, or None if failed
    """
    
    # Customize prompt based on number of bullets
    user_prompt = f"""Research and summarize the following topic: {topic}

Please provide exactly {num_bullets} key bullet points in the "Key Points" section.

Make the summary informative yet accessible to someone new to this topic."""

    try:
        # Call the OpenAI API
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": user_prompt}
            ],
            temperature=0.7,  # Balanced creativity
            max_tokens=1000   # Reasonable limit for summaries
        )
        
        # Extract the response content
        content = response.choices[0].message.content
        return content
        
    except OpenAIError as e:
        print(f"❌ OpenAI API Error: {e}")
        return None
    except Exception as e:
        print(f"❌ Unexpected Error: {e}")
        return None


def sanitize_filename(topic: str) -> str:
    """
    Convert a topic string into a safe filename.
    
    Args:
        topic: The original topic string
    
    Returns:
        A safe filename string
    """
    # Remove or replace unsafe characters
    safe_name = re.sub(r'[<>:"/\\|?*]', '', topic)
    # Replace spaces with underscores
    safe_name = safe_name.replace(' ', '_')
    # Limit length
    safe_name = safe_name[:50]
    # Ensure it's not empty
    return safe_name or "research"


def save_to_markdown(content: str, topic: str, output_dir: str = ".") -> str:
    """
    Save the research content to a Markdown file.
    
    Args:
        content: The markdown content to save
        topic: The topic (used for filename)
        output_dir: Directory to save the file
    
    Returns:
        The path to the saved file
    """
    # Create safe filename
    filename = f"{sanitize_filename(topic)}.md"
    filepath = os.path.join(output_dir, filename)
    
    # Add metadata header
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    header = f"""---
topic: {topic}
generated: {timestamp}
model: gpt-4o-mini
---

"""
    
    # Write to file
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(header + content)
    
    return filepath


# ===========================================
# CLI INTERFACE
# ===========================================

def create_parser() -> argparse.ArgumentParser:
    """Create the argument parser for the CLI."""
    
    parser = argparse.ArgumentParser(
        description="🔬 CLI Research Assistant - AI-powered topic summarization",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python cli_researcher.py --topic "Black Holes"
  python cli_researcher.py --topic "Quantum Computing" --bullets 5
  python cli_researcher.py -t "Climate Change" -o ./research/

Part of the Zero-To-GenAI course.
        """
    )
    
    parser.add_argument(
        "-t", "--topic",
        type=str,
        required=True,
        help="The topic to research (e.g., 'Machine Learning')"
    )
    
    parser.add_argument(
        "-b", "--bullets",
        type=int,
        default=3,
        help="Number of key points to generate (default: 3)"
    )
    
    parser.add_argument(
        "-o", "--output",
        type=str,
        default=".",
        help="Output directory for the markdown file (default: current directory)"
    )
    
    parser.add_argument(
        "-p", "--print-only",
        action="store_true",
        help="Print to console only, don't save to file"
    )
    
    return parser


def main():
    """Main entry point for the CLI."""
    
    # Parse arguments
    parser = create_parser()
    args = parser.parse_args()
    
    # Validate arguments
    if args.bullets < 1 or args.bullets > 10:
        print("❌ Error: Number of bullets must be between 1 and 10")
        sys.exit(1)
    
    # Create output directory if it doesn't exist
    if not args.print_only and not os.path.exists(args.output):
        os.makedirs(args.output)
    
    # Header
    print("=" * 60)
    print("🔬 CLI Research Assistant")
    print("=" * 60)
    print(f"📚 Topic: {args.topic}")
    print(f"📝 Key Points: {args.bullets}")
    print()
    print("🤖 Researching... (this may take a few seconds)")
    print()
    
    # Perform research
    result = research_topic(args.topic, args.bullets)
    
    if result is None:
        print("❌ Failed to generate research. Please try again.")
        sys.exit(1)
    
    # Display result
    print("=" * 60)
    print("📄 RESEARCH RESULTS")
    print("=" * 60)
    print()
    print(result)
    print()
    
    # Save to file (unless print-only mode)
    if not args.print_only:
        try:
            filepath = save_to_markdown(result, args.topic, args.output)
            print("=" * 60)
            print(f"✅ Saved to: {filepath}")
            print("=" * 60)
        except IOError as e:
            print(f"❌ Error saving file: {e}")
            sys.exit(1)
    
    print("\n🎉 Research complete!")


if __name__ == "__main__":
    main()


# ===========================================
# FUTURE EXTENSIONS: WEB SEARCH INTEGRATION
# ===========================================
#
# This basic researcher uses only the LLM's training knowledge.
# To make it a TRUE research assistant, you could add web search!
#
# Option 1: Tavily API (Recommended for AI applications)
# -------------------------------------------------------
# Tavily is designed specifically for AI agents and provides
# clean, structured search results.
#
# Installation:
#   pip install tavily-python
#
# Usage:
#   from tavily import TavilyClient
#   
#   tavily = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))
#   
#   def search_web(query: str) -> str:
#       """Search the web for current information."""
#       results = tavily.search(query=query, max_results=5)
#       
#       # Format results for the LLM
#       context = ""
#       for result in results['results']:
#           context += f"Source: {result['url']}\n"
#           context += f"Content: {result['content']}\n\n"
#       
#       return context
#   
#   # Then modify research_topic() to include web context:
#   web_context = search_web(topic)
#   user_prompt = f"""
#   Use this current information from the web:
#   {web_context}
#   
#   Research and summarize: {topic}
#   """
#
#
# Option 2: Serper API (Google Search results)
# ---------------------------------------------
# Serper provides Google Search results via API.
#
# Installation:
#   pip install google-serper
#
# Usage:
#   import requests
#   
#   def search_google(query: str) -> str:
#       """Search Google for current information."""
#       url = "https://google.serper.dev/search"
#       headers = {"X-API-KEY": os.getenv("SERPER_API_KEY")}
#       payload = {"q": query}
#       
#       response = requests.post(url, headers=headers, json=payload)
#       results = response.json()
#       
#       # Format organic results
#       context = ""
#       for item in results.get('organic', [])[:5]:
#           context += f"Title: {item['title']}\n"
#           context += f"Snippet: {item['snippet']}\n\n"
#       
#       return context
#
#
# Option 3: LangChain Tools (More integrated)
# -------------------------------------------
# LangChain has built-in tool integrations for search.
#
#   from langchain_community.tools import TavilySearchResults
#   from langchain.agents import create_react_agent
#   
#   search_tool = TavilySearchResults()
#   tools = [search_tool]
#   
#   # Create an agent that can decide when to search
#   agent = create_react_agent(llm, tools, prompt)
#
#
# Benefits of adding web search:
# - Access to current/real-time information
# - Fact-checking against multiple sources
# - Links to sources for verification
# - More comprehensive research
#
# ===========================================
