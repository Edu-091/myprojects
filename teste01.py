pip install git+https://github.com/openai/whisper.git
pip install ffmpeg

import whisper
import textwrap  # Necessário para formatar o texto

# Carregar o modelo Whisper
# Escolha entre "tiny", "base", "small", "medium", "large"
model = whisper.load_model("large")

# Nome do arquivo de áudio (substitua pelo caminho correto)
audio_file = r".\HeberJr02v01_11_2025.mp3"  # Certifique-se de que o arquivo existe

try:
    # Verifique se o arquivo realmente existe antes de continuar
    import os
    if not os.path.exists(audio_file):
        raise FileNotFoundError(f"Arquivo não encontrado: {audio_file}")

    # Transcrever o áudio
    print("Transcrevendo o áudio...")
    result = model.transcribe(audio_file, language="pt")

    # Obter o texto transcrito
    transcricao = result['text']

    # Formatar o texto com quebras de linha (80 caracteres por linha)
    transcricao_formatada = textwrap.fill(transcricao, width=80)

    # Mostrar a transcrição formatada
    print("Transcrição formatada:")
    print(transcricao_formatada)
except Exception as e:
    print(f"Ocorreu um erro durante a transcrição: {e}")
