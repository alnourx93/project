#!/usr/bin/env python3
"""
Agentic Google Maps - Main CLI Application
"""

import os
import sys
from dotenv import load_dotenv
from search_engine import AgenticSearchEngine


def print_banner():
    """Print application banner"""
    banner = """
╔═══════════════════════════════════════════════════════════╗
║                                                           ║
║           🤖 AGENTIC GOOGLE MAPS 🗺️                      ║
║                                                           ║
║        AI-Powered Intelligent Place Search                ║
║                                                           ║
╚═══════════════════════════════════════════════════════════╝
    """
    print(banner)


def print_examples():
    """Print example queries"""
    examples = """
💡 Example Queries:

1. "I want a gym that is 300 AED a month and is large and opens 24 hours"

2. "Find me a cheap restaurant that's open late"

3. "I need a coffee shop with good wifi and quiet atmosphere"

4. "Show me a family-friendly restaurant with outdoor seating"

5. "Find a hotel with pool and spa under 500 AED per night"

6. "I want a barbershop that's open on Sundays"
    """
    print(examples)


def main():
    """Main application entry point"""
    # Load environment variables
    load_dotenv()

    google_api_key = os.getenv('GOOGLE_MAPS_API_KEY')
    anthropic_api_key = os.getenv('ANTHROPIC_API_KEY')
    default_location = os.getenv('DEFAULT_LOCATION', 'Dubai, UAE')
    default_radius = int(os.getenv('DEFAULT_RADIUS', '5000'))

    # Check API keys
    if not google_api_key or not anthropic_api_key:
        print("❌ Error: API keys not found!")
        print("\nPlease set up your .env file with:")
        print("  - GOOGLE_MAPS_API_KEY")
        print("  - ANTHROPIC_API_KEY")
        print("\nSee .env.example for reference.")
        sys.exit(1)

    # Initialize search engine
    search_engine = AgenticSearchEngine(google_api_key, anthropic_api_key)

    print_banner()
    print(f"📍 Default location: {default_location}")
    print(f"📏 Default search radius: {default_radius}m ({default_radius/1000}km)")

    # Interactive mode
    while True:
        print("\n" + "─"*60)
        print("\nWhat would you like to search for?")
        print("(Type 'examples' for examples, 'quit' to exit)")
        print()

        user_input = input("🔍 Your query: ").strip()

        if not user_input:
            continue

        if user_input.lower() in ['quit', 'exit', 'q']:
            print("\n👋 Goodbye!\n")
            break

        if user_input.lower() in ['examples', 'example', 'help']:
            print_examples()
            continue

        # Ask for location
        print(f"\n📍 Location (press Enter for '{default_location}'): ", end='')
        location_input = input().strip()
        location = location_input if location_input else default_location

        # Ask for radius
        print(f"📏 Search radius in km (press Enter for {default_radius/1000}km): ", end='')
        radius_input = input().strip()
        try:
            radius = int(float(radius_input) * 1000) if radius_input else default_radius
        except ValueError:
            radius = default_radius
            print(f"   Using default radius: {default_radius/1000}km")

        # Ask for max results
        print("🔢 Max results (press Enter for 5): ", end='')
        max_results_input = input().strip()
        try:
            max_results = int(max_results_input) if max_results_input else 5
        except ValueError:
            max_results = 5
            print("   Using default: 5 results")

        # Perform search
        try:
            results = search_engine.search(
                query=user_input,
                location=location,
                radius=radius,
                max_results=max_results,
                analyze_reviews=True
            )

            # Display results
            if results:
                search_engine.display_results(results, detailed=True)

                # Ask if user wants to see more details
                print("\nWould you like to see full details for a specific place?")
                print("Enter the number (1-{}), or press Enter to continue: ".format(len(results)), end='')
                detail_input = input().strip()

                if detail_input.isdigit():
                    idx = int(detail_input) - 1
                    if 0 <= idx < len(results):
                        result = results[idx]
                        place = result['place']

                        print("\n" + "="*60)
                        print(f"📍 DETAILED VIEW: {place.get('name')}")
                        print("="*60)

                        # Show all available information
                        if place.get('formatted_address'):
                            print(f"\n🏠 Address:\n   {place['formatted_address']}")

                        if place.get('formatted_phone_number'):
                            print(f"\n📞 Phone:\n   {place['formatted_phone_number']}")

                        if place.get('website'):
                            print(f"\n🌐 Website:\n   {place['website']}")

                        if place.get('rating'):
                            print(f"\n⭐ Rating:\n   {place['rating']}/5 ({place.get('user_ratings_total', 0)} reviews)")

                        hours = place.get('opening_hours', {})
                        weekday_text = hours.get('weekday_text', [])
                        if weekday_text:
                            print(f"\n🕐 Opening Hours:")
                            for day in weekday_text:
                                print(f"   {day}")

                        reviews = place.get('reviews', [])
                        if reviews:
                            print(f"\n💬 Recent Reviews:")
                            for i, review in enumerate(reviews[:3], 1):
                                rating = review.get('rating', 'N/A')
                                author = review.get('author_name', 'Anonymous')
                                text = review.get('text', 'No text')
                                print(f"\n   Review {i} - {author} (⭐ {rating}/5):")
                                print(f"   {text[:200]}{'...' if len(text) > 200 else ''}")

                        print("\n" + "="*60)

        except Exception as e:
            print(f"\n❌ Error during search: {e}")
            print("Please try again with a different query.")

    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except KeyboardInterrupt:
        print("\n\n👋 Goodbye!\n")
        sys.exit(0)
