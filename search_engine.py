"""
Agentic Search Engine
Combines Google Maps API with AI Agent for intelligent place search
"""

from typing import List, Dict, Optional
from maps_client import MapsClient
from agent import MapsAgent


class AgenticSearchEngine:
    """Main search engine that orchestrates the agentic Google Maps search"""

    def __init__(self, google_api_key: str, anthropic_api_key: str):
        self.maps_client = MapsClient(google_api_key)
        self.agent = MapsAgent(anthropic_api_key)

    def search(
        self,
        query: str,
        location: Optional[str] = None,
        radius: int = 5000,
        max_results: int = 10,
        analyze_reviews: bool = True
    ) -> List[Dict]:
        """
        Perform an agentic search for places

        Args:
            query: Natural language query
            location: Search location
            radius: Search radius in meters
            max_results: Maximum number of results to return
            analyze_reviews: Whether to analyze reviews with AI

        Returns:
            List of places with analysis
        """
        print(f"\n🔍 Searching for: '{query}'")
        print(f"📍 Location: {location or 'Not specified'}")
        print("\n" + "="*60)

        # Step 1: Parse the query using AI
        print("\n🤖 AI Agent: Parsing your query...")
        criteria = self.agent.parse_query(query, location)
        print(f"\n📋 Extracted criteria:")
        print(f"   • Place type: {criteria.get('place_type', 'N/A')}")
        print(f"   • Search query: {criteria.get('search_query', 'N/A')}")
        if criteria.get('price_criteria'):
            print(f"   • Price: {criteria['price_criteria']}")
        if criteria.get('hours_criteria'):
            print(f"   • Hours: {criteria['hours_criteria']}")
        if criteria.get('size_criteria'):
            print(f"   • Size: {criteria['size_criteria']}")
        if criteria.get('other_criteria'):
            print(f"   • Other: {', '.join(criteria['other_criteria'])}")

        # Step 2: Search Google Maps
        print("\n🗺️  Searching Google Maps...")
        search_location = criteria.get('location') or location

        # Determine if we should check for 24 hour places
        open_now = False
        if criteria.get('hours_criteria'):
            hours = criteria['hours_criteria'].lower()
            if 'now' in hours or 'currently' in hours:
                open_now = True

        places = self.maps_client.search_nearby(
            location=search_location,
            keyword=criteria.get('search_query'),
            radius=radius,
            place_type=criteria.get('place_type'),
            open_now=open_now
        )

        if not places:
            print("\n❌ No places found matching your criteria.")
            return []

        print(f"✅ Found {len(places)} potential matches")

        # Step 3: Get detailed information and analyze
        results = []
        print("\n🔬 Analyzing places...")

        for i, place in enumerate(places[:max_results], 1):
            place_id = place.get('place_id')
            place_name = place.get('name', 'Unknown')

            print(f"\n   [{i}/{min(len(places), max_results)}] Analyzing: {place_name}")

            # Get detailed information
            details = self.maps_client.get_place_details(place_id)

            # Merge basic info with details
            full_place = {**place, **details}

            # Analyze reviews if requested
            if analyze_reviews:
                reviews = details.get('reviews', [])
                if reviews:
                    analysis = self.agent.analyze_place_reviews(reviews, criteria)
                else:
                    analysis = {
                        "match_score": 50,
                        "reasoning": "No reviews available for detailed analysis",
                        "price_info": None,
                        "hours_info": None,
                        "size_info": None,
                        "other_info": []
                    }
            else:
                analysis = None

            # Generate summary
            if analysis:
                summary = self.agent.summarize_place(full_place, analysis, criteria)
            else:
                summary = f"{place_name} - {full_place.get('formatted_address', 'N/A')}"

            results.append({
                "place": full_place,
                "analysis": analysis,
                "summary": summary,
                "criteria": criteria
            })

        # Step 4: Sort by match score
        if analyze_reviews:
            results.sort(
                key=lambda x: x['analysis']['match_score'] if x['analysis'] else 0,
                reverse=True
            )

        return results

    def display_results(self, results: List[Dict], detailed: bool = False):
        """
        Display search results in a user-friendly format

        Args:
            results: List of search results
            detailed: Whether to show detailed information
        """
        if not results:
            print("\nNo results to display.")
            return

        print("\n" + "="*60)
        print("🎯 SEARCH RESULTS")
        print("="*60)

        for i, result in enumerate(results, 1):
            place = result['place']
            analysis = result['analysis']
            summary = result['summary']

            print(f"\n{i}. {place.get('name', 'Unknown')}")
            print("   " + "-"*56)

            # Match score
            if analysis:
                score = analysis['match_score']
                score_emoji = "🟢" if score >= 70 else "🟡" if score >= 40 else "🔴"
                print(f"   {score_emoji} Match Score: {score}/100")
                print(f"   💭 {analysis['reasoning']}")

            # Basic info
            print(f"\n   📍 {place.get('formatted_address') or place.get('vicinity', 'N/A')}")

            rating = place.get('rating')
            if rating:
                stars = "⭐" * int(rating)
                total_ratings = place.get('user_ratings_total', 0)
                print(f"   {stars} {rating}/5 ({total_ratings} reviews)")

            # Hours
            hours = place.get('opening_hours', {})
            if hours.get('open_now') is not None:
                status = "🟢 Open now" if hours['open_now'] else "🔴 Closed now"
                print(f"   {status}")

            # AI Summary
            print(f"\n   📝 AI Summary:")
            print(f"      {summary}")

            if detailed and analysis:
                # Detailed analysis
                if analysis.get('price_info'):
                    print(f"\n   💰 Price Info: {analysis['price_info']}")
                if analysis.get('hours_info'):
                    print(f"   🕐 Hours Info: {analysis['hours_info']}")
                if analysis.get('size_info'):
                    print(f"   📏 Size Info: {analysis['size_info']}")
                if analysis.get('other_info'):
                    print(f"   ℹ️  Other Info:")
                    for info in analysis['other_info']:
                        print(f"      • {info}")

                # Contact info
                if place.get('formatted_phone_number'):
                    print(f"\n   📞 {place['formatted_phone_number']}")
                if place.get('website'):
                    print(f"   🌐 {place['website']}")

                # Hours
                weekday_text = hours.get('weekday_text', [])
                if weekday_text:
                    print(f"\n   🕐 Opening Hours:")
                    for day in weekday_text:
                        print(f"      {day}")

            print()

        print("="*60)
