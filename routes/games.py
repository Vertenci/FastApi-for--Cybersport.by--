from fastapi import APIRouter, HTTPException
import httpx
from models import Game


router = APIRouter()
BASE_URL_GAMES = "https://127.0.0.1:8000/api/games/"


@router.get("/games/", tags=['Games'])
async def get_games():
    async with httpx.AsyncClient(verify=False) as client:
        response = await client.get(BASE_URL_GAMES)
        return response.json()


@router.get("/games/{game_id}/", tags=['Games'])
async def get_game(game_id: int):
    async with httpx.AsyncClient(verify=False) as client:
        response = await client.get(f"{BASE_URL_GAMES}{game_id}/")
        if response.status_code == 404:
            raise HTTPException(status_code=404, detail="Game not found")
        return response.json()


@router.post("/games/", tags=['Games'])
async def create_game(game: Game):
    async with httpx.AsyncClient(verify=False) as client:
        response = await client.post(BASE_URL_GAMES, json=game.dict())
        return response.json()


@router.delete("/games/{game_id}", tags=['Games'])
async def delete_game(game_id: int):
    async with httpx.AsyncClient(verify=False) as client:
        response = await client.delete(f"{BASE_URL_GAMES}{game_id}/")
        if response.status_code == 404:
            raise HTTPException(status_code=404, detail="Game not found")
        return {"detail": "Game deleted"}


@router.put("/games/{game_id}", tags=['Games'])
async def update_game(game_id: int, game: Game):
    async with httpx.AsyncClient(verify=False) as client:
        response = await client.put(f"{BASE_URL_GAMES}{game_id}/", json=game.dict())
        if response.status_code == 404:
            raise HTTPException(status_code=404, detail="Game not found")
        return response.json()
