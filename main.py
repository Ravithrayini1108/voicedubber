import imageio_ffmpeg
from pydub import AudioSegment

# Fix ffmpeg path
ffmpeg_path = imageio_ffmpeg.get_ffmpeg_exe()
AudioSegment.converter = ffmpeg_path
AudioSegment.ffprobe = ffmpeg_path

from modules.audio_extractor import extract_audio
from modules.transcriber import transcribe
from modules.translator import translate_segments
from modules.tts_generator import generate_speech
from modules.aligner import align_and_merge
from modules.vocal_remover import remove_vocals

# ========== SETTINGS ==========
INPUT_FILE = "input/CoComelon.mp3"
TARGET_LANGUAGE = "hi"
# ==============================

def main():
    print("=" * 45)
    print("  🎵 Children's Rhyme Dubber")
    print("=" * 45)

    # Step 1: Extract clean audio
    audio_path = extract_audio(INPUT_FILE)

    # Step 2: Remove vocals to get background music only
    background_music = remove_vocals(audio_path)

    # Step 3: Transcribe English speech
    segments = transcribe(audio_path)

    # Step 4: Translate to target language
    segments = translate_segments(segments, target_lang=TARGET_LANGUAGE)

    # Step 5: Generate dubbed speech
    audio_clips = generate_speech(segments, lang=TARGET_LANGUAGE)

    # Step 6: Align & merge with background music
    original = AudioSegment.from_wav(audio_path)
    output = "output/dubbed_hindi.wav" if TARGET_LANGUAGE == "hi" else "output/dubbed_telugu.wav"
    align_and_merge(audio_clips, len(original), output_path=output, original_audio="input/background.mp3")

    print("\n🎉 All done! Open the output/ folder to hear your dubbed rhyme.")

if __name__ == "__main__":
    main()