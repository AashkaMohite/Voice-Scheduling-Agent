from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from calendar_utils import create_event

app = FastAPI()

class EventRequest(BaseModel):
    name: str
    start_datetime: str
    attendee: str = None
    end_datetime: str = None
    duration_minutes: int = None
    title: str = None
    agenda: str = None

@app.get("/")
def home():
    return {"message": "Voice Scheduler API is running"}

@app.post("/create-event")
def schedule_event(req: EventRequest):
    try:
        link = create_event(
            name=req.name,
            start_datetime=req.start_datetime,
            attendee=req.attendee,
            end_datetime=req.end_datetime,
            duration_minutes=req.duration_minutes,
            title=req.title,
            agenda=req.agenda,
        )
        return {
            "status": "success",
            "event_link": link
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))