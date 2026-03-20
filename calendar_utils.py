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


def parse_meeting_time(datetime_str: str) -> datetime.datetime:
    cleaned = datetime_str.strip()

    # First try standard parsing
    try:
        return parser.parse(cleaned, fuzzy=True)
    except Exception:
        pass

    raise ValueError(f"Could not parse datetime: {datetime_str}")


def create_event(name, datetime_str, title=None):
    creds = authenticate()
    service = build("calendar", "v3", credentials=creds)

    start_time = parse_meeting_time(datetime_str)
    end_time = start_time + datetime.timedelta(hours=1)

    event = {
        "summary": title if title else f"Meeting with {name}",
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