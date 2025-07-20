import cv2
import google.generativeai as genai
from PIL import Image
import os

# ✅ Step 1: Gemini API key
genai.configure(api_key="AIzaSyCF1Rm9bSRBfVSvucT8IZq12OmfCgvGJlo")
model = genai.GenerativeModel("models/gemini-2.0-flash")

# ✅ Step 2: Extract key frames from the video
def extract_frames(video_path, interval=90):  # Every 90 frames (~3 sec at 30fps)
    frames = []
    cap = cv2.VideoCapture(video_path)
    frame_count = 0
    success, frame = cap.read()
    
    while success:
        if frame_count % interval == 0:
            frame_path = f"frame_{frame_count}.jpg"
            cv2.imwrite(frame_path, frame)
            frames.append(frame_path)
        success, frame = cap.read()
        frame_count += 1
    
    cap.release()
    return frames


def describe_frame(path):
    # Open image using PIL
    image = Image.open(path)
    
    # Pass the PIL Image object, not raw bytes
    response = model.generate_content(["Describe what's happening in this image.", image])
    return response.text


# ✅ Step 4: Combine into a summary
def summarize_video(video_path):
    print("📸 Extracting frames...")
    frame_paths = extract_frames(video_path)

    print("🧠 Describing key frames...")
    descriptions = []
    for path in frame_paths:
        desc = describe_frame(path)
        print(f"{path}: {desc}")
        descriptions.append(desc)
        os.remove(path)  # Clean up frames

    print("\n✨ Generating final summary...")
    final_response = genai.GenerativeModel("models/gemini-2.0-flash").generate_content([
        "Given these scene descriptions, create a short summary of the video:\n\n" + "\n".join(descriptions)
    ])
    
    return final_response.text

# ✅ Step 5: Run
video_path = "your_video.mp4"  # 🔄 Replace with your file
summary = summarize_video(video_path)

print("\n🎯 Video Summary:\n", summary)
