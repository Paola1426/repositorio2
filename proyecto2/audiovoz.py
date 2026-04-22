"""_summary_
"""
from gtts import gTTS

texto = "Hola, esto es una prueba de audio en Python"
tts = gTTS(text=texto, lang='es')
tts.save("audio.mp3")

texto = "Hola, esto es una prueba de audio en Python 3"
tts = gTTS(text=texto, lang='es')
tts.save("audio2.mp3")
