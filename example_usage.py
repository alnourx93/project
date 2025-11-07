#!/usr/bin/env python3
"""
Example Usage Script
Demonstrates how to use the Agentic Google Maps search engine programmatically
"""

import os
from dotenv import load_dotenv
from search_engine import AgenticSearchEngine


def example_gym_search():
    """Example: Search for a gym with specific criteria"""
    print("\n" + "="*60)
    print("EXAMPLE 1: Gym with specific requirements")
    print("="*60)

    # Load environment variables
    load_dotenv()
    google_api_key = os.getenv('GOOGLE_MAPS_API_KEY')
    anthropic_api_key = os.getenv('ANTHROPIC_API_KEY')

    # Initialize search engine
    engine = AgenticSearchEngine(google_api_key, anthropic_api_key)

    # Perform search
    results = engine.search(
        query="I want a gym that is 300 AED a month and is large and opens 24 hours",
        location="Dubai, UAE",
        radius=5000,  # 5km
        max_results=3,
        analyze_reviews=True
    )

    # Display results
    engine.display_results(results, detailed=True)


def example_restaurant_search():
    """Example: Search for a restaurant"""
    print("\n" + "="*60)
    print("EXAMPLE 2: Restaurant search")
    print("="*60)

    load_dotenv()
    google_api_key = os.getenv('GOOGLE_MAPS_API_KEY')
    anthropic_api_key = os.getenv('ANTHROPIC_API_KEY')

    engine = AgenticSearchEngine(google_api_key, anthropic_api_key)

    results = engine.search(
        query="Find me a family-friendly Italian restaurant with outdoor seating",
        location="Dubai Marina, Dubai",
        radius=3000,
        max_results=3,
        analyze_reviews=True
    )

    engine.display_results(results, detailed=False)


def example_coffee_shop_search():
    """Example: Search for a coffee shop"""
    print("\n" + "="*60)
    print("EXAMPLE 3: Coffee shop for working")
    print("="*60)

    load_dotenv()
    google_api_key = os.getenv('GOOGLE_MAPS_API_KEY')
    anthropic_api_key = os.getenv('ANTHROPIC_API_KEY')

    engine = AgenticSearchEngine(google_api_key, anthropic_api_key)

    results = engine.search(
        query="Coffee shop with good wifi and quiet atmosphere for working",
        location="Downtown Dubai",
        radius=2000,
        max_results=3,
        analyze_reviews=True
    )

    engine.display_results(results, detailed=False)


def example_programmatic_access():
    """Example: Access results programmatically"""
    print("\n" + "="*60)
    print("EXAMPLE 4: Programmatic access to results")
    print("="*60)

    load_dotenv()
    google_api_key = os.getenv('GOOGLE_MAPS_API_KEY')
    anthropic_api_key = os.getenv('ANTHROPIC_API_KEY')

    engine = AgenticSearchEngine(google_api_key, anthropic_api_key)

    results = engine.search(
        query="24 hour pharmacy",
        location="Dubai, UAE",
        radius=5000,
        max_results=5,
        analyze_reviews=True
    )

    # Process results programmatically
    print("\nProcessing results programmatically:\n")

    for i, result in enumerate(results, 1):
        place = result['place']
        analysis = result['analysis']

        # Extract specific data
        name = place.get('name')
        rating = place.get('rating', 'N/A')
        match_score = analysis['match_score'] if analysis else 0
        address = place.get('formatted_address', 'N/A')

        print(f"{i}. {name}")
        print(f"   Rating: {rating}/5")
        print(f"   Match Score: {match_score}/100")
        print(f"   Address: {address}")

        # Check if it has specific features from reviews
        if analysis and analysis.get('hours_info'):
            print(f"   Hours Info: {analysis['hours_info']}")

        print()


if __name__ == "__main__":
    import sys

    # Check if API keys are set
    load_dotenv()
    if not os.getenv('GOOGLE_MAPS_API_KEY') or not os.getenv('ANTHROPIC_API_KEY'):
        print("❌ Error: API keys not found!")
        print("Please set up your .env file first.")
        sys.exit(1)

    # Run examples
    print("\n🤖 Agentic Google Maps - Example Usage\n")

    examples = {
        '1': ('Gym Search', example_gym_search),
        '2': ('Restaurant Search', example_restaurant_search),
        '3': ('Coffee Shop Search', example_coffee_shop_search),
        '4': ('Programmatic Access', example_programmatic_access),
        'all': ('All Examples', None)
    }

    print("Choose an example to run:")
    for key, (name, _) in examples.items():
        print(f"  {key}. {name}")
    print()

    choice = input("Enter choice (1-4 or 'all'): ").strip()

    if choice == 'all':
        example_gym_search()
        input("\nPress Enter to continue to next example...")
        example_restaurant_search()
        input("\nPress Enter to continue to next example...")
        example_coffee_shop_search()
        input("\nPress Enter to continue to next example...")
        example_programmatic_access()
    elif choice in examples and examples[choice][1]:
        examples[choice][1]()
    else:
        print("Invalid choice!")

    print("\n✅ Examples completed!\n")
