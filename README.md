# Athlete Fit GenAI Chatbot 🏃‍♂️🚴‍♀️🤖

A personalized AI-powered chatbot that generates endurance-focused fitness training plans based on user inputs — hosted locally using [Ollama](https://ollama.com/) and Python.

## 🧠 Overview

This project leverages **GenAI (Generative AI)** models running locally via Ollama to generate structured, goal-oriented training plans for athletes. Whether you're into running or cycling, this chatbot offers a tailored 6-week training roadmap based on your current fitness level, sports preferences, and schedule.

## ✅ Features

- 🏋️‍♂️ Generate custom training plans based on:
  - Fitness goal (e.g., increase endurance)
  - Sports (e.g., running, cycling)
  - Experience level (e.g., beginner, intermediate, advanced)
  - Weekly training commitment
  - Duration in weeks
- 🤖 Powered by locally hosted Ollama LLM models
- 🔐 Runs fully offline — no cloud dependencies
- 🌐 Future integration with:
  - **Strava & Garmin APIs** using Swagger/OpenAPI
  - Smartwatch data pipelines for real-time fitness adaptation

## 📂 Project Structure

athlete-fit-genai-chatbot/
├── json_query_claude.py # Python script to query LLM and print training plan
├── .env # Environment file for API keys or configs (excluded from Git)
├── venv/ # Python virtual environment


## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/janagoudarniroop/genai.git
cd athlete-fit-genai-chatbot


2. Set Up the Virtual Environment

python3 -m venv venv
source venv/bin/activate

3. Install Dependencies

pip install -r requirements.txt


4. Run the Script

python3 json_query_claude.py

Paste your JSON input like:

{
  "goal": "increase endurance",
  "training_days": 5,
  "sports": ["running", "cycling"],
  "experience_level": "intermediate",
  "duration_weeks": 6
}



 Future Enhancements
🌐 OAuth integration with Strava & Garmin for fitness tracking

📈 Smartwatch syncing for real-time workout adjustment

📊 Web-based dashboard to view and download training plans

🎙️ Voice chatbot interface using Whisper + LLM




 Tech Stack
Python 3.11

Ollama (LLM runtime)

Local CLI interface

Planned: Swagger/OpenAPI for fitness APIs


Author
Niroop Janagoudar


GitHub Repo: https://github.com/janagoudarniroop/genai
LinkedIn Profile: https://www.linkedin.com/in/niroop-janagoudar-a82280146/
