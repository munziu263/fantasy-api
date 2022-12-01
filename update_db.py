# Packages
from requests import get, Response
from pydantic import BaseModel

# Modules
from db import SessionLocal, Base
from schema import FPL
import schema
import models

# --- Constants
ROOT_URL = "https://fantasy.premierleague.com/api/bootstrap-static/"
PLAYER_URL = (
    lambda element_id: f"https://fantasy.premierleague.com/api/element-summary/{element_id}/"
)

db = SessionLocal()


# --- Get data
def get_root_data():
    response: Response = get(ROOT_URL)
    fpl_data = FPL(**response.json())
    return fpl_data


def get_player_summary(player_id: int):
    response: Response = get(PLAYER_URL(player_id))
    player_data = schema.ElementSummary(**response.json())
    return player_data


def to_model(model: Base, objects: list[BaseModel]) -> list[Base]:
    return [model(**obj.dict()) for obj in objects]


def to_mappings(objects: list[BaseModel]) -> list[dict]:
    return [obj.dict() for obj in objects]


def update_table(model: Base, objects: list[BaseModel]) -> None:
    mappings = to_mappings(objects)
    db.bulk_update_mappings(model, mappings)
    db.commit()


def load_table(model: Base, data: list[BaseModel]):
    objects = [model(**obj.dict()) for obj in data]
    db.add_all(objects)
    db.commit()


def main():
    fpl = get_root_data()

    groups: dict = {
        models.Element: fpl.elements,
        models.ElementType: fpl.element_types,
        models.Event: fpl.events,
        models.Team: fpl.teams,
    }

    for model, objects in groups.items():
        if db.query(model).count():
            update_table(model, objects)
        else:
            load_table(model, objects)


if __name__ == "__main__":
    main()
