"""
Google Maps API Client
Handles all interactions with Google Maps Places API
"""

import googlemaps
from typing import List, Dict, Optional
import os


class MapsClient:
    """Wrapper for Google Maps Places API"""

    def __init__(self, api_key: str):
        self.client = googlemaps.Client(key=api_key)

    def search_places(
        self,
        query: str,
        location: Optional[str] = None,
        radius: int = 5000,
        place_type: Optional[str] = None
    ) -> List[Dict]:
        """
        Search for places using text search

        Args:
            query: Search query (e.g., "gyms", "restaurants")
            location: Location to search around (address or lat/lng)
            radius: Search radius in meters (default 5km)
            place_type: Type of place (e.g., "gym", "restaurant")

        Returns:
            List of place dictionaries
        """
        try:
            # If location is provided as string, geocode it first
            if location and isinstance(location, str):
                geocode_result = self.client.geocode(location)
                if geocode_result:
                    location = geocode_result[0]['geometry']['location']
                else:
                    print(f"Could not geocode location: {location}")
                    location = None

            # Perform text search
            results = self.client.places(
                query=query,
                location=location,
                radius=radius,
                type=place_type
            )

            return results.get('results', [])

        except Exception as e:
            print(f"Error searching places: {e}")
            return []

    def get_place_details(self, place_id: str) -> Dict:
        """
        Get detailed information about a place

        Args:
            place_id: Google Place ID

        Returns:
            Place details dictionary
        """
        try:
            result = self.client.place(
                place_id=place_id,
                fields=[
                    'name', 'formatted_address', 'formatted_phone_number',
                    'opening_hours', 'website', 'rating', 'reviews',
                    'price_level', 'types', 'geometry', 'photos',
                    'user_ratings_total', 'vicinity'
                ]
            )
            return result.get('result', {})

        except Exception as e:
            print(f"Error getting place details: {e}")
            return {}

    def get_place_reviews(self, place_id: str) -> List[Dict]:
        """
        Get reviews for a specific place

        Args:
            place_id: Google Place ID

        Returns:
            List of review dictionaries
        """
        details = self.get_place_details(place_id)
        return details.get('reviews', [])

    def search_nearby(
        self,
        location: str,
        keyword: Optional[str] = None,
        radius: int = 5000,
        place_type: Optional[str] = None,
        open_now: bool = False
    ) -> List[Dict]:
        """
        Search for nearby places

        Args:
            location: Center location (address or lat/lng)
            keyword: Keyword to match (e.g., "24 hour")
            radius: Search radius in meters
            place_type: Type of place
            open_now: Only return places open now

        Returns:
            List of place dictionaries
        """
        try:
            # Geocode location
            geocode_result = self.client.geocode(location)
            if not geocode_result:
                print(f"Could not geocode location: {location}")
                return []

            location_coords = geocode_result[0]['geometry']['location']

            # Search nearby
            results = self.client.places_nearby(
                location=location_coords,
                keyword=keyword,
                radius=radius,
                type=place_type,
                open_now=open_now
            )

            return results.get('results', [])

        except Exception as e:
            print(f"Error searching nearby places: {e}")
            return []
