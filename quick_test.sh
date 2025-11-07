#!/bin/bash

echo "╔═══════════════════════════════════════════════════════════╗"
echo "║                                                           ║"
echo "║        🎮 QUICK TEST - Agentic Google Maps 🗺️            ║"
echo "║                                                           ║"
echo "╚═══════════════════════════════════════════════════════════╝"
echo ""
echo "Choose a test option:"
echo ""
echo "1. 🎬 Watch Full Demo (automated)"
echo "   Shows complete search with your example query"
echo ""
echo "2. 🎮 Interactive Demo (try your own queries)"
echo "   Type your own searches and see how AI parses them"
echo ""
echo "3. 💻 See Code Examples"
echo "   View programmatic usage examples"
echo ""
read -p "Enter choice (1, 2, or 3): " choice

case $choice in
    1)
        echo ""
        echo "🎬 Running automated demo..."
        echo ""
        python demo.py
        ;;
    2)
        echo ""
        echo "🎮 Starting interactive demo..."
        echo ""
        python demo_interactive.py
        ;;
    3)
        echo ""
        echo "💻 Running code examples..."
        echo ""
        python example_usage.py
        ;;
    *)
        echo "Invalid choice!"
        exit 1
        ;;
esac

echo ""
echo "✅ Test complete!"
echo ""
echo "Ready to use the real version with actual Google Maps data?"
echo "See TEST_NOW.md for setup instructions!"
