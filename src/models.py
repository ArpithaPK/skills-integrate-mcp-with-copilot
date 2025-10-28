from sqlalchemy import (
    create_engine,
    Column,
    Integer,
    String,
    Text,
    Table,
    ForeignKey,
)
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
from pathlib import Path
import os

Base = declarative_base()

# Use DATABASE_URL env var if provided, otherwise a local sqlite file next to this module
db_file = Path(__file__).parent / "app.db"
DATABASE_URL = os.environ.get("DATABASE_URL", f"sqlite:///{db_file}")

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False} if DATABASE_URL.startswith("sqlite") else {},
)
SessionLocal = sessionmaker(bind=engine)

# Association table for many-to-many relationship between activities and participants
registrations = Table(
    "registrations",
    Base.metadata,
    Column("activity_name", String, ForeignKey("activities.name"), primary_key=True),
    Column("participant_email", String, ForeignKey("participants.email"), primary_key=True),
)


class Activity(Base):
    __tablename__ = "activities"
    name = Column(String, primary_key=True, index=True)
    description = Column(Text)
    schedule = Column(String)
    max_participants = Column(Integer)
    participants = relationship("Participant", secondary=registrations, back_populates="activities")


class Participant(Base):
    __tablename__ = "participants"
    email = Column(String, primary_key=True, index=True)
    activities = relationship("Activity", secondary=registrations, back_populates="participants")


def init_db(seed_activities: dict | None = None):
    """Create tables and optionally seed activities if none exist."""
    Base.metadata.create_all(bind=engine)
    if not seed_activities:
        return
    session = SessionLocal()
    try:
        existing = session.query(Activity).count()
        if existing == 0:
            for name, data in seed_activities.items():
                act = Activity(
                    name=name,
                    description=data.get("description"),
                    schedule=data.get("schedule"),
                    max_participants=data.get("max_participants"),
                )
                session.add(act)
                # ensure participants exist and associate them
                for email in data.get("participants", []):
                    p = session.get(Participant, email)
                    if not p:
                        p = Participant(email=email)
                        session.add(p)
                    act.participants.append(p)
            session.commit()
    finally:
        session.close()
