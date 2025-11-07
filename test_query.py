#!/usr/bin/env python3
"""
Quick test with custom query
"""
import sys
from demo import DemoSearchEngine

if len(sys.argv) < 2:
    print("Usage: python test_query.py \"your search query here\"")
    print("\nExamples:")
    print('  python test_query.py "gym that opens 24 hours"')
    print('  python test_query.py "large fitness center"')
    print('  python test_query.py "cheap gym under 300 AED"')
    sys.exit(1)

query = " ".join(sys.argv[1:])

engine = DemoSearchEngine()
results = engine.search(
    query=query,
    location="Dubai, UAE",
    radius=5000,
    max_results=3,
    analyze_reviews=True
)

engine.display_results(results, detailed=True)
