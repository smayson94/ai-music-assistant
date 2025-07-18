#!/usr/bin/env python3
"""
Direct test of AI generation without voice transcription
"""

from gpt_parser import parse_prompt_to_structure
from midi_generator import make_music_midi

def test_direct_generation():
    """Test AI generation with direct text input"""
    print("🧠 Testing Direct AI Generation")
    print("=" * 40)
    
    # Test prompts
    test_prompts = [
        "Create jazz chords",
        "Make a trap beat",
        "Generate lo-fi music with chords",
        "Create a classical melody"
    ]
    
    for i, prompt in enumerate(test_prompts, 1):
        print(f"\n🎵 Test {i}: '{prompt}'")
        print("-" * 30)
        
        try:
            # Parse with GPT
            print("🔄 Parsing with AI...")
            parsed = parse_prompt_to_structure(prompt)
            
            if parsed:
                print(f"✅ Genre: {parsed.get('genre', 'unknown')}")
                print(f"✅ BPM: {parsed.get('bpm', 'unknown')}")
                print(f"✅ Music Type: {parsed.get('music_type', 'unknown')}")
                
                if 'chords' in parsed and parsed['chords']:
                    print(f"✅ Chords: {parsed['chords']}")
                
                if 'melody' in parsed and parsed['melody']:
                    print(f"✅ Melody: {parsed['melody']}")
                
                # Generate MIDI
                filename = f"midi_output/test_{i}_{parsed.get('genre', 'unknown')}.mid"
                print(f"🥁 Generating MIDI: {filename}")
                
                midi_file = make_music_midi(parsed, filename)
                print(f"✅ MIDI file created: {midi_file}")
                
            else:
                print("❌ Parsing failed")
                
        except Exception as e:
            print(f"❌ Error: {e}")
    
    print("\n🎉 Testing complete! Check the midi_output folder for results.")

if __name__ == "__main__":
    test_direct_generation() 