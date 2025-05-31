# 🚀 AI Journey Planner

An AI-powered prototype designed to assist working adults in urban areas like Jakarta, Kuala Lumpur, Bangkok, Manila, and Hanoi in planning efficient daily commutes.

## 🎯 Objective

To help reduce travel time and improve user experience by leveraging GenAI to generate smart, human-like journey suggestions for congested cities.

## 🧠 Features

- ✅ AI-powered route suggestions using OpenAI's GPT model  
- ✅ Modular architecture for easy extension  
- ✅ Customizable for any global city  
- ✅ Lightweight and runs on localhost  

## 🛠️ Tech Stack

- Python  
- OpenAI API (GPT-3.5-Turbo)  
- dotenv (for environment variable handling)  
- Git/GitHub for version control  

## 🧩 Folder Structure

AIJourneyPlanner/
├── app.py
├── requirements.txt
├── .gitignore
├── README.md
└── planner/
├── init.py
└── route_planner.py

## 🔐 Environment Setup

Create a `.env` file and add:

```env
OPENAI_API_KEY=your_key_here
⚠️ Don't commit this file — it's already listed in .gitignore.

💡 How It Works

When the app is run, the user provides a starting point and a destination. The OpenAI model generates a friendly, intelligent route with context-aware tips and landmark-based detours.

Sample Output

Planning AI-powered route...
AI Suggested Route:
1. Start at your location in Jakarta and head towards Jalan Jenderal Sudirman, the main thoroughfare in the city.
2. As you approach the Semanggi area, make a stop at Plaza Semanggi to grab a quick breakfast.
3. Continue on to the Kuningan Business District. 

## 🧠 Architecture Diagram

![Architecture Diagram](https://raw.githubusercontent.com/Git786-lab/AI-Journey-Planner/refs/heads/main/ChatGPT%20Image%20May%2030%2C%202025%2C%2008_13_53%20PM.png)


💰 Estimated Monthly Costs
Service	Estimate
OpenAI API	~$5–$20 (based on usage)
Cloud Hosting (optional)	$0–$10 (e.g., Render, Replit, etc.)