from fastapi import FastAPI, Depends, HTTPException
import os
from fastapi.middleware.cors import CORSMiddleware
from api.endpoints import flight_attendants

# Add CORS middleware
# origins = [
#     "http://localhost:3000",  # Allow your local frontend to access the backend
#     "http://localhost:3002",  # Allow your local frontend to access the backend
#     "http://localhost:3001",  # Allow your local frontend to access the backend
#     "https://varcard.io",
#     "https://www.varcard.io"  # Add your production frontend domain if it's different from the backend domain
# ]

origins = ["*"]

print("Running in Docker: ", os.environ.get("RUNNING_IN_DOCKER"))
if os.environ.get("RUNNING_IN_DOCKER"):
    from app.api.endpoints import search
else:
    from api.endpoints import search

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"]
)

app.include_router(search.router)
app.include_router(flight_attendants.router)


@app.get("/elisabeth")
def read_root():
    return {"Hi": "Flight Attendant! :))))"}


@app.on_event("startup")
async def startup_event():
    print("Starting up...")
    # For future: maybe establish a connection pool or other startup tasks


@app.on_event("shutdown")
async def shutdown_event():
    # For future: maybe close the connection pool or other shutdown tasks
    pass
