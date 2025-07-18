#!/usr/bin/env python3
"""
Test the GPT API fix
"""

from gpt_parser import parse_prompt_to_structure

def test_gpt_api():
    """Test the GPT API with a simple text prompt"""
    print("🧠 Testing GPT API Fix")
    print("=" * 30)
    
    # Test with a simple prompt
    test_prompt = "Create a trap beat at 140 BPM"
    
    try:
        print(f"Testing with prompt: '{test_prompt}'")
        result = parse_prompt_to_structure(test_prompt)
        
        if result:
            print("✅ GPT API working!")
            print(f"Genre: {result.get('genre', 'unknown')}")
            print(f"BPM: {result.get('bpm', 'unknown')}")
            print(f"Pattern: {result.get('pattern', {})}")
            return True
        else:
            print("❌ GPT API returned None")
            return False
            
    except Exception as e:
        print(f"❌ GPT API error: {e}")
        return False

if __name__ == "__main__":
    success = test_gpt_api()
    if success:
        print("\n🎉 GPT API is working! You should now get varied patterns.")
    else:
        print("\n⚠️ GPT API still has issues.") 