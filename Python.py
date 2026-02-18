import streamlit as st
from gtts import gTTS
import base64
import os

# Título do App no Navegador
st.set_page_config(page_title="Kids English App", page_icon="🎤")

st.title("🎤 English for Kids")
st.write("Pratica a tua pronúncia e vê a frase ficar verde!")

# Lista de frases
frases = ["hello how are you", "i like apples", "the sky is blue", "see you later"]

def play_audio(text):
    tts = gTTS(text=text, lang='en')
    tts.save("speech.mp3")
    with open("speech.mp3", "rb") as f:
        data = f.read()
        b64 = base64.b64encode(data).decode()
        md = f'<audio autoplay="true" src="data:audio/mp3;base64,{b64}">'
        st.markdown(md, unsafe_allow_html=True)

# Interface do App
for i, frase_alvo in enumerate(frases):
    st.subheader(f"Frase {i+1}")
    st.info(frase_alvo.upper())
    
    if st.button(f"Ouvir Pronúncia {i+1}"):
        play_audio(frase_alvo)
    
    # Na Web, o input de texto é o mais seguro para crianças
    # Se quiseres microfone real na web, usamos um plugin chamado 'streamlit-webrtc'
    resposta = st.text_input(f"Escreve ou dita a frase {i+1}:", key=f"input_{i}").lower().strip()
    
    if resposta == frase_alvo:
        st.success("EXCELENTE! Ficou Verde! ✅")
        st.balloons()
    elif resposta != "":
        st.error("Tenta outra vez! 💪")