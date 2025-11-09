# 🎤 JARVIS Voice Commands Reference

## 🔹 Wake Word
Say **"Jarvis"**, **"Hey Jarvis"**, or **"OK Jarvis"** to activate

---

## ⏰ Time & Date Commands

| Command | Example | Response |
|---------|---------|----------|
| What's the time? | "What time is it?" | Current time |
| What's the date? | "What's today's date?" | Current date and day |

---

## 🌤️ Weather Commands

| Command | Example | Response |
|---------|---------|----------|
| Weather | "What's the weather?" | Current weather conditions |
| Weather in [city] | "Weather in London" | Weather for specific city |

---

## 🔍 Search Commands

| Command | Example | Response |
|---------|---------|----------|
| Search [query] | "Search artificial intelligence" | Opens Google search |
| Google [query] | "Google Python tutorials" | Opens Google search |
| Wikipedia [topic] | "Wikipedia Albert Einstein" | Reads Wikipedia summary |
| Wiki [topic] | "Wiki quantum physics" | Reads Wikipedia summary |

---

## 🌐 Website Commands

| Command | Example | Response |
|---------|---------|----------|
| Open YouTube | "Open YouTube" | Opens YouTube |
| Open Google | "Open Google" | Opens Google |
| Open Gmail | "Open Gmail" | Opens Gmail |
| Open Facebook | "Open Facebook" | Opens Facebook |
| Open Twitter | "Open Twitter" | Opens Twitter |
| Open Instagram | "Open Instagram" | Opens Instagram |
| News | "Show me the news" | Opens Google News |

---

## 🎵 Media Commands

| Command | Example | Response |
|---------|---------|----------|
| Play [song/video] | "Play Bohemian Rhapsody" | Searches YouTube |
| Play [song] on YouTube | "Play jazz music on YouTube" | Opens YouTube search |

---

## 🧮 Calculation Commands

| Command | Example | Response |
|---------|---------|----------|
| Calculate [expression] | "Calculate 25 times 4" | Performs calculation |
| What is [math] | "What is 100 divided by 5" | Performs calculation |
| [number] plus [number] | "50 plus 30" | Performs calculation |

**Supported operations:** plus (+), minus (-), times (×), multiply (*), divided by (/)

---

## 🤖 General AI Questions

JARVIS can answer ANY question using Google Gemini AI:

| Category | Example Questions |
|----------|------------------|
| **Science** | "Explain quantum computing" |
| | "What is photosynthesis?" |
| | "How does gravity work?" |
| **History** | "Who was Napoleon?" |
| | "Tell me about World War 2" |
| | "When was the internet invented?" |
| **Technology** | "What is artificial intelligence?" |
| | "Explain blockchain technology" |
| | "How do computers work?" |
| **General Knowledge** | "What is the capital of France?" |
| | "How many planets are there?" |
| | "Who wrote Romeo and Juliet?" |
| **Advice** | "How can I learn programming?" |
| | "Tips for better sleep" |
| | "How to stay productive?" |
| **Conversational** | "Tell me a joke" |
| | "What do you think about AI?" |
| | "How are you today?" |

---

## ℹ️ System Commands

| Command | Example | Response |
|---------|---------|----------|
| Who are you? | "Who are you?" | JARVIS introduction |
| What are you? | "What are you?" | JARVIS introduction |
| Exit | "Exit" / "Goodbye" / "Quit" | Shuts down JARVIS |

---

## 💡 Tips for Best Results

1. **Speak Clearly** - Enunciate your words
2. **Moderate Pace** - Not too fast, not too slow
3. **Reduce Background Noise** - For better recognition
4. **Wait for "Yes, sir?"** - Before giving your command
5. **Be Specific** - More specific questions get better answers
6. **Natural Language** - Speak naturally, like talking to a person

---

## 🎯 Example Conversation

```
You: "Jarvis"
JARVIS: "Yes, sir?"

You: "What's the weather?"
JARVIS: "The weather is Clear 72°F 45% Wind 5mph"

You: "Search for best restaurants nearby"
JARVIS: "Searching the web for best restaurants nearby" [Opens browser]

You: "Tell me about black holes"
JARVIS: "Black holes are regions of spacetime where gravity is so strong that nothing, not even light, can escape..."

You: "Calculate 156 times 23"
JARVIS: "The answer is 3588"

You: "Play relaxing music on YouTube"
JARVIS: "Playing relaxing music on YouTube, sir" [Opens YouTube]

You: "Exit"
JARVIS: "Goodbye, sir. It has been a pleasure serving you."
```

---

## 🚀 Advanced Features

### Real-Time Information
- JARVIS uses live APIs for weather, search, and Wikipedia
- Responses are always current and up-to-date

### Intelligent Context
- Gemini AI understands context and nuance
- Can handle follow-up questions
- Provides detailed, accurate answers

### Multi-Modal Responses
- Voice responses for all queries
- Opens web browser when needed
- Visual feedback in GUI

---

## 🔧 Customization

Edit `config.py` to customize:
- Voice speed (`VOICE_RATE`)
- Voice volume (`VOICE_VOLUME`)
- Wake words (`WAKE_WORDS`)
- UI colors and appearance

---

**"Sometimes you gotta run before you can walk."** - Tony Stark

