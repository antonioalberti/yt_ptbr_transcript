
# YouTube Video Transcription

This Python script allows you to download a YouTube video, extract the audio, and generate a transcript using the Whisper API.

## Prerequisites

Before running the script, make sure you have the following dependencies installed:

- Python 3.x
- `pytube` library: Install using `pip install pytube`
- `moviepy` library: Install using `pip install moviepy`
- `whisper` library: Install using `pip install git+https://github.com/openai/whisper.git`

## Installation

### Windows

1. Clone the repository or download the `main.py` and `install.bat` files.

2. Open a command prompt and navigate to the directory where the files are located.

3. Run the `install.bat` file by double-clicking on it or executing the following command in the command prompt:

install.bat


This will automatically install the required dependencies (`pytube`, `moviepy`, and `whisper`) using `pip`.

### Other Operating Systems

1. Clone the repository or download the `main.py` file.

2. Open a terminal and navigate to the directory where the `main.py` file is located.

3. Install the required dependencies manually by running the following commands:

pip install pytube
pip install moviepy
pip install git+https://github.com/openai/whisper.git


## Usage

1. Open a terminal or command prompt and navigate to the directory where the `main.py` file is located.

2. Run the script using the following command:

python main.py


3. When prompted, enter the URL of the YouTube video you want to transcribe.

4. The script will download the video, extract the audio, and generate a transcript using the Whisper API.

5. The transcript will be saved as a text file with the same name as the video title (with spaces replaced by underscores) in the same directory as the script.

## Customization

- You can change the model used for transcription by modifying the line `model = whisper.load_model("large")` in the `transcribe_audio()` function. Replace `"large"` with the desired model name. Available models include:
  - `"tiny"`: A tiny model with approximately 39 million parameters.
  - `"base"`: The base model with approximately 74 million parameters.
  - `"small"`: A small model with approximately 244 million parameters.
  - `"medium"`: A medium-sized model with approximately 769 million parameters.
  - `"large"`: A large model with approximately 1.55 billion parameters.

  Note: Larger models provide higher accuracy but require more computational resources and may take longer to transcribe the audio.

- If you encounter any issues or errors during the transcription process, additional error handling and logging statements are included in the code to help identify the problem.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgements

- The Whisper API is developed by OpenAI. For more information, visit [https://github.com/openai/whisper](https://github.com/openai/whisper).
- The `pytube` library is used for downloading YouTube videos. For more information, visit [https://github.com/pytube/pytube](https://github.com/pytube/pytube).
- The `moviepy` library is used for extracting audio from the downloaded video. For more information, visit [https://github.com/Zulko/moviepy](https://github.com/Zulko/moviepy).

