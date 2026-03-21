import datetime
import json
import os

from dateutil import parser
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from google.auth.transport.requests import Request

SCOPES = ["https://www.googleapis.com/auth/calendar"]


def authenticate():
    token_str = os.getenv("GOOGLE_TOKEN_JSON")
    if not token_str:
        raise ValueError("GOOGLE_TOKEN_JSON is not set")

    token_data = json.loads(token_str)
    creds = Credentials.from_authorized_user_info(token_data, SCOPES)

    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())

    if not creds or not creds.valid:
        raise ValueError("Google credentials are invalid and could not be refreshed")

    return creds


def create_event(
    name,
    start_datetime,
    attendee=None,
    end_datetime=None,
    duration_minutes=None,
    title=None,
    agenda=None,
):
    creds = authenticate()
    service = build("calendar", "v3", credentials=creds)

    start_time = parser.parse(start_datetime)

    if end_datetime:
        end_time = parser.parse(end_datetime)
    elif duration_minutes:
        end_time = start_time + datetime.timedelta(minutes=duration_minutes)
    else:
        end_time = start_time + datetime.timedelta(hours=1)

    if title:
        meeting_title = title
    elif attendee:
        meeting_title = f"Meeting with {attendee}"
    else:
        meeting_title = f"Meeting scheduled by {name}"

    description_parts = [f"Scheduled by: {name}"]

    if attendee:
        description_parts.append(f"Meeting with: {attendee}")

    if agenda:
        description_parts.append(f"Agenda: {agenda}")

    if duration_minutes and not end_datetime:
        description_parts.append(f"Duration: {duration_minutes} minutes")

    description = "\n".join(description_parts)

    print("AGENDA RECEIVED:", agenda)
    print("DESCRIPTION:", description)

    event = {
        "summary": meeting_title,
        "description": description,
        "start": {
            "dateTime": start_time.isoformat(),
            "timeZone": "America/Edmonton",
        },
        "end": {
            "dateTime": end_time.isoformat(),
            "timeZone": "America/Edmonton",
        },
    }

    created_event = service.events().insert(
        calendarId="primary",
        body=event
    ).execute()

    return created_event.get("htmlLink")