import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# API Configuration
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')
WOLFRAM_APP_ID = os.getenv('WOLFRAM_APP_ID', '')  # Optional for advanced calculations

# Voice Assistant Settings
ASSISTANT_NAME = "Jarvis"
WAKE_WORDS = ["jarvis", "hey jarvis", "ok jarvis"]

# Speech Recognition Settings
RECOGNITION_TIMEOUT = 5
RECOGNITION_PHRASE_LIMIT = 10

# Text-to-Speech Settings
VOICE_RATE = 180  # Speed of speech
VOICE_VOLUME = 0.9  # Volume level (0.0 to 1.0)

# UI Settings
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
BACKGROUND_COLOR = (10, 15, 30)
ACCENT_COLOR = (0, 150, 255)
TEXT_COLOR = (255, 255, 255)

# Feature Settings
ENABLE_WEB_SEARCH = True
ENABLE_WIKIPEDIA = True
ENABLE_CALCULATIONS = True
MAX_RESPONSE_LENGTH = 500  # Characters for spoken response

