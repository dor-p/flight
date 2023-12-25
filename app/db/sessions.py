import asyncpg
import os

if os.environ.get("RUNNING_IN_DOCKER"):
    from app.core.config import DATABASE_URL
else:
    from core.config import DATABASE_URL


async def get_db_session():
    connection = await asyncpg.connect(DATABASE_URL)
    print("Got db session")
    return connection
