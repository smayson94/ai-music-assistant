#!/usr/bin/env python3
"""
Simple voice recording and transcription test
"""

from whisper_transcriber import record_audio, transcribe

def test_voice():
    """Test voice recording and transcription"""
    print("🎤 Voice Recording Test")
    print("=" * 30)
    
    # Get recording duration from user
    print("⏱️  Choose recording duration:")
    print("1. Quick (5 seconds)")
    print("2. Standard (10 seconds)")
    print("3. Extended (15 seconds)")
    print("4. Custom duration")
    
    duration_choice = input("Enter choice (1-4): ").strip()
    
    if duration_choice == "1":
        duration = 5
    elif duration_choice == "2":
        duration = 10
    elif duration_choice == "3":
        duration = 15
    elif duration_choice == "4":
        try:
            custom_duration = input("Enter custom duration in seconds (5-60): ").strip()
            duration = int(custom_duration)
            if duration < 5 or duration > 60:
                print("⚠️  Duration must be between 5-60 seconds. Using 10 seconds.")
                duration = 10
        except ValueError:
            print("⚠️  Invalid input. Using 10 seconds.")
            duration = 10
    else:
        print("⚠️  Invalid choice. Using 10 seconds.")
        duration = 10
    
    print(f"🎤 Recording for {duration} seconds...")
    
    try:
        # Record audio
        print("Speak your music request now!")
        filename = record_audio(duration=duration)
        
        # Transcribe
        print("Transcribing...")
        text = transcribe(filename)
        
        print(f"✅ Transcribed text: '{text}'")
        
        if text.strip():
            print("🎉 Voice recording and transcription working!")
            return True
        else:
            print("❌ No speech detected. Please try again.")
            return False
            
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

if __name__ == "__main__":
    success = test_voice()
    if success:
        print("\n✅ Voice functionality is working!")
        print("You can now use voice input with: python app.py")
    else:
        print("\n⚠️ Voice functionality needs attention") 