#!/usr/bin/env python3
"""
Test MIDI generation functionality without requiring API key
"""

import json
from midi_generator import make_drum_midi

def test_midi_generation():
    """Test MIDI generation with sample patterns"""
    
    print("🎵 Testing MIDI Generation")
    print("=" * 30)
    
    # Test patterns
    test_patterns = [
        {
            "name": "Basic Hip-Hop",
            "pattern": {
                "kick": "1,1.3,2,2.3",
                "snare": "2,4",
                "hats": "1.2,1.4,2.2,2.4,3.2,3.4,4.2,4.4"
            },
            "bpm": 90
        },
        {
            "name": "Trap Beat",
            "pattern": {
                "kick": "1,1.5,2,2.5,3,3.5,4,4.5",
                "snare": "2,4",
                "hats": "1.2,1.4,1.6,1.8,2.2,2.4,2.6,2.8,3.2,3.4,3.6,3.8,4.2,4.4,4.6,4.8"
            },
            "bpm": 140
        },
        {
            "name": "Lo-Fi",
            "pattern": {
                "kick": "1,3",
                "snare": "2,4",
                "hats": "1.2,1.4,2.2,2.4,3.2,3.4,4.2,4.4"
            },
            "bpm": 85
        }
    ]
    
    for test in test_patterns:
        print(f"\n🎵 Generating: {test['name']}")
        print(f"BPM: {test['bpm']}")
        print(f"Pattern: {json.dumps(test['pattern'], indent=2)}")
        
        try:
            filename = make_drum_midi(
                test['pattern'],
                bpm=test['bpm'],
                filename=f"midi_output/test_{test['name'].lower().replace(' ', '_')}.mid"
            )
            print(f"✅ Generated: {filename}")
        except Exception as e:
            print(f"❌ Error: {e}")
    
    print("\n🎉 MIDI generation test complete!")
    print("Check the midi_output/ directory for generated files.")

if __name__ == "__main__":
    test_midi_generation() 