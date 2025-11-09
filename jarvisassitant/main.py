#!/usr/bin/env python3
"""
J.A.R.V.I.S - Just A Rather Very Intelligent System
An Iron Man inspired AI Voice Assistant
"""

import threading
import time
from jarvis_core import JarvisCore
from jarvis_gui import JarvisGUI
from config import ASSISTANT_NAME

def main():
    """Main function to run JARVIS"""
    print("=" * 60)
    print("  J.A.R.V.I.S - Just A Rather Very Intelligent System")
    print("  Iron Man Inspired AI Voice Assistant")
    print("=" * 60)
    print()
    
    # Initialize components
    jarvis = JarvisCore()
    gui = JarvisGUI()
    
    # Welcome message
    welcome_msg = "Good day, sir. JARVIS is now online and ready to assist you."
    jarvis.speak(welcome_msg)
    
    running = True
    
    def voice_loop():
        """Voice processing loop running in separate thread"""
        nonlocal running
        
        while running:
            try:
                # Update GUI status
                gui.status = f"Waiting for wake word '{ASSISTANT_NAME}'..."
                
                # Wait for wake word
                print(f"\nSay '{ASSISTANT_NAME}' to activate...")
                if jarvis.wait_for_wake_word():
                    # Wake word detected
                    gui.status = "Wake word detected! Listening for command..."
                    jarvis.speak("Yes, sir?")

                    # Wait for speaking to finish
                    while jarvis.is_speaking:
                        time.sleep(0.1)
                    time.sleep(0.5)

                    # Listen for command
                    gui.status = "Listening for your command..."
                    command = jarvis.listen()

                    if command:
                        gui.command_text = command
                        gui.status = "Processing command..."

                        # Process command
                        result = jarvis.process_command(command)

                        # Wait for response to be spoken
                        while jarvis.is_speaking:
                            time.sleep(0.1)

                        if result == "EXIT":
                            running = False
                            break

                        gui.response_text = jarvis.last_response
                        gui.status = "Command processed. Ready for next command."
                    else:
                        gui.status = "No command detected."
                        jarvis.speak("I didn't catch that, sir.")
                        while jarvis.is_speaking:
                            time.sleep(0.1)
                
                time.sleep(0.1)
                
            except KeyboardInterrupt:
                running = False
                break
            except Exception as e:
                print(f"Error in voice loop: {e}")
                time.sleep(1)
    
    # Start voice processing in separate thread
    voice_thread = threading.Thread(target=voice_loop, daemon=True)
    voice_thread.start()
    
    # Main GUI loop
    try:
        while running:
            running = gui.update(
                is_listening=jarvis.is_listening,
                is_speaking=jarvis.is_speaking,
                status=gui.status,
                command=gui.command_text,
                response=gui.response_text
            )
            
            if not running:
                break
                
    except KeyboardInterrupt:
        print("\n\nShutting down JARVIS...")
    finally:
        # Cleanup
        running = False
        jarvis.speak("Shutting down. Goodbye, sir.")
        time.sleep(2)
        jarvis.cleanup()
        gui.cleanup()
        print("JARVIS has been shut down.")

if __name__ == "__main__":
    main()

