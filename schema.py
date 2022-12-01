# PYTHON CORE
from datetime import datetime
from typing import Optional

# PACKAGES
from pydantic import BaseModel


# --- Models
class TopElementInfo(BaseModel):
    id: int
    points: int


class Event(BaseModel):
    id: int
    name: str
    deadline_time: datetime
    deadline_time_epoch: int
    finished: bool
    is_previous: bool
    is_current: bool
    is_next: bool
    top_element: Optional[int]
    most_captained: Optional[int]
    most_vice_captained: Optional[int]
    most_selected: Optional[int]
    most_transferred_in: Optional[int]
    highest_score: Optional[int]
    average_entry_score: Optional[int]


class Element(BaseModel):
    # Identify
    id: int
    code: int

    # Details
    first_name: str
    second_name: str
    web_name: str
    element_type: Optional[int]
    team: int
    team_code: int
    now_cost: int
    photo: str

    # Stats
    total_points: int
    form: float
    ep_this: float
    ep_next: float

    class Config:
        orm_mode = True


class ElementType(BaseModel):
    id: int
    element_count: int
    plural_name: str
    singular_name: str
    singular_name_short: str
    squad_select: int
    squad_min_play: int
    squad_max_play: int

    class Config:
        orm_mode = True


class Team(BaseModel):
    id: int
    code: int
    name: str
    short_name: str
    strength: int

    class Config:
        orm_mode = True


class FPL(BaseModel):
    elements: list[Element]
    teams: list[Team]
    element_types: list[ElementType]
    events: list[Event]


class History(BaseModel):
    element: int
    fixture: int
    opponent_team: int
    kickoff_time: datetime
    was_home: bool
    team_h_score: int
    team_a_score: int
    total_points: int
    minutes: int
    round: int
    goals_scored: int
    goals_conceded: int
    own_goals: int
    assists: int
    clean_sheets: int
    yellow_cards: int
    red_cards: int
    saves: int
    ict_index: float
    value: int
    bonus: int
    bps: int
    assists: int
    clean_sheets: int
    yellow_cards: int
    red_cards: int
    saves: int
    ict_index: float
    value: int
    bonus: int
    bps: int
    selected: int
    expected_goals: float
    expected_assists: float
    expected_goal_involvements: float
    expected_goals_conceded: float

    class Config:
        orm_mode = True


class HistoryPast(BaseModel):
    element_code: int
    season_name: str
    start_cost: int
    end_cost: int
    total_points: int
    minutes: int
    goals_scored: int
    goals_conceded: int
    own_goals: int
    assists: int
    clean_sheets: int
    yellow_cards: int
    red_cards: int
    saves: int
    influence: float
    creativity: float
    threat: float
    ict_index: float
    bonus: int
    bps: int
    expected_goals: float
    expected_assists: float
    expected_goal_involvements: float
    expected_goals_conceded: float

    class Config:
        orm_mode = True


class ElementSummary(BaseModel):
    history: list[History]
    history_past: list[HistoryPast]

    class Config:
        orm_mode = True


class Player(BaseModel):
    Element: Element
    Team: Team
    ElementType: ElementType
    ElementSummary: Optional[ElementSummary]

    class Config:
        orm_mode = True
