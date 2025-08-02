# AI Multimedia Analyzer

AI Multimedia Analyzer is an innovative web application designed to help users quickly and efficiently understand the content of images, videos, and audio files. By leveraging advanced AI through the Gemini API, the application automatically generates concise, meaningful summaries tailored to each media type. This tool is ideal for professionals, students, content curators, and anyone who deals with large volumes of multimedia content and needs to extract essential information rapidly.

---

## How It Works

1. **User Authentication:**  
   Users must register and log in using secure authentication. User credentials are managed via a MySQL database hosted on alwaysdata.net, ensuring data security and reliability.

2. **Media Upload:**  
   Users can upload images, videos, or audio files from their device through the intuitive web interface. The system accepts common formats for each media type.

3. **AI-Powered Summarization:**  
   - **Images:** The AI analyzes the uploaded image and generates a textual summary or description, capturing the main subjects, context, and any notable features.
   - **Videos:** The AI processes the video, identifies key scenes and topics, and provides a brief summary of the main content, saving users time from watching the entire clip.
   - **Audio:** The AI transcribes and summarizes the audio, highlighting the main points and themes, making it easy to grasp podcasts, lectures, or voice notes.

   Each media type uses prompts specifically engineered to maximize the relevance and accuracy of the AI's output.

4. **Results Display:**  
   Summaries are presented directly in the user's dashboard, allowing for quick review and, if needed, download or copy for further use.

---

## Features

- **Multi-Format Support:**  
  Upload and analyze images, videos, and audio—each with dedicated AI processing for the best results.

- **Custom Prompts:**  
  The system adapts its prompt to the specific media type, ensuring context-aware and accurate summaries.

- **Secure User Authentication:**  
  Registration and login processes are backed by a robust MySQL database, protecting user data.

- **Modern Tech Stack:**  
  - **Frontend:** HTML, CSS, JavaScript for a responsive user experience  
  - **Backend:** Python Flask, handling API calls and business logic  
  - **AI Integration:** Gemini API for advanced media analysis  
  - **Database:** MySQL (hosted on alwaysdata.net) for user management  

- **Problem Solving:**  
  - **Time-Saving:** Instantly grasp the essence of long videos, audio, or complex images.
  - **Accessibility:** Converts visual and audio content into text, aiding users with disabilities or those needing quick content reviews.
  - **Content Curation:** Helps educators, journalists, and researchers summarize and share key insights from multimedia sources.

---

## Demo


https://github.com/user-attachments/assets/2445fd06-f340-483e-ab6a-b8aefae8b080




---

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/Tangudu-Amar/multimeida-app.git
cd multimeida-app
```

### 2. Create and Activate a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate   # On Windows use: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the project root with the following structure:

```env
GEMINI_API_KEY=your_gemini_api_key
MYSQL_HOST=your_mysql_host
MYSQL_USER=your_mysql_user
MYSQL_PASSWORD=your_mysql_password
MYSQL_DB=your_mysql_db_name
```

> **Note:** MySQL database is hosted on alwaysdata.net. Replace the values above with your deployment credentials.

### 5. Run the Application

```bash
python app.py
```

The application will start on `http://localhost:5000`.

---

## Usage

1. **Register/Login:**  
   Create a user account or log in with existing credentials.

2. **Upload Media:**  
   Select an image, video, or audio file to upload.

3. **Receive Summaries:**  
   The application processes the file using the Gemini API and displays a concise summary tailored to the media type.

4. **Practical Scenarios Solved:**  
   - **Summarize long lectures, meetings, or podcasts without listening to the entire content.**
   - **Extract key information from images for documentation or quick reference.**
   - **Quickly understand the highlights of video content without viewing the whole file.**
   - **Increase accessibility by converting visual/audio content to text.**

---

## How Each Library in requirements.txt Is Used

- **Flask**: The core backend web framework used for routing, handling HTTP requests, and managing the server-side logic of the app.
- **python-dotenv**: Loads environment variables (like API keys and database credentials) from a `.env` file into the application.
- **google-generativeai**: Provides access to the Gemini API, which powers the AI-driven summarization of media files.
- **Pillow**: Handles image processing tasks, such as opening, resizing, and transforming images before analysis.
- **opencv-python**: Used for advanced image and video processing—extracting frames, analyzing video content, and preparing data for AI summarization.
- **moviepy**: Processes video files—extracting audio, cutting clips, and converting formats as needed for analysis.
- **requests**: Makes HTTP requests to external APIs (including the Gemini API) and other web services.
- **whisper**: An automatic speech recognition (ASR) model for transcribing audio content to text before summarization.
- **torch**: Provides the backend for running the Whisper ASR model and other deep learning tasks.
- **torchaudio**: Handles audio processing and transformations, especially for preparing audio files for speech recognition.
- **werkzeug**: Supplies utilities for WSGI applications, underlying Flask’s request/response handling.
- **python-docx**: Allows exporting summaries or analysis results as Word documents (.docx) for user download.
- **mysql-connector-python**: Connects the Flask app to the MySQL database for user authentication and data persistence.
- **gunicorn**: A WSGI HTTP server for deploying the Flask application in production environments.

---

## .env File Structure

```
GEMINI_API_KEY=your_gemini_api_key
MYSQL_HOST=your_mysql_host
MYSQL_USER=your_mysql_user
MYSQL_PASSWORD=your_mysql_password
MYSQL_DB=your_mysql_db_name
```

---

## Contact

For support or inquiries, please contact:  
- **GitHub:** [Tangudu-Amar](https://github.com/Tangudu-Amar)  
- **Email:** amartangudu2004.2@gmail.com

---

## Acknowledgements

- [Gemini API](https://ai.google.dev/gemini-api)
- [Alwaysdata](https://www.alwaysdata.com/)
