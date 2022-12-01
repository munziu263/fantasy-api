# Core

# Packages
from sqlalchemy import (
    Column,
    Integer,
    String,
    Float,
    ForeignKey,
    DateTime,
    Boolean,
)
from sqlalchemy.orm import relationship

# Modules
from db import Base


class Event(Base):
    __tablename__ = "event"

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    deadline_time = Column(DateTime, nullable=False)
    deadline_time_epoch = Column(Integer, nullable=False)
    finished = Column(Boolean, nullable=False)
    is_previous = Column(Boolean, nullable=False)
    is_current = Column(Boolean, nullable=False)
    is_next = Column(Boolean, nullable=False)
    top_element = Column(Integer)
    most_captained = Column(Integer)
    most_vice_captained = Column(Integer)
    most_selected = Column(Integer)
    most_transferred_in = Column(Integer)
    highest_score = Column(Integer)
    average_entry_score = Column(Integer)


class Team(Base):
    __tablename__ = "team"

    id = Column(Integer, primary_key=True)
    code = Column(Integer, nullable=False)
    name = Column(String(255), nullable=False)
    short_name = Column(String(255), nullable=False)
    strength = Column(Integer, nullable=False)

    players = relationship("Element", back_populates="team_name")


class Element(Base):
    __tablename__ = "element"

    # Identity
    id = Column(Integer, primary_key=True)
    code = Column(Integer, nullable=False)

    # Details
    first_name = Column(String(255), nullable=False)
    second_name = Column(String(255), nullable=False)
    web_name = Column(String(255), nullable=False)
    element_type = Column(Integer, ForeignKey("element_type.id"), nullable=False)
    team = Column(Integer, ForeignKey("team.id"), nullable=False)
    team_code = Column(Integer, nullable=False)
    now_cost = Column(Integer, nullable=False)
    photo = Column(String(255))

    team_name = relationship("Team", back_populates="players")
    position = relationship("ElementType", back_populates="players")

    # Stats
    total_points = Column(Integer, nullable=False)
    form = Column(Float)
    ep_this = Column(Float)
    ep_next = Column(Float)


class ElementType(Base):
    __tablename__ = "element_type"

    id = Column(Integer, primary_key=True)
    element_count = Column(Integer, nullable=False)
    plural_name = Column(String(255), nullable=False)
    singular_name = Column(String(255), nullable=False)
    singular_name_short = Column(String(255), nullable=False)
    squad_select = Column(Integer, nullable=False)
    squad_min_play = Column(Integer, nullable=False)
    squad_max_play = Column(Integer, nullable=False)

    players = relationship("Element", back_populates="position")
