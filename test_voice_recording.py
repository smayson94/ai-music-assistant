#!/usr/bin/env python3
"""
Test voice recording and transcription functionality
"""

from whisper_transcriber import record_audio, transcribe

def test_voice_recording():
    """Test voice recording and transcription"""
    
    print("🎤 Testing Voice Recording")
    print("=" * 30)
    
    try:
        # Test recording
        print("🎙️ Recording 3 seconds of audio...")
        print("Please speak something when prompted!")
        
        filename = record_audio(duration=3)
        print(f"✅ Recording saved to: {filename}")
        
        # Test transcription
        print("\n📝 Transcribing audio...")
        text = transcribe(filename)
        
        if text.strip():
            print(f"✅ Transcribed text: '{text}'")
        else:
            print("⚠️  No speech detected (this is normal if you didn't speak)")
        
        print("\n🎉 Voice recording test complete!")
        
    except Exception as e:
        print(f"❌ Error during voice recording: {e}")
        print("This might be due to microphone permissions or hardware issues.")

if __name__ == "__main__":
    test_voice_recording() 