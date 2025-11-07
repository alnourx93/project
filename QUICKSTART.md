# 🚀 Quick Start Guide

Get started with Agentic Google Maps in 5 minutes!

## Step 1: Install Dependencies

```bash
pip install -r requirements.txt
```

## Step 2: Set Up API Keys

1. Copy the example environment file:
   ```bash
   cp .env.example .env
   ```

2. Edit `.env` and add your API keys:
   ```
   GOOGLE_MAPS_API_KEY=your_key_here
   ANTHROPIC_API_KEY=your_key_here
   ```

### Where to Get API Keys?

**Google Maps API**:
- Visit: https://console.cloud.google.com/
- Enable "Places API" and "Geocoding API"
- Create credentials → API Key

**Anthropic API**:
- Visit: https://console.anthropic.com/
- Create an API key

## Step 3: Run the Application

```bash
python main.py
```

## Step 4: Try a Query

When prompted, enter:
```
I want a gym that is 300 AED a month and is large and opens 24 hours
```

Location: `Dubai, UAE` (or press Enter for default)

Radius: `5` (or press Enter for default)

Max results: `5` (or press Enter for default)

## Example Queries

Try these:

1. `Find me a cheap Italian restaurant that's open late`
2. `Coffee shop with good wifi and quiet atmosphere`
3. `Family-friendly hotel with pool under 500 AED`
4. `Barbershop open on Sundays with good reviews`

## Run Examples

```bash
python example_usage.py
```

## Tips

- Be specific in your queries
- Higher match scores (70+) are better
- Read the AI reasoning to understand results
- Check extracted info from reviews

## Troubleshooting

**No results found?**
- Try a more general query
- Increase search radius
- Check location spelling

**API errors?**
- Verify API keys in .env
- Check internet connection
- Ensure APIs are enabled

## Need Help?

Check the full [README.md](README.md) for detailed documentation.

---

Happy searching! 🎉
