# 🎬 YouTube Summarizer

**YouTube Summarizer** is a web-based application that allows users to generate concise, meaningful summaries of YouTube videos. Whether you're trying to quickly understand a long lecture, catch up on a podcast, or extract insights from a documentary, this tool saves time and helps you focus on what matters most. Built with simplicity and power in mind, it harnesses the capabilities of advanced language models to turn long video content into digestible summaries.

---

## 🚀 Features

- **Automatic Transcript Retrieval**: Just paste a YouTube URL—our backend fetches the video transcript automatically (if available).
- **Smart Summarization**: Using OpenAI's GPT models, the tool condenses video transcripts into coherent summaries, preserving key ideas.
- **Clean and Simple UI**: Designed for ease of use, the interface guides you from input to summary in a few intuitive steps.
- **Fast & Lightweight**: Optimized for speed, the app delivers summaries in seconds without unnecessary bloat.
- **Cross-Platform Compatibility**: Works seamlessly on modern desktop browsers—no installation required.

---

## 🛠️ Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/nishantsingh604/yt-summarizer.git
   cd yt-summarizer
   ```

2. **Backend Setup**:
   ```bash
   cd backend
   pip install -r requirements.txt
   python app.py
   ```

3. **Frontend Setup**:
   ```bash
   cd ../frontend
   npm install
   npm start
   ```

---

## 🤖 Technologies Used

- **Frontend**:
  - HTML5, CSS3, JavaScript (Vanilla JS)
  - Responsive design principles
  - Axios for HTTP requests

- **Backend**:
  - Python 3
  - Flask (REST API framework)
  - youtube-transcript-api (for transcript extraction)

- **AI Integration**:
  - OpenAI API (for GPT-based summarization)
  - Prompt engineering for coherent and readable summaries

- **Dev Tools & Deployment**:
  - Git & GitHub for version control
  - npm & pip for dependency management
  - Cross-origin handling via Flask-CORS

---

## 📦 Project By

**Nishant Singh**  
[GitHub Profile](https://github.com/nishantsingh604)

---

