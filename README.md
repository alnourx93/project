# 🤖 Agentic Google Maps 🗺️

An AI-powered intelligent place search system that understands natural language queries and finds places based on complex criteria like price, hours, size, and reviews.

## ✨ Features

- **Natural Language Queries**: Ask in plain English like "I want a gym that is 300 AED a month and is large and opens 24 hours"
- **AI-Powered Analysis**: Uses Claude AI to parse queries and analyze reviews
- **Review Intelligence**: Automatically analyzes Google reviews to extract price, hours, size, and other information
- **Smart Ranking**: Ranks places based on how well they match your criteria
- **Detailed Information**: Access to names, addresses, ratings, reviews, hours, and contact info
- **Interactive CLI**: Easy-to-use command-line interface

## 🎯 How It Works

1. **Query Parsing**: AI agent parses your natural language query into structured criteria
2. **Place Search**: Searches Google Maps for relevant places
3. **Review Analysis**: Analyzes reviews to find specific information (price, hours, amenities)
4. **Smart Ranking**: Ranks results based on match score
5. **Results Display**: Shows you the best matches with detailed information

## 🚀 Setup

### Prerequisites

- Python 3.8 or higher
- Google Maps API key
- Anthropic API key (for Claude AI)

### Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd project
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up API keys**:

   Create a `.env` file in the project root:
   ```bash
   cp .env.example .env
   ```

   Edit `.env` and add your API keys:
   ```env
   GOOGLE_MAPS_API_KEY=your_google_maps_api_key_here
   ANTHROPIC_API_KEY=your_anthropic_api_key_here
   DEFAULT_LOCATION=Dubai, UAE
   DEFAULT_RADIUS=5000
   ```

### Getting API Keys

#### Google Maps API Key

1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project or select existing one
3. Enable the following APIs:
   - Places API
   - Geocoding API
4. Go to "Credentials" and create an API key
5. Copy the API key to your `.env` file

**Important**: Google Maps API has usage limits. Check [pricing](https://mapsplatform.google.com/pricing/) for details.

#### Anthropic API Key

1. Go to [Anthropic Console](https://console.anthropic.com/)
2. Sign up or log in
3. Go to "API Keys" section
4. Create a new API key
5. Copy the API key to your `.env` file

## 🎮 Usage

### Running the Application

```bash
python main.py
```

### Example Queries

1. **Gym with specific criteria**:
   ```
   I want a gym that is 300 AED a month and is large and opens 24 hours
   ```

2. **Restaurant search**:
   ```
   Find me a cheap Italian restaurant that's open late and has outdoor seating
   ```

3. **Coffee shop**:
   ```
   I need a coffee shop with good wifi and quiet atmosphere for working
   ```

4. **Hotel search**:
   ```
   Show me a family-friendly hotel with pool and spa under 500 AED per night
   ```

5. **Service search**:
   ```
   Find a barbershop that's open on Sundays and has good reviews
   ```

6. **Specific amenities**:
   ```
   I want a restaurant with valet parking and live music
   ```

### Interactive Options

When you run the application, you'll be prompted for:

- **Query**: Your natural language search query
- **Location**: Where to search (default: Dubai, UAE)
- **Radius**: Search radius in kilometers (default: 5km)
- **Max Results**: Number of results to show (default: 5)

### Understanding Results

Each result shows:

- **Match Score** (0-100): How well the place matches your criteria
  - 🟢 70-100: Great match
  - 🟡 40-69: Moderate match
  - 🔴 0-39: Poor match

- **AI Reasoning**: Why the place got this score

- **Extracted Information**:
  - Price info found in reviews
  - Hours info found in reviews
  - Size/space info found in reviews
  - Other relevant details

- **Place Details**:
  - Name and address
  - Rating and number of reviews
  - Current open/closed status
  - Contact information
  - Opening hours

## 📁 Project Structure

```
.
├── main.py              # Main CLI application
├── search_engine.py     # Agentic search engine
├── agent.py             # AI agent for query parsing and analysis
├── maps_client.py       # Google Maps API client
├── requirements.txt     # Python dependencies
├── .env.example         # Example environment variables
├── .env                 # Your environment variables (not in git)
└── README.md           # This file
```

## 🔧 Components

### MapsClient (`maps_client.py`)

Handles all interactions with Google Maps Places API:
- Place search
- Place details retrieval
- Review fetching
- Nearby search with filters

### MapsAgent (`agent.py`)

AI agent powered by Claude:
- Parses natural language queries into structured criteria
- Analyzes reviews to extract specific information
- Generates human-friendly summaries

### AgenticSearchEngine (`search_engine.py`)

Orchestrates the search process:
- Combines Maps API and AI Agent
- Ranks results by relevance
- Formats and displays results

### Main Application (`main.py`)

Interactive CLI interface:
- User input handling
- Result display
- Detailed view for individual places

## 💡 Tips

1. **Be specific**: The more details you provide, the better the results
2. **Use natural language**: Write queries as you would ask a friend
3. **Check match scores**: Higher scores mean better matches
4. **Read AI reasoning**: Understand why a place was recommended
5. **Review extracted info**: See what the AI found in reviews

## ⚠️ Limitations

- **API Costs**: Both Google Maps and Anthropic APIs have usage costs
- **Rate Limits**: APIs have rate limits; don't make too many requests quickly
- **Review Quality**: Results depend on the quality and quantity of reviews
- **Information Accuracy**: Extracted info from reviews may not always be current
- **Language**: Works best with English queries and reviews

## 🔒 Privacy & Security

- API keys are stored in `.env` file (not committed to git)
- No user data is stored or transmitted except to APIs
- Review data is only used for analysis, not stored

## 🐛 Troubleshooting

### "API keys not found"
- Make sure `.env` file exists
- Check that API keys are correctly set in `.env`
- Verify no extra spaces or quotes around keys

### "No places found"
- Try a more general query
- Increase search radius
- Check if location is correct
- Try a different location

### "Error during search"
- Check your internet connection
- Verify API keys are valid
- Check API quotas and limits
- Review error message for details

### "Could not geocode location"
- Make sure location is specific enough
- Try adding country or city
- Use format: "Area, City, Country"

## 🤝 Contributing

Feel free to:
- Report bugs
- Suggest features
- Submit pull requests
- Improve documentation

## 📄 License

This project is open source and available under the MIT License.

## 🙏 Acknowledgments

- Google Maps Platform for place data
- Anthropic Claude for AI capabilities
- Python community for excellent libraries

## 📞 Support

For issues or questions:
1. Check this README
2. Review error messages
3. Check API documentation
4. Open an issue on GitHub

---

**Happy searching! 🎉**
