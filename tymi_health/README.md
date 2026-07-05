# TYMI Health Companion

A full-stack health companion application featuring a nurse triage system powered by Groq AI.

## Project Structure

- `frontend/`: HTML/CSS/JS frontend (TeleportHQ style export)
- `backend/`: Python Flask API
- `tymi_health.db`: SQLite database

## Setup Instructions

### Backend Setup
1. Navigate to the `backend/` directory.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Add your Groq API Key to `AI.env`:
   ```
   GROQ_API_KEY=your_actual_key_here
   ```
4. Start the server:
   ```bash
   python server.py
   ```

### Frontend Setup
1. Open `frontend/index.html` in any modern web browser.
2. Ensure the backend is running so the frontend can fetch and submit data.

## Features
- **Patient Intake**: Submit patient vitals and symptoms.
- **AI Triage**: Automatic categorization (Red, Orange, Yellow, Green) using Groq Llama 3.
- **Dashboard**: Real-time view of patient status and counts.
- **Local Storage**: All records stored in a local SQLite database.
