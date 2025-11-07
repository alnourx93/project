"""
Agentic Query Parser and Place Analyzer
Uses Claude AI to understand natural language queries and analyze places
"""

import anthropic
import json
from typing import Dict, List, Optional


class MapsAgent:
    """AI Agent for parsing queries and analyzing places"""

    def __init__(self, api_key: str):
        self.client = anthropic.Anthropic(api_key=api_key)

    def parse_query(self, user_query: str, location: Optional[str] = None) -> Dict:
        """
        Parse a natural language query into structured search criteria

        Args:
            user_query: User's natural language query
            location: Optional location context

        Returns:
            Dictionary with search criteria
        """
        prompt = f"""You are a helpful assistant that parses natural language queries about places into structured search criteria.

User query: "{user_query}"
{f'Location context: {location}' if location else ''}

Extract the following information from the query:
1. place_type: What type of place (gym, restaurant, cafe, etc.)
2. keywords: List of keywords to search for
3. price_criteria: Any price-related requirements (e.g., "300 AED per month", "cheap", "expensive")
4. hours_criteria: Operating hours requirements (e.g., "24 hours", "open late", "open now")
5. size_criteria: Size requirements (e.g., "large", "small", "spacious")
6. other_criteria: Any other specific requirements (e.g., "has pool", "parking", "family-friendly")
7. location: Specific location mentioned (if any)
8. search_query: A concise search query for Google Maps

Return ONLY a valid JSON object with these fields. Use null for any fields that aren't specified.

Example response:
{{
    "place_type": "gym",
    "keywords": ["gym", "fitness center"],
    "price_criteria": "300 AED per month",
    "hours_criteria": "24 hours",
    "size_criteria": "large",
    "other_criteria": [],
    "location": null,
    "search_query": "24 hour gym"
}}
"""

        try:
            message = self.client.messages.create(
                model="claude-3-5-sonnet-20241022",
                max_tokens=1024,
                messages=[{"role": "user", "content": prompt}]
            )

            response_text = message.content[0].text
            # Extract JSON from response
            criteria = json.loads(response_text)
            return criteria

        except Exception as e:
            print(f"Error parsing query: {e}")
            return {
                "place_type": None,
                "keywords": [user_query],
                "price_criteria": None,
                "hours_criteria": None,
                "size_criteria": None,
                "other_criteria": [],
                "location": None,
                "search_query": user_query
            }

    def analyze_place_reviews(
        self,
        reviews: List[Dict],
        criteria: Dict
    ) -> Dict:
        """
        Analyze reviews to check if place matches specific criteria

        Args:
            reviews: List of review dictionaries
            criteria: Search criteria from parse_query

        Returns:
            Analysis results with match score and reasoning
        """
        if not reviews:
            return {
                "match_score": 0,
                "reasoning": "No reviews available",
                "price_info": None,
                "hours_info": None,
                "size_info": None,
                "other_info": []
            }

        # Combine reviews into text
        reviews_text = "\n\n".join([
            f"Rating: {r.get('rating', 'N/A')}/5\n{r.get('text', '')}"
            for r in reviews[:10]  # Limit to first 10 reviews
        ])

        criteria_text = json.dumps(criteria, indent=2)

        prompt = f"""Analyze these Google Maps reviews to determine if this place matches the user's criteria.

USER CRITERIA:
{criteria_text}

REVIEWS:
{reviews_text}

Based on the reviews, determine:
1. Does this place match the price criteria? Extract any price information mentioned.
2. Does it match the hours criteria? Extract any hours information mentioned.
3. Does it match the size criteria? Extract any size/space information mentioned.
4. Does it match other criteria? Extract relevant information.
5. Overall match score (0-100)
6. Brief reasoning for the score

Return ONLY a valid JSON object:
{{
    "match_score": 85,
    "reasoning": "Brief explanation of why this score",
    "price_info": "Price information found in reviews or null",
    "hours_info": "Hours information found in reviews or null",
    "size_info": "Size information found in reviews or null",
    "other_info": ["other relevant points from reviews"]
}}
"""

        try:
            message = self.client.messages.create(
                model="claude-3-5-sonnet-20241022",
                max_tokens=1024,
                messages=[{"role": "user", "content": prompt}]
            )

            response_text = message.content[0].text
            analysis = json.loads(response_text)
            return analysis

        except Exception as e:
            print(f"Error analyzing reviews: {e}")
            return {
                "match_score": 0,
                "reasoning": f"Error analyzing reviews: {e}",
                "price_info": None,
                "hours_info": None,
                "size_info": None,
                "other_info": []
            }

    def summarize_place(
        self,
        place: Dict,
        analysis: Dict,
        criteria: Dict
    ) -> str:
        """
        Generate a natural language summary of a place

        Args:
            place: Place details from Google Maps
            analysis: Analysis results from analyze_place_reviews
            criteria: Original search criteria

        Returns:
            Natural language summary
        """
        place_info = {
            "name": place.get('name'),
            "address": place.get('formatted_address') or place.get('vicinity'),
            "rating": place.get('rating'),
            "total_ratings": place.get('user_ratings_total'),
            "hours": place.get('opening_hours', {}).get('weekday_text', []),
            "phone": place.get('formatted_phone_number'),
            "website": place.get('website')
        }

        prompt = f"""Create a concise, helpful summary of this place for a user searching based on these criteria.

SEARCH CRITERIA:
{json.dumps(criteria, indent=2)}

PLACE INFORMATION:
{json.dumps(place_info, indent=2)}

ANALYSIS RESULTS:
{json.dumps(analysis, indent=2)}

Create a 2-3 sentence summary highlighting:
1. The place name and what it is
2. How well it matches the criteria (mention the match score)
3. Key relevant details from reviews and place info (price, hours, size if available)

Be conversational and helpful. If information is missing, mention it.
"""

        try:
            message = self.client.messages.create(
                model="claude-3-5-sonnet-20241022",
                max_tokens=512,
                messages=[{"role": "user", "content": prompt}]
            )

            return message.content[0].text.strip()

        except Exception as e:
            print(f"Error generating summary: {e}")
            name = place.get('name', 'Unknown')
            rating = place.get('rating', 'N/A')
            address = place.get('formatted_address') or place.get('vicinity', 'N/A')
            return f"{name} (Rating: {rating}/5) - {address}"
