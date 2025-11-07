#!/usr/bin/env python3
"""
Interactive Demo - Agentic Google Maps
Test with your own queries using mock data
"""

import sys
from demo import DemoSearchEngine


def print_banner():
    print("""
╔═══════════════════════════════════════════════════════════╗
║                                                           ║
║     🤖 AGENTIC GOOGLE MAPS 🗺️ - INTERACTIVE DEMO        ║
║                                                           ║
║        AI-Powered Intelligent Place Search                ║
║          (No API Keys Required - Mock Data)               ║
║                                                           ║
╚═══════════════════════════════════════════════════════════╝
    """)


def print_examples():
    print("""
💡 Example Queries to Try:

1. "I want a gym that is 300 AED a month and is large and opens 24 hours"

2. "Find me a gym that's open 24/7"

3. "I need a large fitness center"

4. "Show me gyms under 300 AED per month"

Note: This demo uses mock gym data from Dubai. The AI agent
will parse your query and analyze the mock reviews!
    """)


def main():
    print_banner()
    print("ℹ️  This is a DEMO using mock data - no API keys needed!")
    print("   Try different queries to see how the AI understands them.\n")

    engine = DemoSearchEngine()

    while True:
        print("\n" + "─"*60)
        print("\nWhat would you like to search for?")
        print("(Type 'examples' for ideas, 'quit' to exit)")
        print()

        user_input = input("🔍 Your query: ").strip()

        if not user_input:
            continue

        if user_input.lower() in ['quit', 'exit', 'q']:
            print("\n👋 Thanks for trying the demo!\n")
            print("Ready for the real thing? Set up API keys and run: python main.py")
            break

        if user_input.lower() in ['examples', 'example', 'help']:
            print_examples()
            continue

        # Ask for location
        print(f"\n📍 Location (press Enter for 'Dubai, UAE'): ", end='')
        location_input = input().strip()
        location = location_input if location_input else "Dubai, UAE"

        # Ask for max results
        print("🔢 Max results (press Enter for 3): ", end='')
        max_results_input = input().strip()
        try:
            max_results = int(max_results_input) if max_results_input else 3
        except ValueError:
            max_results = 3

        # Perform search
        try:
            results = engine.search(
                query=user_input,
                location=location,
                radius=5000,
                max_results=max_results,
                analyze_reviews=True
            )

            # Display results
            engine.display_results(results, detailed=True)

            # Explain what happened
            print("\n" + "="*60)
            print("🎓 WHAT JUST HAPPENED:")
            print("="*60)
            print("""
1. The AI agent parsed your natural language query
2. It extracted key criteria (price, hours, size, etc.)
3. It searched mock gym data (simulating Google Maps)
4. It analyzed reviews to find matching information
5. It calculated a match score for each place
6. Results were ranked by relevance

In the REAL version with API keys:
• Searches actual Google Maps data
• Analyzes real user reviews
• Works for ANY type of place (restaurants, hotels, etc.)
• Covers the entire world, not just mock data
            """)

        except Exception as e:
            print(f"\n❌ Error: {e}")
            import traceback
            traceback.print_exc()

    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except KeyboardInterrupt:
        print("\n\n👋 Demo ended!\n")
        sys.exit(0)
