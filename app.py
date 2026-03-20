from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from calendar_utils import create_event

app = FastAPI()

class EventRequest(BaseModel):
    name: str
    datetime: str
    title: str = None

@app.get("/")
def home():
    return {"message": "Voice Scheduler API is running"}

@app.post("/create-event")
def schedule_event(req: EventRequest):
    try:
        link = create_event(req.name, req.datetime, req.title)
        return {
            "status": "success",
            "event_link": link
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))