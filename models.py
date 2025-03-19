from typing import Optional, List

from pydantic import BaseModel


class Game(BaseModel):
    id: int
    icon: str
    name: str


class Team(BaseModel):
    id: int
    name: str
    icon: str
    founding_date: str
    team_history: str
    prize: int
    country: str
    icon_country: str
    site: str


class Player(BaseModel):
    id: int
    team: Optional[Team]
    game: Optional[Game]
    nickname: str
    fio: str
    datebirth: str
    country: str
    sum_prize: int
    description: str
    wins: int
    draws: int
    loses: int


class Tournament(BaseModel):
    id: int
    game: int
    teams: List[Team]
    name: str
    description: str
    start_date: str
    end_date: str
    sum_prize: int
    location: str


class Indicator(BaseModel):
    id: int
    team: Team
    tournament: int
    match: Optional[int]
    wins: Optional[int]
    loses: Optional[int]
    draws: Optional[int]
    achievements: Optional[str]


class Match(BaseModel):
    id: int
    game: int
    team_one: int
    team_two: int
    tournament: Optional[int]
    date: str
    score: str
