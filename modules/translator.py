from deep_translator import GoogleTranslator

def translate_segments(segments, target_lang="hi"):
    print(f"🔄 Translating to {'Hindi' if target_lang == 'hi' else 'Telugu'}...")
    translator = GoogleTranslator(source="en", target=target_lang)

    for seg in segments:
        seg["translated"] = translator.translate(seg["text"])
        print(f"  EN: {seg['text']}")
        print(f"  TR: {seg['translated']}\n")

    print("✅ Translation done!")
    return segments