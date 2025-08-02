# AI Multimedia Analyzer

AI Multimedia Analyzer is a web application that allows users to upload images, videos, and audio files to receive concise, AI-generated summaries for each type of media. The system provides tailored prompts and leverages the Gemini API for media analysis. User authentication is implemented via a MySQL database.

---

## Features

- **Image, Video, and Audio Summarization:**  
  Upload media files and receive short, meaningful summaries specific to their type.

- **Prompt Adaptation:**  
  Each media type has dedicated prompts to enhance the relevance and accuracy of summaries.

- **User Authentication:**  
  Secure login and registration using a MySQL backend.

- **Modern Tech Stack:**  
  - **Frontend:** HTML, CSS, JavaScript  
  - **Backend:** Python Flask  
  - **AI Integration:** Gemini API  
  - **Database:** MySQL (hosted on alwaysdata.net)  

---

## Demo



https://github.com/user-attachments/assets/f6d84521-51cf-4e77-af02-35cc5277b759


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
   The application will process the file using the Gemini API and display a concise summary tailored to the media type.

4. **Supported Problem Statements:**  
   - Quickly extract key information from multimedia content without manual review.
   - Save time in analyzing large or complex media files.
   - Enhance accessibility of multimedia content through text summaries.

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
