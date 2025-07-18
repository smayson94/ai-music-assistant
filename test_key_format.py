#!/usr/bin/env python3
"""
Test API key format and validity
"""

import os
from dotenv import load_dotenv

def test_api_key_format():
    """Test the API key format"""
    print("🔑 Testing API Key Format")
    print("=" * 40)
    
    # Load environment variables
    load_dotenv()
    
    # Get API key
    api_key = os.getenv("OPENAI_API_KEY", "")
    
    if not api_key:
        print("❌ No API key found in .env file")
        return False
    
    print(f"API key length: {len(api_key)} characters")
    print(f"API key starts with: {api_key[:10]}...")
    print(f"API key ends with: ...{api_key[-10:]}")
    
    # Check if it looks like a valid OpenAI API key
    if api_key.startswith("sk-") and len(api_key) > 50:
        print("✅ API key format looks correct")
        return True
    else:
        print("❌ API key format looks incorrect")
        print("OpenAI API keys should:")
        print("- Start with 'sk-'")
        print("- Be at least 50 characters long")
        return False

if __name__ == "__main__":
    success = test_api_key_format()
    if success:
        print("\n✅ API key format is correct")
        print("If you're still seeing 0 requests, the issue might be:")
        print("1. API key is invalid/expired")
        print("2. Network connectivity issues")
        print("3. OpenAI service issues")
    else:
        print("\n❌ API key format is incorrect")
        print("Please check your OpenAI API key in the .env file") 