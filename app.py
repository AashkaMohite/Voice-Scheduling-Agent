from fastapi import FastAPI, HTTPException
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
def schedule_event(req: EventRequest):
    print("REQUEST:", req.dict())

    try:
        if not req.start_datetime:
            raise HTTPException(status_code=422, detail="start_datetime missing")

        link = create_event(
            name=req.name,
            start_datetime=req.start_datetime,
            attendee=req.attendee,
            end_datetime=req.end_datetime,
            duration_minutes=req.duration_minutes,
            title=req.title,
            agenda=req.agenda,
        )

        return {"status": "success", "event_link": link}

    except HTTPException:
        raise
    except Exception as e:
        print("❌ ERROR:", str(e))
        raise HTTPException(status_code=500, detail=str(e))