from datetime import datetime
from fastapi import FastAPI, Request, Query, HTTPException
from typing import List, Dict, Any
import os
import pytz
import subprocess
import sys

# App initialization
app = FastAPI()


@app.get("/")
def root():
    return {"message": "Welcome to the FastAPI app!"}

@app.get("/helloworld")
async def hello_world(request: Request,
                     tz: str = Query(None, description="IANA timezone string, e.g. 'America/New_York'")):
    accept = request.headers.get("accept", "")
    message = "Hello World!"
    if tz:
        try:
            tzinfo = pytz.timezone(tz)
            now = datetime.now(tzinfo)
            message = f"Hello World! It is {now.strftime('%Y-%m-%d %H:%M:%S %Z')} in timezone {tz}."
        except pytz.UnknownTimeZoneError:
            raise HTTPException(status_code=400, detail="Invalid timezone specified.")
    if "application/json" in accept:
        return {"message": message}
    return message

def flatten_json(data: Dict[str, Any]) -> List[Any]:
    result = []
    for key, value in data.items():
        result.append(key)
        if isinstance(value, dict):
            result.extend(flatten_json(value))
        elif isinstance(value, list):
            for item in value:
                if isinstance(item, dict):
                    result.extend(flatten_json(item))
                else:
                    result.append(item)
        else:
            result.append(value)
    return result

@app.post("/unravel")
async def unravel(data: Dict[str, Any]):
    return flatten_json(data)

@app.get("/roll")
async def roll():
    try:
        subprocess.run(["git", "pull"], check=True)
        os.execv(sys.executable, [sys.executable] + sys.argv)
    except subprocess.CalledProcessError:
        raise HTTPException(status_code=500, detail="Failed to pull latest code.")
