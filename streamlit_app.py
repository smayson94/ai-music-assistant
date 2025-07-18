import streamlit as st
import os
import json
from whisper_transcriber import record_audio, transcribe
from gpt_parser import parse_prompt_to_structure
from midi_generator import make_drum_midi

st.set_page_config(
    page_title="AI Music Assistant",
    page_icon="🎵",
    layout="wide"
)

def main():
    st.title("🎵 AI Music Assistant")
    st.markdown("---")
    
    # Sidebar for API key
    with st.sidebar:
        st.header("🔑 Setup")
        api_key = st.text_input("OpenAI API Key", type="password", help="Enter your OpenAI API key")
        if api_key:
            os.environ["OPENAI_API_KEY"] = api_key
            st.success("✅ API key set")
        else:
            st.warning("⚠️ Please enter your OpenAI API key")
            return
    
    # Main content
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.header("🎤 Voice Input")
        if st.button("🎙️ Record Voice Command", type="primary"):
            if not api_key:
                st.error("Please set your OpenAI API key first")
                return
            
            with st.spinner("Recording... Speak your music request!"):
                try:
                    filename = record_audio(duration=5)
                    text = transcribe(filename)
                    st.success(f"Transcribed: '{text}'")
                    
                    # Process with AI
                    with st.spinner("Processing with AI..."):
                        parsed = parse_prompt_to_structure(text)
                        st.json(parsed)
                    
                    # Generate MIDI
                    with st.spinner("Generating MIDI..."):
                        midi_file = make_drum_midi(
                            parsed["pattern"], 
                            bpm=parsed.get("bpm", 90),
                            filename=f"midi_output/{parsed['genre']}_beat.mid"
                        )
                        st.success(f"✅ MIDI generated: {midi_file}")
                        
                        # Provide download link
                        with open(midi_file, "rb") as f:
                            st.download_button(
                                label="📥 Download MIDI",
                                data=f.read(),
                                file_name=os.path.basename(midi_file),
                                mime="audio/midi"
                            )
                            
                except Exception as e:
                    st.error(f"Error: {e}")
    
    with col2:
        st.header("📝 Text Input")
        text_input = st.text_area(
            "Enter your music request:",
            placeholder="e.g., 'Make a trap beat at 140 BPM with heavy 808s'",
            height=100
        )
        
        if st.button("🎵 Generate from Text", type="secondary"):
            if not api_key:
                st.error("Please set your OpenAI API key first")
                return
            
            if not text_input.strip():
                st.error("Please enter a music request")
                return
            
            try:
                with st.spinner("Processing with AI..."):
                    parsed = parse_prompt_to_structure(text_input)
                    st.json(parsed)
                
                with st.spinner("Generating MIDI..."):
                    midi_file = make_drum_midi(
                        parsed["pattern"], 
                        bpm=parsed.get("bpm", 90),
                        filename=f"midi_output/{parsed['genre']}_beat.mid"
                    )
                    st.success(f"✅ MIDI generated: {midi_file}")
                    
                    # Provide download link
                    with open(midi_file, "rb") as f:
                        st.download_button(
                            label="📥 Download MIDI",
                            data=f.read(),
                            file_name=os.path.basename(midi_file),
                            mime="audio/midi"
                        )
                        
            except Exception as e:
                st.error(f"Error: {e}")
    
    # Examples section
    st.markdown("---")
    st.header("💡 Example Commands")
    examples = [
        "Make a lo-fi hip-hop beat at 85 BPM",
        "Create a trap beat at 140 BPM with heavy 808s",
        "Generate a house music pattern at 128 BPM",
        "Make a boom bap beat at 90 BPM",
        "Create a techno rhythm at 130 BPM"
    ]
    
    for example in examples:
        st.code(example)
    
    st.markdown("---")
    st.markdown("""
    ### 🎯 How it works:
    1. **Voice/Text Input**: Describe the music you want
    2. **AI Processing**: GPT converts your request to structured music data
    3. **MIDI Generation**: Creates a drum pattern based on your request
    4. **Download**: Get the MIDI file to use in your DAW
    
    ### 🎛️ Next Steps:
    - Import the MIDI file into Ableton Live, FL Studio, or any DAW
    - Add your own sounds and instruments
    - Build upon the generated pattern
    """)

if __name__ == "__main__":
    main() 