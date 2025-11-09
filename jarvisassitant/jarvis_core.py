import speech_recognition as sr
import pyttsx3
import google.generativeai as genai
import threading
import time
import requests
import wikipedia
import webbrowser
from datetime import datetime
from config import *

class JarvisCore:
    def __init__(self):
        """Initialize JARVIS core components"""
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()
        
        # Initialize text-to-speech engine
        try:
            self.tts_engine = pyttsx3.init()
            self.tts_engine.setProperty('rate', VOICE_RATE)
            self.tts_engine.setProperty('volume', VOICE_VOLUME)

            # Set voice to male (JARVIS-like)
            voices = self.tts_engine.getProperty('voices')
            print(f"Available voices: {len(voices)}")

            # Try to find a good male voice
            voice_set = False
            for voice in voices:
                voice_name = voice.name.lower()
                if any(keyword in voice_name for keyword in ['david', 'mark', 'zira', 'male']):
                    self.tts_engine.setProperty('voice', voice.id)
                    print(f"✓ Using voice: {voice.name}")
                    voice_set = True
                    break

            if not voice_set and len(voices) > 0:
                # Use first available voice
                self.tts_engine.setProperty('voice', voices[0].id)
                print(f"✓ Using default voice: {voices[0].name}")

            # Test TTS
            print("Testing TTS engine...")

        except Exception as e:
            print(f"Warning: TTS initialization error: {e}")
            self.tts_engine = None
        
        # Initialize Gemini AI
        if GEMINI_API_KEY:
            try:
                genai.configure(api_key=GEMINI_API_KEY)
                # Use the latest available Gemini model (2025 update)
                # Try models in order of preference: fastest and most reliable
                model_names = [
                    'gemini-2.0-flash',           # Latest fast model
                    'gemini-flash-latest',        # Alias for latest flash
                    'gemini-2.5-flash',           # Alternative fast model
                    'gemini-pro-latest'           # Fallback to pro
                ]

                self.model = None
                for model_name in model_names:
                    try:
                        self.model = genai.GenerativeModel(model_name)
                        self.chat = self.model.start_chat(history=[])
                        print(f"✓ Gemini AI initialized with model: {model_name}")
                        break
                    except Exception as e:
                        continue

                if not self.model:
                    print("Warning: Could not initialize any Gemini model")
                    self.model = None
            except Exception as e:
                print(f"Error initializing Gemini: {e}")
                self.model = None
        else:
            self.model = None
            print("Warning: GEMINI_API_KEY not found. AI features will be limited.")
        
        self.is_listening = False
        self.is_speaking = False
        self.last_command = ""
        self.last_response = ""
        
        # Adjust for ambient noise
        print("Calibrating microphone for ambient noise...")
        with self.microphone as source:
            self.recognizer.adjust_for_ambient_noise(source, duration=2)
        print("Calibration complete!")
    
    def speak(self, text):
        """Convert text to speech"""
        self.is_speaking = True
        self.last_response = text
        print(f"JARVIS: {text}")

        if not self.tts_engine:
            print("ERROR: TTS engine not initialized!")
            self.is_speaking = False
            return

        try:
            # Speak synchronously to ensure it completes
            print("[Speaking...]")
            self.tts_engine.say(text)
            self.tts_engine.runAndWait()
            print("[Speech complete]")
        except Exception as e:
            print(f"TTS Error: {e}")
            # Try to reinitialize TTS
            try:
                self.tts_engine = pyttsx3.init()
                self.tts_engine.setProperty('rate', VOICE_RATE)
                self.tts_engine.setProperty('volume', VOICE_VOLUME)
                self.tts_engine.say(text)
                self.tts_engine.runAndWait()
            except:
                print("Failed to reinitialize TTS")
        finally:
            self.is_speaking = False
    
    def listen(self, timeout=None):
        """Listen for voice input"""
        try:
            self.is_listening = True
            with self.microphone as source:
                print("Listening...")
                audio = self.recognizer.listen(
                    source, 
                    timeout=timeout or RECOGNITION_TIMEOUT,
                    phrase_time_limit=RECOGNITION_PHRASE_LIMIT
                )
            
            self.is_listening = False
            print("Processing speech...")
            
            # Recognize speech using Google Speech Recognition
            text = self.recognizer.recognize_google(audio)
            self.last_command = text
            print(f"You said: {text}")
            return text.lower()
            
        except sr.WaitTimeoutError:
            self.is_listening = False
            return None
        except sr.UnknownValueError:
            self.is_listening = False
            print("Could not understand audio")
            return None
        except sr.RequestError as e:
            self.is_listening = False
            print(f"Could not request results; {e}")
            return None
        except Exception as e:
            self.is_listening = False
            print(f"Error: {e}")
            return None
    
    def search_web(self, query):
        """Search the web for real-time information"""
        try:
            # Use DuckDuckGo Instant Answer API (no key required)
            url = f"https://api.duckduckgo.com/?q={query}&format=json"
            response = requests.get(url, timeout=5)
            data = response.json()

            if data.get('AbstractText'):
                return data['AbstractText']
            elif data.get('RelatedTopics') and len(data['RelatedTopics']) > 0:
                first_topic = data['RelatedTopics'][0]
                if isinstance(first_topic, dict) and 'Text' in first_topic:
                    return first_topic['Text']

            return None
        except Exception as e:
            print(f"Web search error: {e}")
            return None

    def get_wikipedia_summary(self, query):
        """Get Wikipedia summary"""
        try:
            wikipedia.set_lang("en")
            result = wikipedia.summary(query, sentences=2)
            return result
        except wikipedia.exceptions.DisambiguationError as e:
            # If multiple results, pick the first one
            try:
                result = wikipedia.summary(e.options[0], sentences=2)
                return result
            except:
                return None
        except wikipedia.exceptions.PageError:
            return None
        except Exception as e:
            print(f"Wikipedia error: {e}")
            return None

    def get_weather(self, city=""):
        """Get weather information"""
        try:
            # Use wttr.in API (no key required)
            if not city:
                city = "auto"  # Auto-detect location
            url = f"https://wttr.in/{city}?format=%C+%t+%h+%w"
            response = requests.get(url, timeout=5)
            if response.status_code == 200:
                return f"The weather is {response.text.strip()}"
            return None
        except Exception as e:
            print(f"Weather error: {e}")
            return None

    def calculate(self, expression):
        """Perform calculations"""
        try:
            # Safe evaluation of mathematical expressions
            allowed_chars = set('0123456789+-*/()%. ')
            if all(c in allowed_chars for c in expression):
                result = eval(expression)
                return f"The answer is {result}"
            return None
        except Exception as e:
            print(f"Calculation error: {e}")
            return None

    def get_ai_response(self, query):
        """Get response from Gemini AI with real-time context"""
        if not self.model:
            return "I apologize, but my AI capabilities are currently offline. Please configure the Gemini API key."

        try:
            # Try to get real-time information first
            context = ""

            # Check if query needs real-time data
            if any(word in query.lower() for word in ['weather', 'temperature', 'forecast']):
                weather_info = self.get_weather()
                if weather_info:
                    context = f"Current weather information: {weather_info}\n\n"

            # Add context to make JARVIS more personality-driven
            jarvis_prompt = f"""You are JARVIS, an advanced AI assistant like in Iron Man.
You are sophisticated, helpful, and have a touch of wit.
Respond to the following query in a concise, intelligent manner suitable for voice output.
Keep your response to 2-3 sentences maximum so it can be spoken clearly.
Be informative but brief.

{context}User query: {query}"""

            response = self.chat.send_message(jarvis_prompt)

            # Get the text response
            response_text = response.text

            # Limit response length for voice output
            if len(response_text) > MAX_RESPONSE_LENGTH:
                # Truncate at sentence boundary
                sentences = response_text.split('. ')
                response_text = '. '.join(sentences[:2]) + '.'

            return response_text

        except Exception as e:
            error_msg = str(e)
            print(f"AI Error: {e}")

            # Handle specific errors
            if '429' in error_msg or 'quota' in error_msg.lower() or 'rate limit' in error_msg.lower():
                return "I apologize sir, but I've reached my API quota limit. Please wait a moment and try again, or check your API key settings."
            elif '401' in error_msg or 'unauthorized' in error_msg.lower():
                return "I'm having authentication issues, sir. Please verify your API key is correct."
            elif '404' in error_msg:
                return "The AI model is currently unavailable, sir. The system may need an update."
            else:
                return "I encountered an error processing your request, sir. Please try again."
    
    def process_command(self, command):
        """Process voice commands with enhanced capabilities"""
        if not command:
            return None

        command_lower = command.lower()

        # Exit commands
        if any(word in command_lower for word in ['exit', 'quit', 'goodbye', 'bye jarvis']):
            response = "Goodbye, sir. It has been a pleasure serving you."
            self.speak(response)
            return "EXIT"

        # Time query
        elif 'time' in command_lower and 'what' in command_lower:
            current_time = datetime.now().strftime("%I:%M %p")
            response = f"The current time is {current_time}, sir."
            self.speak(response)
            return response

        # Date query
        elif 'date' in command_lower and ('what' in command_lower or 'today' in command_lower):
            current_date = datetime.now().strftime("%B %d, %Y")
            day_name = datetime.now().strftime("%A")
            response = f"Today is {day_name}, {current_date}, sir."
            self.speak(response)
            return response

        # Weather query
        elif 'weather' in command_lower:
            response = self.get_weather()
            if response:
                self.speak(response)
                return response
            else:
                response = "I'm unable to fetch weather information at the moment, sir."
                self.speak(response)
                return response

        # Wikipedia search
        elif 'wikipedia' in command_lower or 'wiki' in command_lower:
            search_query = command_lower.replace('wikipedia', '').replace('wiki', '').replace('search', '').strip()
            if search_query:
                self.speak(f"Searching Wikipedia for {search_query}")
                wiki_result = self.get_wikipedia_summary(search_query)
                if wiki_result:
                    response = wiki_result
                    self.speak(response)
                    return response
                else:
                    response = f"I couldn't find information about {search_query} on Wikipedia, sir."
                    self.speak(response)
                    return response

        # Web search
        elif 'search' in command_lower or 'google' in command_lower:
            search_query = command_lower.replace('search', '').replace('google', '').replace('for', '').strip()
            if search_query:
                self.speak(f"Searching the web for {search_query}")
                webbrowser.open(f"https://www.google.com/search?q={search_query}")
                response = f"I've opened a web search for {search_query}, sir."
                self.speak(response)
                return response

        # Open website
        elif 'open' in command_lower and any(site in command_lower for site in ['youtube', 'google', 'gmail', 'facebook', 'twitter', 'instagram']):
            if 'youtube' in command_lower:
                webbrowser.open("https://www.youtube.com")
                response = "Opening YouTube, sir."
            elif 'google' in command_lower:
                webbrowser.open("https://www.google.com")
                response = "Opening Google, sir."
            elif 'gmail' in command_lower:
                webbrowser.open("https://mail.google.com")
                response = "Opening Gmail, sir."
            elif 'facebook' in command_lower:
                webbrowser.open("https://www.facebook.com")
                response = "Opening Facebook, sir."
            elif 'twitter' in command_lower:
                webbrowser.open("https://www.twitter.com")
                response = "Opening Twitter, sir."
            elif 'instagram' in command_lower:
                webbrowser.open("https://www.instagram.com")
                response = "Opening Instagram, sir."
            else:
                response = "Opening the website, sir."

            self.speak(response)
            return response

        # Play on YouTube
        elif 'play' in command_lower and ('youtube' in command_lower or 'video' in command_lower or 'song' in command_lower):
            search_query = command_lower.replace('play', '').replace('youtube', '').replace('video', '').replace('song', '').replace('on', '').strip()
            if search_query:
                webbrowser.open(f"https://www.youtube.com/results?search_query={search_query}")
                response = f"Playing {search_query} on YouTube, sir."
                self.speak(response)
                return response

        # Calculations
        elif any(word in command_lower for word in ['calculate', 'compute', 'plus', 'minus', 'multiply', 'divide', 'times']):
            # Extract mathematical expression
            expression = command_lower.replace('calculate', '').replace('compute', '').replace('what is', '').replace('equals', '').strip()
            expression = expression.replace('plus', '+').replace('minus', '-').replace('times', '*').replace('multiply', '*').replace('divided by', '/')

            result = self.calculate(expression)
            if result:
                self.speak(result)
                return result
            else:
                # Fall back to AI
                response = self.get_ai_response(command)
                self.speak(response)
                return response

        # Introduction
        elif 'who are you' in command_lower or 'what are you' in command_lower:
            response = "I am JARVIS, your personal AI assistant. Just A Rather Very Intelligent System, at your service, sir."
            self.speak(response)
            return response

        # News
        elif 'news' in command_lower:
            webbrowser.open("https://news.google.com")
            response = "Opening the latest news for you, sir."
            self.speak(response)
            return response

        # Default: Use Gemini AI for intelligent responses
        else:
            response = self.get_ai_response(command)
            self.speak(response)
            return response
    
    def wait_for_wake_word(self):
        """Listen for wake word"""
        command = self.listen(timeout=None)
        if command:
            for wake_word in WAKE_WORDS:
                if wake_word in command:
                    return True
        return False
    
    def cleanup(self):
        """Cleanup resources"""
        try:
            self.tts_engine.stop()
        except:
            pass

