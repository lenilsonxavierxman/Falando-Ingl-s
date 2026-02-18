import streamlit as st
from gtts import gTTS
import base64

# Configuração da Página
st.set_page_config(page_title="Kids English Talk", page_icon="🌟")

st.title("🌟 English for Kids: Talk Time!")
st.write("Ouve a frase e pratica a tua pronúncia!")

# --- Escopo das 4 Frases ---
frases = ["hello how are you", "i like apples", "the sky is blue", "see you later"]

def gerar_audio(texto):
    """Gera áudio que o navegador consegue reproduzir."""
    tts = gTTS(text=texto, lang='en')
    tts.save("audio.mp3")
    with open("audio.mp3", "rb") as f:
        data = f.read()
    b64 = base64.b64encode(data).decode()
    md = f'<audio controls><source src="data:audio/mp3;base64,{b64}" type="audio/mp3"></audio>'
    st.markdown(md, unsafe_allow_html=True)

# Interface de Utilizador
for i, frase in enumerate(frases, 1):
    with st.expander(f"Lição {i}: {frase.upper()}", expanded=(i==1)):
        st.write("1. Ouve a pronúncia correta:")
        if st.button(f"Ouvir Frase {i}", key=f"btn_{i}"):
            gerar_audio(frase)
        
        st.write("2. Escreve o que ouviste para treinar a escrita (ou usa o microfone do teclado):")
        entrada = st.text_input("Escreve aqui:", key=f"input_{i}").lower().strip()
        
        if entrada == frase:
            st.success("CORRECT! Ficou Verde! ✅")
            st.balloons() # Efeito visual de festa!
        elif entrada != "":
            st.error("Tenta outra vez! 💪")