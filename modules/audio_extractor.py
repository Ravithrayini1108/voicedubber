import subprocess
import os

FFMPEG = r"C:\Users\Dell\PycharmProjects\voicedegubbger\.venv\Lib\site-packages\imageio_ffmpeg\binaries\ffmpeg-win-x86_64-v7.1.exe"

def extract_audio(input_path, output_path="input/clean_audio.wav"):
    print("🔄 Extracting audio...")
    os.makedirs("input", exist_ok=True)
    subprocess.run([
        FFMPEG, "-y",
        "-i", input_path,
        "-ac", "1",
        "-ar", "16000",
        output_path
    ], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print("✅ Audio extracted successfully!")
    return output_path