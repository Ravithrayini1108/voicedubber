import subprocess
import os

FFMPEG = r"C:\Users\Dell\PycharmProjects\voicedegubbger\.venv\Scripts\ffmpeg.exe"

def remove_vocals(input_audio, output_path="output/background.wav"):
    print("🔄 Removing vocals from audio...")
    os.makedirs("output", exist_ok=True)

    # This ffmpeg filter removes center channel vocals
    subprocess.run([
        FFMPEG, "-y",
        "-i", input_audio,
        "-af", "pan=stereo|c0=c0-c1|c1=c1-c0",
        "-ac", "2",
        "-ar", "16000",
        output_path
    ], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    print(f"✅ Background music extracted: {output_path}")
    return output_path
