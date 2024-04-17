
# YouTube Video Transcription

This project allows you to download a YouTube video, extract its audio, and transcribe the audio using the OpenAI Whisper API.

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


3. Enter the YouTube video URL when prompted.

4. The script will download the video, extract its audio, and save it as an MP3 file in the project directory.

5. The audio will be transcribed using the OpenAI Whisper API, and the transcription will be saved as a text file in the project directory.

## Dependencies

The project relies on the following Python packages:

- `pytube`: For downloading YouTube videos
- `moviepy`: For extracting audio from the downloaded video
- `python-dotenv`: For loading the OpenAI API key from the `.env` file
- `openai`: For transcribing the audio using the OpenAI Whisper API

These dependencies are listed in the `requirements.txt` file and will be automatically installed during the installation process.

## License

This project is licensed under the [MIT License](LICENSE).











