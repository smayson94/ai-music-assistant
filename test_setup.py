#!/usr/bin/env python3
"""
Test script to verify the AI Music Assistant setup
"""

import sys
import os

def test_imports():
    """Test if all required modules can be imported"""
    print("🧪 Testing imports...")
    
    try:
        import numpy
        print("✅ numpy")
    except ImportError:
        print("❌ numpy - Install with: pip install numpy")
        return False
    
    try:
        import scipy
        print("✅ scipy")
    except ImportError:
        print("❌ scipy - Install with: pip install scipy")
        return False
    
    try:
        import sounddevice
        print("✅ sounddevice")
    except ImportError:
        print("❌ sounddevice - Install with: pip install sounddevice")
        return False
    
    try:
        import openai
        print("✅ openai")
    except ImportError:
        print("❌ openai - Install with: pip install openai")
        return False
    
    try:
        import pretty_midi
        print("✅ pretty_midi")
    except ImportError:
        print("❌ pretty_midi - Install with: pip install pretty_midi")
        return False
    
    try:
        import streamlit
        print("✅ streamlit")
    except ImportError:
        print("❌ streamlit - Install with: pip install streamlit")
        return False
    
    try:
        from faster_whisper import WhisperModel
        print("✅ faster_whisper")
    except ImportError:
        print("❌ faster_whisper - Install with: pip install faster-whisper")
        return False
    
    return True

def test_local_modules():
    """Test if our custom modules can be imported"""
    print("\n🧪 Testing local modules...")
    
    try:
        from whisper_transcriber import record_audio, transcribe
        print("✅ whisper_transcriber")
    except ImportError as e:
        print(f"❌ whisper_transcriber - {e}")
        return False
    
    try:
        from gpt_parser import parse_prompt_to_structure
        print("✅ gpt_parser")
    except ImportError as e:
        print(f"❌ gpt_parser - {e}")
        return False
    
    try:
        from midi_generator import make_drum_midi
        print("✅ midi_generator")
    except ImportError as e:
        print(f"❌ midi_generator - {e}")
        return False
    
    return True

def test_midi_output_dir():
    """Test if MIDI output directory exists and is writable"""
    print("\n🧪 Testing MIDI output directory...")
    
    midi_dir = "midi_output"
    if not os.path.exists(midi_dir):
        try:
            os.makedirs(midi_dir)
            print(f"✅ Created {midi_dir} directory")
        except Exception as e:
            print(f"❌ Could not create {midi_dir} directory - {e}")
            return False
    else:
        print(f"✅ {midi_dir} directory exists")
    
    # Test write permission
    test_file = os.path.join(midi_dir, "test.mid")
    try:
        import pretty_midi
        midi = pretty_midi.PrettyMIDI()
        midi.write(test_file)
        os.remove(test_file)
        print("✅ MIDI output directory is writable")
    except Exception as e:
        print(f"❌ MIDI output directory is not writable - {e}")
        return False
    
    return True

def main():
    """Run all tests"""
    print("🎵 AI Music Assistant - Setup Test")
    print("=" * 40)
    
    all_passed = True
    
    # Test imports
    if not test_imports():
        all_passed = False
    
    # Test local modules
    if not test_local_modules():
        all_passed = False
    
    # Test MIDI output
    if not test_midi_output_dir():
        all_passed = False
    
    print("\n" + "=" * 40)
    if all_passed:
        print("🎉 All tests passed! Your setup is ready.")
        print("\nNext steps:")
        print("1. Set your OpenAI API key")
        print("2. Run: python app.py (for CLI)")
        print("3. Run: streamlit run streamlit_app.py (for web interface)")
    else:
        print("❌ Some tests failed. Please fix the issues above.")
        print("\nTo install missing dependencies:")
        print("pip install -r requirements.txt")
    
    return all_passed

if __name__ == "__main__":
    main() 