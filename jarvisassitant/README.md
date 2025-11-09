# J.A.R.V.I.S - Just A Rather Very Intelligent System

An Iron Man inspired AI Voice Assistant with interactive GUI, powered by Google Gemini AI.

![JARVIS](https://img.shields.io/badge/AI-JARVIS-blue)
![Python](https://img.shields.io/badge/Python-3.8+-green)
![Status](https://img.shields.io/badge/Status-Active-success)

## Features

✨ **Voice Recognition** - Listen to your commands using advanced speech recognition
🤖 **AI-Powered Responses** - Intelligent answers using Google Gemini AI with real-time data
🗣️ **Text-to-Speech** - JARVIS-like voice responses
🎨 **Interactive GUI** - Beautiful animated interface inspired by Iron Man
🎯 **Wake Word Detection** - Activate with "Jarvis" or "Hey Jarvis"
⚡ **Real-time Processing** - Fast and responsive interactions
🌐 **Web Integration** - Search Google, open websites, play YouTube videos
📚 **Wikipedia Search** - Get instant information from Wikipedia
🌤️ **Weather Updates** - Real-time weather information
🧮 **Calculations** - Perform mathematical calculations
📰 **News Access** - Quick access to latest news
💬 **Natural Conversations** - Ask anything and get intelligent responses

## Demo

The assistant features:
- Animated circular visualization (like JARVIS in Iron Man)
- Real-time status updates
- Visual feedback for listening and speaking states
- Particle effects and smooth animations
- Clean, futuristic interface

## Installation

### Prerequisites

- Python 3.8 or higher
- Microphone for voice input
- Speakers for audio output
- Google Gemini API key (free at https://makersuite.google.com/app/apikey)

### Step 1: Clone or Download

```bash
cd jarvisassistant
```

### Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

**Note for Windows users:** If you encounter issues installing PyAudio, download the appropriate wheel file from [here](https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio) and install it:

```bash
pip install PyAudio-0.2.11-cp3xx-cp3xx-win_amd64.whl
```

### Step 3: Configure API Key

1. Copy `.env.example` to `.env`:
   ```bash
   cp .env.example .env
   ```

2. Edit `.env` and add your Gemini API key:
   ```
   GEMINI_API_KEY=your_actual_gemini_api_key_here
   ```

3. Get your free Gemini API key from: https://makersuite.google.com/app/apikey

## Usage

### Running JARVIS

```bash
python main.py
```

### How to Interact

1. **Activate JARVIS**: Say "Jarvis", "Hey Jarvis", or "OK Jarvis"
2. **Wait for Response**: JARVIS will say "Yes, sir?"
3. **Give Command**: Speak your question or command
4. **Get Response**: JARVIS will process and respond

### Example Commands

**Time & Date:**
- "What's the time?"
- "What's today's date?"

**Weather:**
- "What's the weather?"
- "Weather in New York"

**Search & Information:**
- "Search for best pizza recipes"
- "Wikipedia Albert Einstein"
- "Tell me about artificial intelligence"
- "Explain quantum computing"

**Web & Media:**
- "Open YouTube"
- "Play relaxing music"
- "Open Gmail"
- "Show me the news"

**Calculations:**
- "Calculate 25 times 4"
- "What is 100 divided by 5"

**General Questions:**
- "Who are you?"
- "How does photosynthesis work?"
- "Tell me a joke"

**Exit:**
- "Exit" or "Goodbye" (to quit)

📖 **See VOICE_COMMANDS.md for complete command reference**

## Features Breakdown

### Voice Commands
- **Time Query**: Ask for current time
- **Date Query**: Ask for today's date
- **General Questions**: Any question will be answered by Gemini AI
- **Exit Commands**: Say "exit", "quit", "goodbye", or "bye"

### GUI Features
- Animated pulsing core (JARVIS visualization)
- Color-coded states:
  - **Blue**: Idle/Ready
  - **Red**: Listening
  - **Green**: Speaking
- Real-time command and response display
- Particle effects for visual feedback

## Configuration

Edit `config.py` to customize:

```python
# Assistant Settings
ASSISTANT_NAME = "Jarvis"
WAKE_WORDS = ["jarvis", "hey jarvis", "ok jarvis"]

# Voice Settings
VOICE_RATE = 180  # Speech speed
VOICE_VOLUME = 0.9  # Volume (0.0 to 1.0)

# UI Settings
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
ACCENT_COLOR = (0, 150, 255)  # RGB color
```

## Troubleshooting

### Microphone Not Working
- Check microphone permissions in system settings
- Ensure microphone is set as default input device
- Run the calibration by restarting the application

### PyAudio Installation Issues
- **Windows**: Download wheel file from [here](https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio)
- **Linux**: `sudo apt-get install portaudio19-dev python3-pyaudio`
- **Mac**: `brew install portaudio`

### API Key Issues
- Verify your `.env` file exists and contains the correct key
- Check that your Gemini API key is valid
- Ensure you have internet connection
- **Fixed**: Now uses `gemini-1.5-flash` model (gemini-pro is deprecated)

### Speech Recognition Issues
- Speak clearly and at a moderate pace
- Reduce background noise
- Adjust `RECOGNITION_TIMEOUT` in `config.py`

## Project Structure

```
jarvisassistant/
├── main.py              # Main application entry point
├── jarvis_core.py       # Core AI and voice processing
├── jarvis_gui.py        # GUI and animations
├── config.py            # Configuration settings
├── requirements.txt     # Python dependencies
├── .env.example         # Environment variables template
├── .env                 # Your API keys (create this)
└── README.md           # This file
```

## Technologies Used

- **Speech Recognition**: Google Speech Recognition API
- **Text-to-Speech**: pyttsx3 (offline TTS)
- **AI Engine**: Google Gemini Pro
- **GUI**: Pygame
- **Audio**: PyAudio

## Future Enhancements

- [ ] Add more voice commands (open apps, search web, etc.)
- [ ] Implement conversation history
- [ ] Add voice customization options
- [ ] Integration with smart home devices
- [ ] Multi-language support
- [ ] Custom wake word training

## Credits

Inspired by JARVIS from Iron Man movies.
Built with ❤️ using Python and Google Gemini AI.

## License

This project is open source and available for educational purposes.

---

**"Sometimes you gotta run before you can walk."** - Tony Stark

