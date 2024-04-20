from pytube import YouTube
from moviepy.editor import *
import os
import re
import openai
from dotenv import load_dotenv

# Load the API key from the .env file
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def download_video(url, output_dir):
    video = YouTube(url)
    stream = video.streams.get_highest_resolution()
    
    # Download the video
    output_filename = "video.mp4"
    output_path = os.path.join(output_dir, output_filename)
    stream.download(output_dir, filename=output_filename)
    
    # Check if the video is inside a folder
    if os.path.isdir(output_path):
        video_files = [f for f in os.listdir(output_path) if f.endswith(".mp4")]
        if video_files:
            video_file = os.path.join(output_path, video_files[0])
            os.rename(video_file, output_path)
            os.rmdir(output_path)
    
    return output_path, video.title

def split_video_into_parts(video_path, output_dir, duration):
    video_clip = VideoFileClip(video_path)
    total_duration = video_clip.duration
    
    video_parts = []
    start_time = 0
    end_time = duration
    part_num = 1
    
    while start_time < total_duration:
        part_filename = f"video_part_{part_num}.mp4"
        part_path = os.path.join(output_dir, part_filename)
        
        # Create a black screen clip with the same duration as the video part
        black_screen = ColorClip(video_clip.size, color=(0, 0, 0), duration=min(duration, total_duration - start_time))
        
        # Write the black screen clip to a file
        black_screen.write_videofile(part_path, fps=video_clip.fps)
        video_parts.append(part_path)
        
        start_time = end_time
        end_time = min(start_time + duration, total_duration)
        part_num += 1
    
    video_clip.close()
    
    return video_parts

def extract_audio_from_parts(video_parts, output_dir):
    audio_parts = []
    
    for video_part in video_parts:
        video_clip = VideoFileClip(video_part)
        audio_clip = video_clip.audio
        
        audio_filename = os.path.splitext(os.path.basename(video_part))[0] + ".mp3"
        audio_path = os.path.join(output_dir, audio_filename)
        
        audio_clip.write_audiofile(audio_path)
        audio_parts.append(audio_path)
        
        video_clip.close()
        audio_clip.close()
    
    return audio_parts

def transcribe_audio_parts(audio_parts, output_file):
    with open(output_file, "w") as file:
        for audio_part in audio_parts:
            with open(audio_part, "rb") as audio_file:
                transcript = openai.Audio.transcribe("whisper-1", audio_file)
                file.write(transcript["text"])
                file.write("\n")

if __name__ == "__main__":
    video_url = input("Enter the YouTube video URL: ")
    
    # Create the "downloads" folder if it doesn't exist
    downloads_folder = "downloads"
    os.makedirs(downloads_folder, exist_ok=True)
    
    # Download the video
    video_path, video_title = download_video(video_url, downloads_folder)
    
    # Create a folder for the video using the video title
    video_folder = re.sub(r'[\\/*?:"<>|\s]', "_", video_title)
    video_output_dir = os.path.join(downloads_folder, video_folder)
    os.makedirs(video_output_dir, exist_ok=True)
    
    # Move the downloaded video to the video folder
    video_filename = os.path.basename(video_path)
    new_video_path = os.path.join(video_output_dir, video_filename)
    os.rename(video_path, new_video_path)
    
    # Split the video into parts with black screens
    part_duration = 10 * 60  # 10 minutes per part
    video_parts = split_video_into_parts(new_video_path, video_output_dir, part_duration)
    
    # Extract audio from each video part
    audio_parts = extract_audio_from_parts(video_parts, video_output_dir)
    
    # Transcribe each audio part separately
    output_file = os.path.join(video_output_dir, f"{video_folder}_transcription.txt")
    transcribe_audio_parts(audio_parts, output_file)
    
    print("Transcription completed. Output file:", output_file)
