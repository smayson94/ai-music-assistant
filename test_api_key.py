#!/usr/bin/env python3
"""
Test script to verify OpenAI API key setup
"""

import os
from dotenv import load_dotenv
from config import validate_setup, get_openai_key

def test_api_key():
    """Test the API key configuration"""
    print("🔑 Testing OpenAI API Key Setup")
    print("=" * 40)
    
    # Load environment variables
    load_dotenv()
    
    # Check if .env file exists
    if os.path.exists('.env'):
        print("✅ .env file found")
    else:
        print("❌ .env file not found")
        return False
    
    # Validate setup
    if validate_setup():
        print("✅ API key configuration is valid")
        
        # Test getting the key
        api_key = get_openai_key()
        if api_key and api_key != "your_openai_api_key_here":
            print("✅ API key is set and ready to use")
            print(f"   Key starts with: {api_key[:10]}...")
            return True
        else:
            print("❌ API key not properly configured")
            print("   Please edit the .env file and replace 'your_openai_api_key_here' with your actual API key")
            return False
    else:
        print("❌ API key configuration is invalid")
        return False

if __name__ == "__main__":
    success = test_api_key()
    if success:
        print("\n🎉 Ready for testing!")
        print("You can now run: python app.py")
    else:
        print("\n⚠️  Please configure your API key before testing")
        print("1. Get an API key from: https://platform.openai.com/api-keys")
        print("2. Edit the .env file and replace 'your_openai_api_key_here' with your actual key") 