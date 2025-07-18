#!/usr/bin/env python3
"""
Test API key status and quota
"""

import openai
from config import get_openai_key

def test_api_status():
    """Test the API key and check quota status"""
    print("🔑 Testing API Key Status")
    print("=" * 40)
    
    # Get API key
    api_key = get_openai_key()
    if not api_key:
        print("❌ No API key found!")
        return False
    
    print(f"✅ API key found: {api_key[:10]}...")
    
    # Initialize client
    try:
        client = openai.OpenAI(api_key=api_key)
        print("✅ OpenAI client initialized")
    except Exception as e:
        print(f"❌ Client initialization error: {e}")
        return False
    
    # Test with a simple request
    try:
        print("🧠 Testing API with simple request...")
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "user", "content": "Say hello"}
            ],
            max_tokens=10
        )
        
        result = response.choices[0].message.content
        print(f"✅ API working! Response: '{result}'")
        return True
        
    except openai.RateLimitError as e:
        print(f"⚠️ Rate limit error: {e}")
        print("This might be a temporary issue.")
        return False
        
    except openai.AuthenticationError as e:
        print(f"❌ Authentication error: {e}")
        print("Check if your API key is correct.")
        return False
        
    except openai.QuotaExceededError as e:
        print(f"❌ Quota exceeded: {e}")
        print("Check your OpenAI billing and usage limits.")
        return False
        
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return False

if __name__ == "__main__":
    success = test_api_status()
    if success:
        print("\n🎉 API is working correctly!")
    else:
        print("\n⚠️ API has issues. Check your OpenAI account.") 