import os
from dotenv import load_dotenv

# Load environment variables from .env file if it exists
load_dotenv()

# OpenAI API Configuration
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")

# Audio Recording Configuration
DEFAULT_SAMPLE_RATE = 44100
DEFAULT_RECORDING_DURATION = 15  # seconds - customizable duration

# MIDI Configuration
DEFAULT_BPM = 90
DEFAULT_GENRE = "hip-hop"

# File Paths
MIDI_OUTPUT_DIR = "midi_output"
AUDIO_INPUT_FILE = "input.wav"

def validate_setup():
    """Validate that the setup is complete"""
    if not OPENAI_API_KEY:
        print("⚠️  Warning: OpenAI API key not found!")
        print("   Set it as an environment variable: OPENAI_API_KEY=your_key_here")
        print("   Or set it in the web interface")
        return False
    return True

def get_openai_key():
    """Get OpenAI API key with fallback"""
    return OPENAI_API_KEY or input("Enter your OpenAI API key: ").strip() 