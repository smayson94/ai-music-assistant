# 🚀 Quick Start Guide

Get your AI Music Assistant running in 5 minutes!

## 1. Install Dependencies

```bash
pip install -r requirements.txt
```

## 2. Test Your Setup

```bash
python test_setup.py
```

This will verify all dependencies are installed correctly.

## 3. Set Up OpenAI API Key

**Option A: Environment Variable**
```bash
# Windows
set OPENAI_API_KEY=your_api_key_here

# Or create a .env file with:
OPENAI_API_KEY=your_api_key_here
```

**Option B: Web Interface**
- Run the web app and enter your key there

## 4. Run the Assistant

**Web Interface (Recommended):**
```bash
streamlit run streamlit_app.py
```

**Command Line:**
```bash
python app.py
```

## 5. Try It Out!

**Voice Commands to Test:**
- "Make a lo-fi beat at 85 BPM"
- "Create a trap beat at 140 BPM"
- "Generate a house pattern at 128 BPM"

## 🎯 What You'll Get

1. **Voice Input**: Speak your music request
2. **AI Processing**: GPT converts it to structured data
3. **MIDI Output**: Downloadable MIDI file
4. **DAW Ready**: Import into Ableton, FL Studio, etc.

## 🐛 Common Issues

**"No speech detected"**
- Check microphone permissions
- Speak clearly and loudly
- Try text input mode

**"OpenAI API error"**
- Verify your API key
- Check account balance
- Ensure internet connection

## 📁 Generated Files

MIDI files will be saved in `midi_output/` directory.

---

**Ready to make music! 🎵** 