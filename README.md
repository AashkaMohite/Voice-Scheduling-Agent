# Voice Scheduling Agent

A real-time voice assistant that schedules meetings using natural language and integrates with Google Calendar.

---

## Overview

This project is a conversational voice AI agent that allows users to schedule meetings through voice. It extracts structured meeting details from natural speech and creates real calendar events using the Google Calendar API.

The system is designed to be flexible, human-like, and production-oriented, supporting optional fields, smart defaults, and natural conversation flow.

---

## Features

- Natural voice conversation (via Vapi)
- Extracts:
  - Name
  - Date & time
  - Attendee (optional)
  - Duration or end time
  - Title (optional)
  - Agenda (optional)
- Defaults:
  - Year defaults to 2026
  - Duration defaults to 60 minutes
- Converts natural language to structured datetime
- Creates real Google Calendar events
- Deployed backend (FastAPI + Render)


---

## Deployed API

https://voice-scheduling-agent-ydaj.onrender.com

Test endpoint:
- /docs


---

## How to Test the Agent

1. Open the Vapi agent link: https://vapi.ai/?demo=true&shareKey=7a0a88d2-9d64-4855-8164-dc910a223685&assistantId=72367bc4-85be-429f-8f68-affec52bc97e 

2. Speak naturally, for example:
“Hi, my name is Jerry. Schedule a meeting with Tom on 30th March at 5 PM for 30 minutes about project planning.”

3. Confirm when asked:
    "Yes, please schedule it."
  
4. Check Google Calendar for the created event


---

## Technology Used 

-⁠  ⁠*Backend:* FastAPI (Python) <br>
-⁠  ⁠*Voice Interface:* VAPI <br>
-⁠  ⁠*Calendar Integration:* Google Calendar API <br>
-⁠  ⁠*Deployment:* Render <br>
-⁠  ⁠*Libraries:* <br>
  - ⁠ google-api-python-client ⁠
  - ⁠ google-auth ⁠
  - ⁠ python-dateutil ⁠
  - ⁠ pydantic ⁠


---  

## Google Calendar Integration

-⁠  ⁠Uses Google OAuth credentials <br>
-⁠  ⁠Tokens are stored securely via environment variables <br>
-⁠  ⁠Automatically refreshes expired tokens <br>
-⁠  ⁠Creates events in the authenticated user's primary calendar <br>
-⁠  ⁠Supports: <br>
  - dynamic time parsing
  - duration-based scheduling
  - structured event descriptions (attendee, agenda, etc.)

---

## Security

-⁠  ⁠Google OAuth tokens are stored securely using environment variables <br>
-⁠  ⁠No sensitive credentials are committed to the repository <br>
-⁠  ⁠Backend access is controlled via API endpoints 


---

## Run Locally (Optional)

git clone https://github.com/AashkaMohite/Voice-Scheduling-Agent 
cd voice_scheduling_agent

pip install -r requirements.txt
uvicorn app:app --reload

Set environment variable: export GOOGLE_TOKEN_JSON='YOUR_TOKEN_JSON'

Example API Request

{
  "name": "ASH", <br>
  "start_datetime": "2026-03-22T16:00:00", <br>
  "duration_minutes": 30, <br>
  "attendee": "John", <br>
  "title": "Project Sync", <br>
  "agenda": "Discuss roadmap" <br>
}

---

## Scope & Current Limitation

Currently, events are created in the developer’s Google Calendar, as the application uses a single OAuth token configured for this environment.

This design was chosen to simplify deployment and demonstrate end-to-end functionality of the scheduling pipeline.

In a production setup, this can be extended to support multi-user authentication, where each user connects their own Google Calendar via OAuth. This would enable events to be created directly in the user's personal calendar.





