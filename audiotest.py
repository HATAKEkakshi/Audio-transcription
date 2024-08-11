import streamlit as st
import whisper

audio="/Users/hemantkumar/Developer/hackathon/platform/videotranscribe/audio/videotest/test.mp3"
model=whisper.load_model("base")
transcription=model.transcribe(audio)
print(transcription)