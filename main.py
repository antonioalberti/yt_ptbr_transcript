from pytube import YouTube
from moviepy.editor import *
import os
import whisper
import re

def download_video(url):
    try:
        video = YouTube(url)
        print("Video Title:", video.title)
        print("Video Description:", video.description)
        print("Video Duration:", video.length, "seconds")

        print("Downloading video...")
        stream = video.streams.get_highest_resolution()
        video_file = re.sub(r'[\\/*?:"<>|]', "_", video.title) + ".mp4"  # Save video with .mp4 extension
        stream.download(filename=video_file)
        print("Video downloaded successfully.")

        print("Extracting audio...")
        video_clip = VideoFileClip(video_file)
        audio_clip = video_clip.audio
        audio_file = re.sub(r'[\\/*?:"<>|]', "_", video.title) + ".mp3"  # Save audio with .mp3 extension
        audio_clip.write_audiofile(audio_file)
        video_clip.close()
        audio_clip.close()
        print("Audio extracted successfully:", audio_file)

        return audio_file, re.sub(r'[\\/*?:"<>|]', "_", video.title)
    except Exception as e:
        print("An error occurred during video download or audio extraction:", str(e))
        return None, None


def transcribe_audio(audio_file, video_title):
    try:
        if not os.path.exists(audio_file):
            print("Audio file not found:", audio_file)
            return

        model = whisper.load_model("large")  # Change the model to "large"
        print("Transcribing audio...")

        try:
            result = model.transcribe(audio_file)
            transcript = result["text"]
            print("Transcription completed.")

            transcript_file = video_title + ".txt"
            with open(transcript_file, "w") as file:
                file.write(transcript)
            print("Transcription saved to:", transcript_file)
        except Exception as e:
            print("An error occurred during transcription:", str(e))
            print("Transcription failed.")

    except Exception as e:
        print("An error occurred while loading the model or processing the audio:", str(e))

if __name__ == "__main__":
    video_url = input("Enter the YouTube video URL: ")
    audio_file, video_title = download_video(video_url)

    if audio_file:
        audio_file = os.path.abspath(audio_file)
        transcribe_audio(audio_file, video_title)
