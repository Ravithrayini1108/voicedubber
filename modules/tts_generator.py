from gtts import gTTS
import os

def generate_speech(segments, lang="hi", output_dir="output/segments/"):
    os.makedirs(output_dir, exist_ok=True)
    print("🔄 Generating dubbed speech...")

    audio_clips = []
    for i, seg in enumerate(segments):
        out_file = f"{output_dir}seg_{i}.mp3"
        tts = gTTS(text=seg["translated"], lang=lang, slow=False)
        tts.save(out_file)
        audio_clips.append({
            "file": out_file,
            "start": seg["start"],
            "end": seg["end"]
        })
        print(f"  ✅ Segment {i+1}/{len(segments)} generated")

    print("✅ All speech segments generated!")
    return audio_clips