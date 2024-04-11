from pytube import YouTube
from moviepy.editor import *
from dotenv import load_dotenv
from google.cloud import speech
import os
import io

# Carregar as variáveis de ambiente do arquivo .env
load_dotenv()

def download_video(url):
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
        os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")

        # Criar o cliente da API do Google Cloud Speech-to-Text
        client = speech.SpeechClient()

        # Ler o conteúdo do arquivo de áudio
        with io.open(audio_file, "rb") as audio_file:
            content = audio_file.read()

        # Configurar a requisição de transcrição de áudio
        audio = speech.RecognitionAudio(content=content)
        config = speech.RecognitionConfig(
            encoding=speech.RecognitionConfig.AudioEncoding.MP3,
            sample_rate_hertz=44100,
            language_code="pt-BR",
            model="default"
        )

        # Transcrever o áudio usando a API do Google Cloud Speech-to-Text
        response = client.recognize(config=config, audio=audio)

        # Salvar a transcrição em um arquivo de texto
        with open(transcript_file, "w") as file:
            for result in response.results:
                file.write(result.alternatives[0].transcript + "\n")
        print("Transcription saved to:", transcript_file)

    except Exception as e:
        print("An error occurred:", str(e))

# Obter a URL do vídeo do YouTube a partir da entrada do usuário
video_url = input("Enter the YouTube video URL: ")

# Baixar o vídeo, extrair o áudio e transcrever
download_video(video_url)
