import openai
import json
import os
from config import get_openai_key

def parse_prompt_to_structure(prompt):
    """Convert natural language prompt to structured music instructions"""
    
    # Set up OpenAI API key
    api_key = get_openai_key()
    if not api_key:
        print("❌ No OpenAI API key provided!")
        return None
    
    # Initialize OpenAI client with new API
    client = openai.OpenAI(api_key=api_key)
    
    system_msg = """You are a music assistant that converts natural language requests into structured music instructions. 
    Return ONLY valid JSON with the following structure:
    {
        "genre": "string (e.g., trap, lo-fi, house, hip-hop, dubstep, techno, jazz, funk, classical, ambient)",
        "bpm": number,
        "music_type": "drums, chords, melody, or mixed",
        "pattern": {
            "kick": "comma-separated beat positions (e.g., 1,1.3,2,2.3)",
            "snare": "comma-separated beat positions (e.g., 2,4)",
            "hats": "comma-separated beat positions (e.g., 1.2,1.4,2.2,2.4,3.2,3.4,4.2,4.4)"
        },
        "chords": ["C", "Am", "F", "G"] or null,
        "melody": ["C4", "E4", "G4", "A4"] or null
    }
    
    Beat positions: 1=beat 1, 1.2=beat 1.2, 1.3=beat 1.5, 1.4=beat 1.75, etc.
    
    Create varied patterns based on the request:
    - For "chords" or "jazz": Use music_type="chords", include chord progression
    - For "melody" or "piano": Use music_type="melody", include melody notes
    - For "drums" or "beat": Use music_type="drums", include drum pattern
    - For "mixed": Include both drums and chords/melody
    
    Genre-specific patterns:
    - Jazz: Complex chord progressions (ii-V-I, etc.), 120-140 BPM
    - Lo-fi: Simple chords, relaxed tempo, 80-90 BPM
    - Trap: Heavy drums, sparse patterns, 140-150 BPM
    - House: Four-on-floor, groovy, 125-130 BPM
    - Hip-hop: Boom-bap drums, 85-95 BPM
    - Classical: Melodic lines, 60-120 BPM
    - Ambient: Sparse, atmospheric, 60-80 BPM"""
    
    try:
        print("🔄 Attempting OpenAI API call...")
        response = client.chat.completions.create(
            model="gpt-4o-mini",  # Using mini for cost efficiency
            messages=[
                {"role": "system", "content": system_msg},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7
        )
        
        print("✅ OpenAI API call successful!")
        result = response.choices[0].message.content.strip()
        
        # Try to parse as JSON
        try:
            parsed = json.loads(result)
            return parsed
        except json.JSONDecodeError:
            # If JSON parsing fails, return a varied default structure
            print(f"Failed to parse GPT response as JSON: {result}")
            import random
            
            # Create varied fallback patterns
            fallback_patterns = [
                {
                    "genre": "jazz",
                    "bpm": 120,
                    "music_type": "chords",
                    "pattern": {
                        "kick": "1,3",
                        "snare": "2,4",
                        "hats": "1.2,1.4,2.2,2.4,3.2,3.4,4.2,4.4"
                    },
                    "chords": ["Cmaj7", "Dm7", "G7", "Cmaj7"],
                    "melody": null
                },
                {
                    "genre": "trap",
                    "bpm": 140,
                    "music_type": "drums",
                    "pattern": {
                        "kick": "1,1.5,2,2.5,3,3.5,4,4.5",
                        "snare": "2,4",
                        "hats": "1.2,1.4,2.2,2.4,3.2,3.4,4.2,4.4"
                    },
                    "chords": null,
                    "melody": null
                },
                {
                    "genre": "lo-fi",
                    "bpm": 85,
                    "music_type": "mixed",
                    "pattern": {
                        "kick": "1,3",
                        "snare": "2,4",
                        "hats": "1.2,1.4,2.2,2.4,3.2,3.4,4.2,4.4"
                    },
                    "chords": ["Am", "F", "C", "G"],
                    "melody": ["A4", "C5", "E5", "F5"]
                },
                {
                    "genre": "classical",
                    "bpm": 90,
                    "music_type": "melody",
                    "pattern": {
                        "kick": "1,3",
                        "snare": "2,4",
                        "hats": "1.2,1.4,2.2,2.4,3.2,3.4,4.2,4.4"
                    },
                    "chords": null,
                    "melody": ["C4", "E4", "G4", "A4", "C5"]
                }
            ]
            
            return random.choice(fallback_patterns)
            
    except Exception as e:
        print(f"❌ Error calling OpenAI API: {e}")
        print("🔄 Falling back to varied patterns...")
        # Return varied default structure on error
        import random
        
        fallback_patterns = [
            {
                "genre": "trap",
                "bpm": 140,
                "pattern": {
                    "kick": "1,1.5,2,2.5,3,3.5,4,4.5",
                    "snare": "2,4",
                    "hats": "1.2,1.4,2.2,2.4,3.2,3.4,4.2,4.4"
                }
            },
            {
                "genre": "lo-fi",
                "bpm": 85,
                "pattern": {
                    "kick": "1,3",
                    "snare": "2,4",
                    "hats": "1.2,1.4,2.2,2.4,3.2,3.4,4.2,4.4"
                }
            },
            {
                "genre": "house",
                "bpm": 128,
                "pattern": {
                    "kick": "1,2,3,4",
                    "snare": "2,4",
                    "hats": "1.2,1.4,2.2,2.4,3.2,3.4,4.2,4.4"
                }
            },
            {
                "genre": "hip-hop",
                "bpm": 90,
                "pattern": {
                    "kick": "1,1.3,2,2.3",
                    "snare": "2,4",
                    "hats": "1.2,1.4,2.2,2.4,3.2,3.4,4.2,4.4"
                }
            }
        ]
        
        return random.choice(fallback_patterns) 