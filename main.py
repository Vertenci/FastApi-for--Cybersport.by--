from fastapi import FastAPI
from routes import games, matches

app = FastAPI()

app.include_router(games.router)
app.include_router(matches.router)
