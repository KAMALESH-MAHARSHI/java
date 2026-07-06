"""
Generate Kannada voice commentary using Google Cloud Text-to-Speech (Chirp 3: HD).

SETUP (one-time):
1. Create/select a project in Google Cloud Console: https://console.cloud.google.com
2. Enable the "Cloud Text-to-Speech API" for that project.
3. Create a service account key (JSON) or run: gcloud auth application-default login
4. Install the client library:
       pip install google-cloud-texttospeech --break-system-packages
5. Set your credentials env var (if using a service account JSON key):
       export GOOGLE_APPLICATION_CREDENTIALS="/path/to/key.json"

Then just run:
       python generate_kannada_tts.py
"""

from google.cloud import texttospeech

# ---- Your Kannada commentary script ----
SCRIPT_TEXT = """
ಇಗೋ ಬರ್ತಿದೆ ಹೊಸ Nothing Phone (3a) RCB edition!
ಈ ಫೋನ್‌ನ ಡಿಸೈನ್ ತುಂಬಾ ವಿಭಿನ್ನ, ಬ್ಯಾಕ್ ಸೈಡ್‌ನಲ್ಲಿ ಇರುವ ಲೈಟಿಂಗ್ ಮತ್ತು ಸ್ಪೆಷಲ್ ಕಲರ್ ಲುಕ್ ಇದಕ್ಕೆ ಇನ್ನಷ್ಟು ಸ್ಟೈಲ್ ಕೊಡುತ್ತೆ.
6.77 ಇಂಚಿನ AMOLED ಡಿಸ್‌ಪ್ಲೇ, 120Hz ರಿಫ್ರೆಶ್ ರೇಟ್‌ನೊಂದಿಗೆ ಸ್ಮೂತ್ ವೀಕ್ಷಣೆಯ ಅನುಭವ ಕೊಡುತ್ತದೆ.
Snapdragon 7s Gen 3 ಪ್ರೊಸೆಸರ್‌ನಿಂದ ದಿನನಿತ್ಯದ ಬಳಕೆ, ಗೇಮಿಂಗ್, ಮತ್ತು ಮಲ್ಟಿಟಾಸ್ಕಿಂಗ್ ಎಲ್ಲವೂ ಫಾಸ್ಟ್ ಆಗಿರುತ್ತೆ.
50MP ಟ್ರಿಪಲ್ ಕ್ಯಾಮೆರಾ ಸೆಟ್‌ಅಪ್‌ನಲ್ಲಿ OIS, ಟೆಲಿಫೋಟೋ, ಮತ್ತು ಅಲ್ಟ್ರಾವೈಡ್ ಸಪೋರ್ಟ್ ಕೂಡ ಇದೆ.
5000 mAh ಬ್ಯಾಟರಿ ಮತ್ತು 50W ಫಾಸ್ಟ್ ಚಾರ್ಜಿಂಗ್‌ನಿಂದ ದೀರ್ಘಕಾಲ ಬಳಕೆಗೂ, ವೇಗವಾದ ಚಾರ್ಜಿಂಗ್‌ಗೂ ಇದು ಸೂಕ್ತ.
ಒಟ್ಟಿನಲ್ಲಿ, ಸ್ಟೈಲ್ ಮತ್ತು ಪರ್ಫಾರ್ಮೆನ್ಸ್ ಎರಡನ್ನೂ ಇಷ್ಟಪಡುವವರಿಗೆ ಇದು ಒಂದು ಆಕರ್ಷಕ ಸ್ಪೆಷಲ್ ಎಡಿಷನ್!
""".strip()

OUTPUT_FILE = "nothing_phone_3a_rcb_kannada.mp3"

# Recommended: Chirp 3 HD Kannada voice (natural, expressive, best for reels/shorts)
# Male options typically named like: kn-IN-Chirp3-HD-<Name>
# Check available names for your project/region via:
#   client.list_voices(language_code="kn-IN")
VOICE_NAME = "kn-IN-Chirp3-HD-Achernar"   # placeholder — verify exact name (see list_voices below)


def list_available_kannada_voices():
    """Run this first to see exact voice names available to your project."""
    client = texttospeech.TextToSpeechClient()
    voices = client.list_voices(language_code="kn-IN")
    for v in voices.voices:
        print(v.name, v.ssml_gender, v.natural_sample_rate_hertz)


def synthesize():
    client = texttospeech.TextToSpeechClient()

    synthesis_input = texttospeech.SynthesisInput(text=SCRIPT_TEXT)

    voice = texttospeech.VoiceSelectionParams(
        language_code="kn-IN",
        name=VOICE_NAME,
    )

    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3,
        speaking_rate=1.05,   # slightly faster, good for short-form video pacing
        pitch=0.0,
    )

    response = client.synthesize_speech(
        input=synthesis_input, voice=voice, audio_config=audio_config
    )

    with open(OUTPUT_FILE, "wb") as out:
        out.write(response.audio_content)
        print(f"Audio content written to {OUTPUT_FILE}")


if __name__ == "__main__":
    # Uncomment the next line the first time to find the exact voice name available to you:
    # list_available_kannada_voices()
    synthesize()