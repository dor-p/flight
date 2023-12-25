# api/endpoints/search.py
from fastapi import APIRouter, Depends, HTTPException, Request, Response
import os

if os.environ.get("RUNNING_IN_DOCKER"):
    from app.db.sessions import get_db_session
else:
    from db.sessions import get_db_session

router = APIRouter()


@router.options("/flight-attendants")
def options_handler(request: Request):
    return Response(status_code=204)


@router.get("/flight-attendants")
async def list_flight_attendants(request: Request, conn=Depends(get_db_session)):
    query = "SELECT * FROM flight_attendants;"
    rows = await conn.fetch(query)  # Using fetch method to get all rows
    # Convert rows to list of dicts if necessary
    flight_attendants = [dict(row) for row in rows]
    return {"flight_attendants": flight_attendants}
