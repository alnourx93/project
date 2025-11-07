# 🎮 Test Agentic Google Maps NOW!

No API keys needed - try the demo versions immediately!

## 🚀 Quick Test Options

### Option 1: Watch the Demo (Automated)
See a full example query in action:

```bash
python demo.py
```

This will automatically run the query:
*"I want a gym that is 300 AED a month and is large and opens 24 hours"*

You'll see:
- ✅ AI parsing the query
- ✅ Extracting criteria (price, hours, size)
- ✅ Searching places (mock data)
- ✅ Analyzing reviews
- ✅ Ranking results by match score
- ✅ Detailed place information

---

### Option 2: Try Your Own Queries (Interactive)
Test with your own search queries:

```bash
python demo_interactive.py
```

Then try queries like:
- `I want a gym that opens 24 hours`
- `Find me a large fitness center`
- `Show me gyms under 300 AED`
- `I need a gym that is cheap and large`

The AI will parse your query and show you how it understands it!

---

## 📊 What You'll See

### 1. Query Parsing
```
🤖 AI Agent: Parsing your query...

📋 Extracted criteria:
   • Place type: gym
   • Search query: gym
   • Price: 300 AED per month
   • Hours: 24 hours
   • Size: large
```

### 2. Search & Analysis
```
🗺️  Searching Google Maps (Demo Mode)...
✅ Found 3 potential matches

🔬 Analyzing places...
   [1/3] Analyzing: FitZone 24/7 Gym
   [2/3] Analyzing: PowerLift Fitness Center
   [3/3] Analyzing: Mega Fitness Arena
```

### 3. Ranked Results
```
🎯 SEARCH RESULTS

1. FitZone 24/7 Gym
   --------------------------------------------------------
   🟢 Match Score: 100/100
   💭 Based on review analysis: price matches criteria,
      hours match criteria, size matches criteria

   📍 Sheikh Zayed Road, Dubai, UAE
   ⭐⭐⭐⭐ 4.5/5 (342 reviews)
   🟢 Open now

   📝 AI Summary:
      FitZone 24/7 Gym (Rating: 4.5/5) is an excellent match
      with a score of 100/100. Around 300 AED per month
      mentioned in reviews. Open 24 hours according to reviews.

   💰 Price Info: Around 300 AED per month mentioned in reviews
   🕐 Hours Info: Open 24 hours according to reviews
   📏 Size Info: Described as large/spacious in reviews

   📞 +971 4 123 4567
   🌐 https://fitzone24.ae
```

---

## 🎯 Key Features Demonstrated

### Natural Language Understanding
The AI understands queries like:
- "300 AED a month" → Extracts price criteria
- "24 hours" → Extracts hours criteria
- "large" → Extracts size criteria

### Intelligent Review Analysis
Analyzes reviews to find:
- 💰 Price mentions ("299 AED", "300 dirhams")
- 🕐 Hours mentions ("open 24/7", "always open")
- 📏 Size mentions ("huge", "massive", "spacious")

### Smart Ranking
- 🟢 100/100 = Perfect match (all criteria met)
- 🟡 50-69/100 = Partial match (some criteria met)
- 🔴 0-49/100 = Poor match (few criteria met)

---

## 🔄 Demo vs Real Version

### Demo Version (Current)
- ✅ No API keys needed
- ✅ Test immediately
- ✅ See AI parsing in action
- ✅ Understand the workflow
- ⚠️ Uses mock gym data (3 gyms in Dubai)
- ⚠️ Limited to demo scenarios

### Real Version (With API Keys)
- ✅ Real Google Maps data
- ✅ Millions of actual places worldwide
- ✅ Real user reviews
- ✅ Any type of place (gyms, restaurants, hotels, etc.)
- ✅ Any location globally
- 🔑 Requires Google Maps + Anthropic API keys

---

## 💡 Tips for Testing

1. **Be specific** - Add details like price, hours, size
2. **Try variations** - Different combinations of criteria
3. **Check reasoning** - See why each place got its score
4. **Review analysis** - Notice what AI extracts from reviews

---

## 🚀 Next Steps

### Ready for the Real Thing?

1. **Get API Keys**:
   - Google Maps API: https://console.cloud.google.com/
   - Anthropic API: https://console.anthropic.com/

2. **Set up .env**:
   ```bash
   cp .env.example .env
   # Edit .env with your API keys
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the real version**:
   ```bash
   python main.py
   ```

5. **Search ANYTHING, ANYWHERE**!
   - "Sushi restaurant in Tokyo with private rooms"
   - "Coffee shop in London with good wifi"
   - "Hotel in Paris under 150 euros with pool"
   - "Barbershop in New York open on Sundays"

---

## ❓ Questions?

Check out:
- **QUICKSTART.md** - 5-minute setup guide
- **README.md** - Full documentation
- **example_usage.py** - Code examples

---

**Have fun testing! 🎉**
