import streamlit as st
import whisper
import os
os.environ["PATH"] += os.pathsep + f'/usr/local/bin/'
os.environ["PATH"] += os.pathsep + f'/usr/local/bin/'

st.title("Whisper App")

#audio_file=st.file_uploader("Upload Audio" , type=["wav","mp3","m4a"])
file="/Users/hemantkumar/Downloads/ttsmaker-file-2024-7-31-9-15-29.mp3"

model=whisper.load_model("base")
st.text("Whisper model loaded")





if st.sidebar.button("Transcribe Audio"):
    if file is not None:
        st.sidebar.success("Transcribing Audio")
        transcription=model.transcribe(file)
        st.sidebar.success("Transcribing Audio")
        st.text(transcription["text"])
    else:
        st.sidebar.error("Please upload an audio file")
st.sidebar.header("Play Original audio file")
st.sidebar.audio(file)