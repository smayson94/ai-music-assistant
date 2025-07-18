import os
import json
from whisper_transcriber import record_audio, transcribe
from gpt_parser import parse_prompt_to_structure
from midi_generator import make_music_midi

def get_recording_duration():
    """Get recording duration from user"""
    print("⏱️  Choose recording duration:")
    print("1. Quick (5 seconds)")
    print("2. Standard (10 seconds)")
    print("3. Extended (15 seconds)")
    print("4. Custom duration")
    
    duration_choice = input("Enter choice (1-4): ").strip()
    
    if duration_choice == "1":
        return 5
    elif duration_choice == "2":
        return 10
    elif duration_choice == "3":
        return 15
    elif duration_choice == "4":
        try:
            custom_duration = input("Enter custom duration in seconds (5-60): ").strip()
            duration = int(custom_duration)
            if duration < 5 or duration > 60:
                print("⚠️  Duration must be between 5-60 seconds. Using 10 seconds.")
                return 10
            return duration
        except ValueError:
            print("⚠️  Invalid input. Using 10 seconds.")
            return 10
    else:
        print("⚠️  Invalid choice. Using 10 seconds.")
        return 10

def get_filename(genre):
    """Get filename from user"""
    print("📁 Choose filename:")
    print("1. Auto-generated (genre_beat.mid)")
    print("2. Custom filename")
    
    filename_choice = input("Enter choice (1 or 2): ").strip()
    
    if filename_choice == "2":
        custom_name = input("Enter custom filename (without .mid): ").strip()
        if not custom_name:
            custom_name = f"{genre}_beat"
        return f"midi_output/{custom_name}.mid"
    else:
        return f"midi_output/{genre}_beat.mid"

def run_assistant():
    """Main function to run the AI music assistant"""
    print("🎵 AI Music Assistant")
    print("=" * 30)
    
    # Get recording duration from user
    duration = get_recording_duration()
    print(f"🎤 Recording for {duration} seconds...")
    
    try:
        # Step 1: Record audio
        print("🎤 Recording your voice command...")
        filename = record_audio(duration=duration)
        
        # Step 2: Transcribe audio
        print("📝 Transcribing...")
        text = transcribe(filename)
        print(f"Transcribed: '{text}'")
        
        if not text.strip():
            print("❌ No speech detected. Please try again.")
            return
        
        # Step 3: Parse with GPT
        print("🧠 Processing with AI...")
        parsed = parse_prompt_to_structure(text)
        print(f"Parsed structure: {json.dumps(parsed, indent=2)}")
        
        # Step 4: Generate MIDI
        print("🥁 Generating MIDI...")
        
        filename = get_filename(parsed['genre'])
        
        midi_file = make_music_midi(
            parsed, 
            filename=filename
        )
        
        print("✅ Success! MIDI file created.")
        print(f"📁 File: {midi_file}")
        print(f"🎵 Genre: {parsed['genre']}")
        print(f"⚡ BPM: {parsed.get('bpm', 90)}")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        print("Please check your OpenAI API key and try again.")

def run_with_text_input():
    """Alternative function to test with text input instead of voice"""
    print("🎵 AI Music Assistant (Text Mode)")
    print("=" * 40)
    
    text = input("Enter your music request: ")
    if not text.strip():
        print("❌ No input provided.")
        return
    
    try:
        # Parse with GPT
        print("🧠 Processing with AI...")
        parsed = parse_prompt_to_structure(text)
        print(f"Parsed structure: {json.dumps(parsed, indent=2)}")
        
        # Generate MIDI
        print("🥁 Generating MIDI...")
        
        filename = get_filename(parsed['genre'])
        
        midi_file = make_music_midi(
            parsed, 
            filename=filename
        )
        
        print("✅ Success! MIDI file created.")
        print(f"📁 File: {midi_file}")
        
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    print("Choose mode:")
    print("1. Voice input (requires microphone)")
    print("2. Text input")
    
    choice = input("Enter choice (1 or 2): ").strip()
    
    if choice == "1":
        run_assistant()
    elif choice == "2":
        run_with_text_input()
    else:
        print("Invalid choice. Running voice mode...")
        run_assistant() 