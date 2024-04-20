# YouTube Video Transcription

This project allows you to download a YouTube video, split it into parts, extract audio from each part, and transcribe the audio using the OpenAI Whisper API.

## Prerequisites

- Python 3.x
- OpenAI API key

## Installation

1. Clone the repository:

git clone https://github.com/your-username/your-repository.git

2. Navigate to the project directory:

cd your-repository

3. Run the `install.bat` script to create a virtual environment and install the required packages:

install.bat

This script will create a virtual environment named `myenv`, activate it, and install the packages listed in the `requirements.txt` file.

4. Create a `.env` file in the project directory and add your OpenAI API key:

OPENAI_API_KEY=your-api-key


Replace `your-api-key` with your actual OpenAI API key.

## Usage

5. Make sure the virtual environment is activated. If not, activate it by running:

myenv\Scripts\activate

6. Run the `main.py` script:

python main.py


7. Enter the YouTube video URL when prompted.

8. The script will download the video, split it into parts, extract audio from each part, and save the audio files in the "downloads" folder.

9. The audio from each part will be transcribed using the OpenAI Whisper API, and the transcription will be saved as a text file in the "downloads" folder.

## Customization

- You can customize the duration of each video part by modifying the `part_duration` variable in the `main.py` script. By default, it is set to 10 minutes (600 seconds).

- The video parts are saved as black screens instead of the original video content to reduce file size. If you want to include the original video content, you can modify the `split_video_into_parts` function in the `main.py` script.

## Dependencies

The project relies on the following Python packages:

- `pytube`: For downloading YouTube videos
- `moviepy`: For splitting the video into parts and extracting audio
- `python-dotenv`: For loading the OpenAI API key from the `.env` file
- `openai`: For transcribing the audio using the OpenAI Whisper API

These dependencies are listed in the `requirements.txt` file and will be automatically installed during the installation process.

## License

This project is licensed under the [MIT License](LICENSE).