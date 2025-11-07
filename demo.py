#!/usr/bin/env python3
"""
Demo Version - Agentic Google Maps
Uses mock data to demonstrate functionality without requiring API keys
"""

import random
import time


class MockMapsClient:
    """Mock Google Maps client with sample data"""

    def __init__(self):
        self.gyms = [
            {
                "place_id": "gym1",
                "name": "FitZone 24/7 Gym",
                "rating": 4.5,
                "user_ratings_total": 342,
                "vicinity": "Sheikh Zayed Road, Dubai",
                "formatted_address": "Sheikh Zayed Road, Dubai, UAE",
                "reviews": [
                    {"rating": 5, "text": "Great gym! It's open 24 hours which is perfect for my schedule. The place is huge with lots of equipment. Membership costs around 299 AED per month which is very reasonable."},
                    {"rating": 4, "text": "Large facility with modern equipment. I pay 300 AED monthly and it's worth it. Always open when I need it."},
                    {"rating": 5, "text": "Best 24-hour gym in the area. Spacious, clean, and the price is competitive at 300 dirhams per month."},
                ],
                "opening_hours": {
                    "open_now": True,
                    "weekday_text": ["Monday: Open 24 hours", "Tuesday: Open 24 hours", "Wednesday: Open 24 hours",
                                     "Thursday: Open 24 hours", "Friday: Open 24 hours", "Saturday: Open 24 hours", "Sunday: Open 24 hours"]
                },
                "formatted_phone_number": "+971 4 123 4567",
                "website": "https://fitzone24.ae"
            },
            {
                "place_id": "gym2",
                "name": "PowerLift Fitness Center",
                "rating": 4.2,
                "user_ratings_total": 156,
                "vicinity": "Dubai Marina, Dubai",
                "formatted_address": "Dubai Marina, Dubai, UAE",
                "reviews": [
                    {"rating": 4, "text": "Good gym but a bit expensive at 450 AED per month. Not open 24 hours unfortunately, closes at 11 PM."},
                    {"rating": 3, "text": "Decent equipment but the space is cramped during peak hours. Worth the money if you go off-peak."},
                    {"rating": 5, "text": "Love this gym! Great trainers and equipment."},
                ],
                "opening_hours": {
                    "open_now": True,
                    "weekday_text": ["Monday: 6:00 AM – 11:00 PM", "Tuesday: 6:00 AM – 11:00 PM", "Wednesday: 6:00 AM – 11:00 PM",
                                     "Thursday: 6:00 AM – 11:00 PM", "Friday: 6:00 AM – 11:00 PM", "Saturday: 8:00 AM – 10:00 PM", "Sunday: 8:00 AM – 10:00 PM"]
                },
                "formatted_phone_number": "+971 4 234 5678",
                "website": "https://powerlift.ae"
            },
            {
                "place_id": "gym3",
                "name": "Mega Fitness Arena",
                "rating": 4.7,
                "user_ratings_total": 523,
                "vicinity": "Business Bay, Dubai",
                "formatted_address": "Business Bay, Dubai, UAE",
                "reviews": [
                    {"rating": 5, "text": "Massive gym with everything you need! Open 24/7 and only 295 AED monthly. Best value in Dubai!"},
                    {"rating": 5, "text": "This place is enormous! Three floors of equipment. Always open and great price at under 300 dirhams."},
                    {"rating": 4, "text": "Very large facility, never crowded. The 24-hour access is fantastic and the monthly fee of 300 AED is reasonable."},
                ],
                "opening_hours": {
                    "open_now": True,
                    "weekday_text": ["Monday: Open 24 hours", "Tuesday: Open 24 hours", "Wednesday: Open 24 hours",
                                     "Thursday: Open 24 hours", "Friday: Open 24 hours", "Saturday: Open 24 hours", "Sunday: Open 24 hours"]
                },
                "formatted_phone_number": "+971 4 345 6789",
                "website": "https://megafitness.ae"
            },
        ]

    def search_nearby(self, location, keyword, radius, place_type, open_now):
        """Mock search that returns sample gyms"""
        time.sleep(0.5)  # Simulate API delay
        return self.gyms

    def get_place_details(self, place_id):
        """Mock place details"""
        for gym in self.gyms:
            if gym["place_id"] == place_id:
                return gym
        return {}


