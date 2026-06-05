import streamlit as st
from deep_translator import GoogleTranslator
from gtts import gTTS
import pyperclip
import os

st.set_page_config(page_title="Language Translation Tool")

st.title("🌍 AI Language Translation Tool")

text = st.text_area("Enter Text")

languages = {
    "English": "en",
    "Telugu": "te",
    "Hindi": "hi",
    "Tamil": "ta",
    "Kannada": "kn",
    "French": "fr",
    "German": "de",
    "Spanish": "es"
}

source = st.selectbox(
    "Source Language",
    list(languages.keys())
)

target = st.selectbox(
    "Target Language",
    list(languages.keys())
)

if st.button("Translate"):
    if text:

        translated_text = GoogleTranslator(
            source=languages[source],
            target=languages[target]
        ).translate(text)

        st.success("Translation Successful")

        st.subheader("Translated Text")
        st.write(translated_text)

        # Copy Button
        if st.button("📋 Copy Translation"):
            pyperclip.copy(translated_text)
            st.success("Copied to clipboard!")

        # Text To Speech
        tts = gTTS(
            text=translated_text,
            lang=languages[target],
            slow=False
        )

        audio_file = "translated_audio.mp3"
        tts.save(audio_file)

        st.audio(audio_file)

        with open(audio_file, "rb") as file:
            st.download_button(
                label="⬇ Download Audio",
                data=file,
                file_name="translation.mp3",
                mime="audio/mp3"
            )

    else:
        st.warning("Please enter some text.")