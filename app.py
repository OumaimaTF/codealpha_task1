import streamlit as st
from googletrans import Translator, LANGUAGES
from gtts import gTTS
import os

# Initialisation du traducteur
translator = Translator()

# Dictionnaire des langues disponibles
language_dict = {name.capitalize(): code for code, name in LANGUAGES.items()}

# Interface Streamlit
st.title("🌍 Language Translation & Text-to-Speech")

# Entrée utilisateur
text = st.text_area("Enter text to translate:", "Hello, how are you?")
target_language = st.selectbox("Select target language:", list(language_dict.keys()), index=20)



# Traduction et lecture du texte traduit
if st.button("Translate & Read"):
    if text.strip():
        try:
            translated_text = translator.translate(text, dest=language_dict[target_language]).text
            st.success(f"Translated Text ({target_language}):")
            st.write(translated_text)

            # Convertir en audio avec la langue cible
            tts_translated = gTTS(translated_text, lang=language_dict[target_language])
            tts_translated.save("translated.mp3")
            st.audio("translated.mp3", format="audio/mp3")

        except Exception as e:
            st.error(f"Translation failed: {str(e)}")
    else:
        st.warning("Please enter text before translating.")
