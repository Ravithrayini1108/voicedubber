import subprocess
import os

FFMPEG = r"C:\Users\Dell\PycharmProjects\voicedegubbger\.venv\Scripts\ffmpeg.exe"

def convert_mp3_to_wav(mp3_path, wav_path):
    subprocess.run([
        FFMPEG, "-y",
        "-i", mp3_path,
        "-ac", "1",
        "-ar", "16000",
        wav_path
    ], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

def align_and_merge(audio_clips, total_duration_ms, output_path="output/dubbed.wav", original_audio=None):
    print("🔄 Aligning and merging audio segments...")
    os.makedirs("output", exist_ok=True)
    os.makedirs("output/wav_segments", exist_ok=True)

    # Convert all mp3 segments to wav first
    inputs = []
    filter_parts = []

    for i, clip in enumerate(audio_clips):
        wav_path = f"output/wav_segments/seg_{i}.wav"
        convert_mp3_to_wav(clip["file"], wav_path)
        delay_ms = int(clip["start"] * 1000)
        inputs += ["-i", wav_path]
        filter_parts.append(f"[{i}]adelay={delay_ms}|{delay_ms}[s{i}]")

    # Mix all dubbed voice segments together
    mix_inputs = "".join([f"[s{i}]" for i in range(len(audio_clips))])
    filter_parts.append(f"{mix_inputs}amix=inputs={len(audio_clips)}:normalize=0,volume=3.0[voice]")

    # Add original background music at lower volume
    if original_audio:
        n = len(audio_clips)
        inputs += ["-i", original_audio]
        filter_parts.append(f"[{n}]volume=0.15[bg]")
        filter_parts.append(f"[voice][bg]amix=inputs=2:normalize=0[out]")
    else:
        filter_parts.append(f"[voice]acopy[out]")

    filter_complex = ";".join(filter_parts)

    cmd = [FFMPEG, "-y"]
    cmd += inputs
    cmd += [
        "-filter_complex", filter_complex,
        "-map", "[out]",
        "-ac", "1",
        "-ar", "16000",
        output_path
    ]

    subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print(f"✅ Final dubbed audio saved to: {output_path}")
    return output_path