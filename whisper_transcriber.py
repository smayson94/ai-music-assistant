import sounddevice as sd
import numpy as np
import scipy.io.wavfile
from faster_whisper import WhisperModel

def record_audio(filename="input.wav", duration=5, samplerate=44100):
    """Record audio from microphone and save to file"""
    print("Recording... Speak now!")
    audio = sd.rec(int(duration * samplerate), samplerate=samplerate, channels=1)
    sd.wait()
    scipy.io.wavfile.write(filename, samplerate, audio)
    print(f"Recording saved to {filename}")
    return filename

def transcribe(filename="input.wav"):
    """Transcribe audio file to text using Whisper"""
    print("Transcribing audio...")
    model = WhisperModel("base")
    segments, _ = model.transcribe(filename)
    text = "".join([seg.text for seg in segments])
    return text.strip()

def record_and_transcribe(duration=5):
    """Record audio and immediately transcribe it"""
    filename = record_audio(duration=duration)
    return transcribe(filename) 