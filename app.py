import streamlit as st
from deep_translator import GoogleTranslator
from gtts import gTTS
import streamlit.components.v1 as components

# ---------------- UI ----------------
st.set_page_config(page_title="Language Translation Tool", page_icon="🌍", layout="centered")

st.title("🌍 AI Language Translation Tool")
st.markdown("Translate text instantly using AI-powered translation")

text = st.text_area("✍️ Enter Text", height=150)

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

col1, col2 = st.columns(2)

with col1:
    source = st.selectbox("📥 Source Language", list(languages.keys()))

with col2:
    target = st.selectbox("📤 Target Language", list(languages.keys()))

# ---------------- TRANSLATE ----------------
if st.button("🚀 Translate"):

    if text.strip() == "":
        st.warning("Please enter text")

    else:
        translated_text = GoogleTranslator(
            source=languages[source],
            target=languages[target]
        ).translate(text)

        st.success("Translation Completed 🎉")

        # OUTPUT BOX
        st.subheader("📌 Translated Text")
        st.text_area("Result", translated_text, height=150)

        # ---------------- COPY BUTTON (REAL FIX) ----------------
        copy_html = f"""
        <textarea id="textBox" style="width:100%;height:100px;">{translated_text}</textarea>
        <br>
        <button onclick="copyText()">📋 Copy Text</button>

        <script>
        function copyText() {{
            var copyText = document.getElementById("textBox");
            copyText.select();
            document.execCommand("copy");
            alert("Copied to clipboard!");
        }}
        </script>
        """

        components.html(copy_html, height=200)

        # ---------------- TEXT TO SPEECH ----------------
        tts = gTTS(text=translated_text, lang=languages[target], slow=False)
        audio_file = "translation.mp3"
        tts.save(audio_file)

        st.audio(audio_file)

        with open(audio_file, "rb") as file:
            st.download_button(
                "⬇ Download Audio",
                file,
                file_name="translation.mp3",
                mime="audio/mp3"
            )

