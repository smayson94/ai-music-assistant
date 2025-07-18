#!/usr/bin/env python3
"""
Test GPT parser functionality
"""

import os
import json
from gpt_parser import parse_prompt_to_structure

def test_gpt_parser():
    """Test GPT parser with sample prompts"""
    
    print("🧠 Testing GPT Parser")
    print("=" * 30)
    
    # Check if API key is available
    api_key = os.getenv("OPENAI_API_KEY", "")
    if not api_key:
        print("⚠️  No OpenAI API key found!")
        print("To test with API key:")
        print("1. Set environment variable: set OPENAI_API_KEY=your_key")
        print("2. Or run the web interface and enter key there")
        print("\nTesting with mock data instead...")
        
        # Test with mock data
        mock_prompts = [
            "Make a lo-fi beat at 85 BPM",
            "Create a trap beat at 140 BPM",
            "Generate a house pattern at 128 BPM"
        ]
        
        for prompt in mock_prompts:
            print(f"\n🎵 Testing prompt: '{prompt}'")
            print("(Mock response - no API key)")
            mock_response = {
                "genre": "hip-hop",
                "bpm": 90,
                "pattern": {
                    "kick": "1,1.3,2,2.3",
                    "snare": "2,4",
                    "hats": "1.2,1.4,2.2,2.4,3.2,3.4,4.2,4.4"
                }
            }
            print(f"Mock structure: {json.dumps(mock_response, indent=2)}")
        
        return
    
    # Test with real API
    test_prompts = [
        "Make a lo-fi beat at 85 BPM",
        "Create a trap beat at 140 BPM",
        "Generate a house pattern at 128 BPM"
    ]
    
    for prompt in test_prompts:
        print(f"\n🎵 Testing prompt: '{prompt}'")
        try:
            result = parse_prompt_to_structure(prompt)
            print(f"✅ Parsed structure: {json.dumps(result, indent=2)}")
        except Exception as e:
            print(f"❌ Error: {e}")
    
    print("\n🎉 GPT parser test complete!")

if __name__ == "__main__":
    test_gpt_parser() 