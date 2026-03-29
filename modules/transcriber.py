import whisper
import os

# Tell whisper where ffmpeg is
os.environ["PATH"] += os.pathsep + r"C:\Users\Dell\PycharmProjects\voicedegubbger\.venv\Lib\site-packages\imageio_ffmpeg\binaries"

def transcribe(audio_path):
    print("🔄 Transcribing audio (this may take a minute)...")
    model = whisper.load_model("base")
    result = model.transcribe(audio_path, language="en")

    segments = []
    for seg in result["segments"]:
        segments.append({
            "text": seg["text"].strip(),
            "start": seg["start"],
            "end": seg["end"]
        })
        print(f"  [{seg['start']:.1f}s → {seg['end']:.1f}s] {seg['text'].strip()}")

    print(f"✅ Transcription done! {len(segments)} lines found.")
    return segments