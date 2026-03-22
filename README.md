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
Open the Vapi agent link and speak naturally, for example:
“Hi, my name is Jerry. Schedule a meeting with Tom tomorrow at 5 PM for 30 minutes about project planning.”
Confirm when asked and check Google Calendar for the created event


---

## Technology Used 

- FastAPI (backend)
- Google Calendar API
- Vapi (voice interface)
- Python
- Render (deployment)

---  

## Google Calendar Integration

- Uses Google OAuth credentials
- Stores tokens securely via environment variables
- Automatically refreshes expired tokens