class MockMapsAgent:
    """Mock AI agent that simulates Claude's responses"""

    def parse_query(self, user_query, location=None):
        """Mock query parsing"""
        print("   🤖 Analyzing query with AI...")
        time.sleep(0.3)

        # Simple keyword-based parsing for demo
        criteria = {
            "place_type": "gym",
            "keywords": ["gym", "fitness"],
            "price_criteria": None,
            "hours_criteria": None,
            "size_criteria": None,
            "other_criteria": [],
            "location": location,
            "search_query": "gym"
        }

        query_lower = user_query.lower()

        if "300 aed" in query_lower or "300" in query_lower:
            criteria["price_criteria"] = "300 AED per month"

        if "24 hour" in query_lower or "24/7" in query_lower or "24 hours" in query_lower:
            criteria["hours_criteria"] = "24 hours"

        if "large" in query_lower or "big" in query_lower or "spacious" in query_lower:
            criteria["size_criteria"] = "large"

        return criteria

    def analyze_place_reviews(self, reviews, criteria):
        """Mock review analysis"""
        time.sleep(0.3)

        # Simple scoring based on reviews
        score = 50
        price_info = None
        hours_info = None
        size_info = None
        other_info = []

        for review in reviews:
            text = review.get('text', '').lower()

            # Check price criteria
            if criteria.get('price_criteria'):
                if '300' in text or '299' in text or '295' in text:
                    score += 20
                    price_info = "Around 300 AED per month mentioned in reviews"
                elif '450' in text or 'expensive' in text:
                    score -= 10
                    price_info = "More expensive, around 450 AED per month"

            # Check hours criteria
            if criteria.get('hours_criteria'):
                if '24 hour' in text or '24/7' in text or 'always open' in text:
                    score += 20
                    hours_info = "Open 24 hours according to reviews"
                elif 'closes at' in text or '11 pm' in text:
                    score -= 10
                    hours_info = "Not open 24 hours"

            # Check size criteria
            if criteria.get('size_criteria'):
                if 'large' in text or 'huge' in text or 'massive' in text or 'enormous' in text:
                    score += 15
                    size_info = "Described as large/spacious in reviews"
                elif 'cramped' in text or 'small' in text:
                    score -= 10
                    size_info = "Some reviewers mention it can be cramped"

        score = min(100, max(0, score))

        reasoning = f"Based on review analysis: "
        reasons = []
        if price_info:
            reasons.append("price matches criteria" if score > 60 else "price doesn't match well")
        if hours_info:
            reasons.append("hours match criteria" if score > 60 else "hours don't match")
        if size_info:
            reasons.append("size matches criteria" if score > 60 else "size mentioned")

        reasoning += ", ".join(reasons) if reasons else "general assessment based on reviews"

        return {
            "match_score": score,
            "reasoning": reasoning,
            "price_info": price_info,
            "hours_info": hours_info,
            "size_info": size_info,
            "other_info": other_info
        }

    def summarize_place(self, place, analysis, criteria):
        """Mock summary generation"""
        name = place.get('name')
        rating = place.get('rating')
        score = analysis.get('match_score', 0)

        summary = f"{name} (Rating: {rating}/5) is a "

        if score >= 80:
            summary += "excellent match"
        elif score >= 60:
            summary += "good match"
        else:
            summary += "partial match"

        summary += f" with a score of {score}/100. "

        if analysis.get('price_info'):
            summary += f"{analysis['price_info']}. "
        if analysis.get('hours_info'):
            summary += f"{analysis['hours_info']}. "

        return summary


