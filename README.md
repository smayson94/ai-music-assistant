# 🎵 AI Music Assistant

An AI-powered music assistant that converts voice commands into MIDI drum patterns. Built with Whisper for speech recognition, GPT for natural language processing, and PrettyMIDI for MIDI generation.

## 🚀 Features

- **Voice Commands**: Speak your music requests naturally
- **Text Input**: Type your requests for testing
- **AI Processing**: GPT converts natural language to structured music data
- **MIDI Generation**: Creates drum patterns ready for your DAW
- **Web Interface**: Streamlit app for easy interaction

## 📋 Requirements

- Python 3.8+
- OpenAI API key
- Microphone (for voice input)

## 🛠️ Installation

1. **Clone or download the project files**

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up your OpenAI API key**:
   - Get an API key from [OpenAI](https://platform.openai.com/api-keys)
   - Set it as an environment variable or in the web interface

## 🎯 Usage

### Option 1: Command Line Interface

Run the main application:
```bash
python app.py
```

Choose between:
- Voice input (requires microphone)
- Text input (for testing)

### Option 2: Web Interface (Recommended)

Launch the Streamlit app:
```bash
streamlit run streamlit_app.py
```

This provides:
- Voice recording button
- Text input area
- Real-time processing
- MIDI file download

## 🎵 Example Commands

Try these voice or text commands:

- "Make a lo-fi hip-hop beat at 85 BPM"
- "Create a trap beat at 140 BPM with heavy 808s"
- "Generate a house music pattern at 128 BPM"
- "Make a boom bap beat at 90 BPM"
- "Create a techno rhythm at 130 BPM"

## 📁 Project Structure

```
ai-music-assistant/
├── app.py                 # Main CLI application
├── streamlit_app.py       # Web interface
├── whisper_transcriber.py # Voice-to-text functionality
├── gpt_parser.py          # Natural language processing
├── midi_generator.py      # MIDI file generation
├── requirements.txt       # Python dependencies
├── README.md             # This file
└── midi_output/          # Generated MIDI files
```

## 🔧 How It Works

1. **Voice Input**: Record audio using your microphone
2. **Speech Recognition**: Whisper transcribes audio to text
3. **AI Processing**: GPT parses text into structured music data
4. **MIDI Generation**: Creates drum patterns with proper timing
5. **Output**: MIDI file ready for your DAW

## 🎛️ DAW Integration

The generated MIDI files can be imported into:
- Ableton Live
- FL Studio
- Logic Pro
- Pro Tools
- Any DAW that supports MIDI

## 🚀 Future Enhancements

- **Humming to Melody**: Convert vocal melodies to MIDI
- **Beatboxing to Drums**: Convert beatboxing to drum patterns
- **Real-time Processing**: Live MIDI generation during performance
- **Ableton Integration**: Direct plugin for Ableton Live
- **Multi-track Generation**: Bass, melody, and chord progressions

## 🐛 Troubleshooting

### Common Issues:

1. **"No speech detected"**
   - Check microphone permissions
   - Speak clearly and loudly
   - Try text input mode

2. **"OpenAI API error"**
   - Verify your API key is correct
   - Check your OpenAI account balance
   - Ensure internet connection

3. **"MIDI file not generated"**
   - Check the `midi_output/` directory exists
   - Verify write permissions

## 📝 License

This project is for educational and personal use. Please respect OpenAI's terms of service.

## 🤝 Contributing

Feel free to:
- Report bugs
- Suggest new features
- Submit improvements
- Share your creations!

---

**Happy music making! 🎵** 