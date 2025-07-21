import whisper
import google.generativeai as genai
import warnings
warnings.filterwarnings("ignore", category=UserWarning, module="whisper")


# ✅ Step 1: Set your Gemini API key
genai.configure(api_key="AIzaSyCF1Rm9bSRBfVSvucT8IZq12OmfCgvGJlo")  # Replace with your API key

# ✅ Step 2: Load MP3 file
audio_path = "example_audio.mp3"  # 👉 Change to your actual audio file path

# ✅ Step 3: Load Whisper model and transcribe
print("🔍 Loading Whisper model...")
model = whisper.load_model("base")  # You can try "small", "medium", or "large" if needed

print("🧠 Transcribing audio with Whisper...")
result = model.transcribe(audio_path)
transcribed_text = result["text"]
print("📜 Transcribed Text:")
print(transcribed_text)

# ✅ Step 4: Generate Summary using Gemini
gemini_model = genai.GenerativeModel("models/gemini-2.0-flash")

response = gemini_model.generate_content([
    f"Transcribed Audio: {transcribed_text}\n\nSummarize this in a few sentences."
])

# ✅ Step 5: Print the summary
print("📝 Audio Summary:")
print(response.text)