class DemoSearchEngine:
    """Demo search engine using mock data"""

    def __init__(self):
        self.maps_client = MockMapsClient()
        self.agent = MockMapsAgent()

    def search(self, query, location=None, radius=5000, max_results=10, analyze_reviews=True):
        """Perform demo search"""
        print(f"\n🔍 Searching for: '{query}'")
        print(f"📍 Location: {location or 'Not specified'}")
        print("\n" + "="*60)

        # Parse query
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

        # Search places
        print("\n🗺️  Searching Google Maps (Demo Mode)...")
        places = self.maps_client.search_nearby(
            location=location,
            keyword=criteria.get('search_query'),
            radius=radius,
            place_type=criteria.get('place_type'),
            open_now=False
        )

        print(f"✅ Found {len(places)} potential matches")

        # Analyze places
        results = []
        print("\n🔬 Analyzing places...")

        for i, place in enumerate(places[:max_results], 1):
            place_id = place.get('place_id')
            place_name = place.get('name', 'Unknown')

            print(f"\n   [{i}/{min(len(places), max_results)}] Analyzing: {place_name}")

            details = self.maps_client.get_place_details(place_id)
            full_place = {**place, **details}

            if analyze_reviews:
                reviews = details.get('reviews', [])
                analysis = self.agent.analyze_place_reviews(reviews, criteria)
            else:
                analysis = None

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

        # Sort by match score
        if analyze_reviews:
            results.sort(
                key=lambda x: x['analysis']['match_score'] if x['analysis'] else 0,
                reverse=True
            )

        return results

    def display_results(self, results, detailed=False):
        """Display results"""
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
            print(f"\n   📍 {place.get('formatted_address', 'N/A')}")

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

                # Sample reviews
                reviews = place.get('reviews', [])
                if reviews:
                    print(f"\n   💬 Sample Reviews:")
                    for j, review in enumerate(reviews[:2], 1):
                        rating_stars = "⭐" * review.get('rating', 0)
                        text = review.get('text', '')[:150]
                        print(f"      {j}. {rating_stars}")
                        print(f"         {text}...")

            print()

        print("="*60)


def main():
    """Demo main function"""
    print("""
╔═══════════════════════════════════════════════════════════╗
║                                                           ║
║           🤖 AGENTIC GOOGLE MAPS 🗺️ - DEMO              ║
║                                                           ║
║        AI-Powered Intelligent Place Search                ║
║              (Running in Demo Mode)                       ║
║                                                           ║
╚═══════════════════════════════════════════════════════════╝

ℹ️  This is a DEMO version using mock data.
   No API keys required - see how the system works!

📝 Demo Query: "I want a gym that is 300 AED a month
                and is large and opens 24 hours"

📍 Location: Dubai, UAE
    """)

    # Initialize demo engine
    engine = DemoSearchEngine()

    # Run demo search
    results = engine.search(
        query="I want a gym that is 300 AED a month and is large and opens 24 hours",
        location="Dubai, UAE",
        radius=5000,
        max_results=3,
        analyze_reviews=True
    )

    # Display results
    engine.display_results(results, detailed=True)

    print("\n" + "="*60)
    print("💡 HOW IT WORKS:")
    print("="*60)
    print("""
1. 🤖 AI Agent parses your natural language query
   → Extracted: gym, 300 AED, 24 hours, large

2. 🗺️  Searches Google Maps for matching places
   → Found gyms in the area

3. 🔬 AI analyzes reviews for each place
   → Looks for price, hours, size mentions
   → Calculates match score (0-100)

4. 📊 Ranks results by relevance
   → Best matches shown first
   → Detailed reasoning provided

5. ✨ Displays results with all details
   → Ratings, reviews, contact info
   → AI-generated summaries
    """)

    print("\n" + "="*60)
    print("🚀 READY TO USE THE REAL VERSION?")
    print("="*60)
    print("""
1. Get API keys:
   • Google Maps: https://console.cloud.google.com/
   • Anthropic: https://console.anthropic.com/

2. Set up .env file:
   cp .env.example .env
   # Add your API keys

3. Run the real version:
   python main.py

📖 See README.md for detailed setup instructions.
    """)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n👋 Demo ended!\n")
