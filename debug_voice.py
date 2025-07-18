#!/usr/bin/env python3
"""
Debug script to test voice processing step by step
"""

import os
import json
from whisper_transcriber import record_audio, transcribe
from gpt_parser import parse_prompt_to_structure

def debug_voice_process():
    """Debug the voice processing pipeline step by step"""
    print("🔍 Debug Voice Processing")
    print("=" * 40)
    
    # Step 1: Record audio
    print("🎤 Step 1: Recording audio...")
    try:
        filename = record_audio(duration=10)
        print(f"✅ Audio recorded: {filename}")
        
        # Check if file exists
        if os.path.exists(filename):
            file_size = os.path.getsize(filename)
            print(f"✅ File size: {file_size} bytes")
        else:
            print("❌ Audio file not found!")
            return
    except Exception as e:
        print(f"❌ Recording error: {e}")
        return
    
    # Step 2: Transcribe
    print("\n📝 Step 2: Transcribing...")
    try:
        text = transcribe(filename)
        print(f"✅ Transcribed text: '{text}'")
        
        if not text.strip():
            print("❌ No speech detected!")
            return
    except Exception as e:
        print(f"❌ Transcription error: {e}")
        return
    
    # Step 3: Parse with GPT
    print("\n🧠 Step 3: Parsing with GPT...")
    try:
        parsed = parse_prompt_to_structure(text)
        if parsed is None:
            print("❌ GPT parsing returned None!")
            return
            
        print(f"✅ Parsed structure: {json.dumps(parsed, indent=2)}")
        
        # Check if genre is present
        if "genre" in parsed:
            print(f"✅ Genre: {parsed['genre']}")
        else:
            print("❌ No genre found in parsed structure!")
            return
            
    except Exception as e:
        print(f"❌ GPT parsing error: {e}")
        return
    
    # Step 4: Show what filename would be generated
    print("\n📁 Step 4: MIDI filename that would be generated:")
    genre = parsed.get("genre", "unknown")
    filename = f"midi_output/{genre}_beat.mid"
    print(f"✅ Would create: {filename}")
    
    print("\n🎉 All steps completed successfully!")
    print("The issue might be in the MIDI generation step.")

if __name__ == "__main__":
    debug_voice_process() 