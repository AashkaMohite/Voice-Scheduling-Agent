from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel
from calendar_utils import create_event
from typing import Optional

app = FastAPI()

class EventRequest(BaseModel):
    name: Optional[str] = None
    start_datetime: Optional[str] = None
    attendee: Optional[str] = None
    end_datetime: Optional[str] = None
    duration_minutes: Optional[int] = None
    title: Optional[str] = None
    agenda: Optional[str] = None

@app.get("/")
def home():
    return {"message": "Voice Scheduler API is running"}

@app.post("/create-event")
async def schedule_event(request: Request):
    body = await request.json()
    print("RAW REQUEST FROM VAPI:", body)

    try:
        req = EventRequest(**body)

        start_value = req.start_datetime 
        if not start_value:
            raise HTTPException(status_code=422, detail="start_datetime missing")

        link = create_event(
            name=req.name,
            start_datetime=start_value,
            attendee=req.attendee,
            end_datetime=req.end_datetime,
            duration_minutes=req.duration_minutes,
            title=req.title,
            agenda=req.agenda,
        )

        return {"status": "success", "event_link": link}

    except Exception as e:
        print("❌ ERROR:", str(e))
        raise HTTPException(status_code=500, detail=str(e))