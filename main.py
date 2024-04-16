from pytube import YouTube
from moviepy.editor import *
from dotenv import load_dotenv
from google.cloud import speech
import os
import io

# Carregar as variáveis de ambiente do arquivo .env
load_dotenv()

def download_video(url, language_code):
    try:
        video = YouTube(url)
        print("Video Title:", video.title)
        print("Video Description:", video.description)
        print("Video Duration:", video.length, "seconds")

        # Obter o título do vídeo e usá-lo como nome do arquivo
        video_title = video.title
        video_file = video_title + ".mp4"
        audio_file = video_title + ".mp3"
        transcript_file = video_title + ".txt"

        # Remover caracteres inválidos dos nomes dos arquivos
        video_file = "".join(c for c in video_file if c.isalnum() or c in [" ", "-", "_", "."]).rstrip()
        audio_file = "".join(c for c in audio_file if c.isalnum() or c in [" ", "-", "_", "."]).rstrip()
        transcript_file = "".join(c for c in transcript_file if c.isalnum() or c in [" ", "-", "_", "."]).rstrip()

        # Baixar o vídeo
        print("Downloading video...")
        stream = video.streams.get_highest_resolution()
        stream.download(filename=video_file)
        print("Video downloaded successfully.")

        # Extrair o áudio do vídeo
        print("Extracting audio...")
        video_clip = VideoFileClip(video_file)
        audio_clip = video_clip.audio
        audio_clip.write_audiofile(audio_file)
        video_clip.close()
        audio_clip.close()
        print("Audio extracted successfully:", audio_file)

        # Configurar as credenciais da API do Google Cloud
        google_credentials = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")
        if google_credentials is None or not os.path.exists(google_credentials):
            raise ValueError("As credenciais do Google Cloud não foram encontradas. Certifique-se de que a variável de ambiente GOOGLE_APPLICATION_CREDENTIALS esteja definida corretamente e aponte para um arquivo JSON válido.")

        os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = google_credentials

        # Criar o cliente da API do Google Cloud Speech-to-Text
        client = speech.SpeechClient()

        # Ler o conteúdo do arquivo de áudio
        with io.open(audio_file, "rb") as audio_file:
            content = audio_file.read()

        # Configurar a requisição de transcrição de áudio
        audio = speech.RecognitionAudio(uri="gs://your-bucket-name/GAME OVER - A.I. Designs New ELECTRIC Motor.mp3")
        config = speech.RecognitionConfig(
            encoding=speech.RecognitionConfig.AudioEncoding.MP3,
            sample_rate_hertz=44100,
            language_code=language_code,
            model="default"
        )

        # Transcrever o áudio usando a API do Google Cloud Speech-to-Text
        operation = client.long_running_recognize(config=config, audio=audio)
        response = operation.result(timeout=90)  # Adjust the timeout as needed

        # Salvar a transcrição em um arquivo de texto
        with open(transcript_file, "w") as file:
            for result in response.results:
                file.write(result.alternatives[0].transcript + "\n")
        print("Transcription saved to:", transcript_file)

    except Exception as e:
        print("An error occurred:", str(e))

# Obter a URL do vídeo do YouTube a partir da entrada do usuário
video_url = input("Enter the YouTube video URL: ")

# Obter o idioma desejado para a transcrição
print("Select the language for transcription:")
print("1. English (en-US)")
print("2. Portuguese (pt-BR)")
print("3. Spanish (es-ES)")
print("4. French (fr-FR)")
print("5. German (de-DE)")
print("6. Other")

language_choice = input("Enter the number corresponding to your language choice: ")

language_codes = {
    "1": "en-US",
    "2": "pt-BR",
    "3": "es-ES",
    "4": "fr-FR",
    "5": "de-DE"
}

if language_choice in language_codes:
    selected_language_code = language_codes[language_choice]
else:
    selected_language_code = input("Enter the language code for your desired language (e.g., ja-JP for Japanese): ")

# Baixar o vídeo e transcrever o áudio
download_video(video_url, selected_language_code)

