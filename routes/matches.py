from fastapi import APIRouter, HTTPException
import httpx
from models import Match
import logging

router = APIRouter()
BASE_URL_MATCHES = "https://127.0.0.1:8000/matches/api/matches/"

logging.basicConfig(level=logging.INFO)


@router.get("/matches/", tags=['Matches'])
async def get_matches():
    async with httpx.AsyncClient(verify=False) as client:
        response = await client.get(BASE_URL_MATCHES)
        return response.json()


@router.get("/matches/{match_id}/", tags=['Matches'])
async def get_match(match_id: int):
    async with httpx.AsyncClient(verify=False) as client:
        response = await client.get(f"{BASE_URL_MATCHES}{match_id}/")
        if response.status_code == 404:
            raise HTTPException(status_code=404, detail="Match not found")
        return response.json()


@router.post("/matches/", tags=['Matches'])
async def create_match(match: Match):
    logging.info(f"Received match data: {match}")
    async with httpx.AsyncClient(verify=False) as client:
        serialized_match = match.dict()
        response = await client.post(BASE_URL_MATCHES, json=serialized_match)
        if response.status_code == 400:
            logging.error(f"Error response: {response.text}")
            raise HTTPException(status_code=400, detail="Invalid data")
        return response.json()


@router.delete("/matches/{match_id}", tags=['Matches'])
async def delete_match(match_id: int):
    async with httpx.AsyncClient(verify=False) as client:
        response = await client.delete(f"{BASE_URL_MATCHES}{match_id}/")
        if response.status_code == 404:
            raise HTTPException(status_code=404, detail="Match not found")
        return {"detail": "Match deleted"}


@router.put("/matches/{match_id}", tags=['Matches'])
async def update_match(match_id: int, match: Match):
    async with httpx.AsyncClient(verify=False) as client:
        response = await client.put(f"{BASE_URL_MATCHES}{match_id}/", json=match.dict())
        if response.status_code == 404:
            raise HTTPException(status_code=404, detail="Match not found")
        return response.json()
