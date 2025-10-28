"""
High School Management System API

A super simple FastAPI application that allows students to view and sign up
for extracurricular activities at Mergington High School.
"""

from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse
import os
from pathlib import Path

app = FastAPI(title="Mergington High School API",
              description="API for viewing and signing up for extracurricular activities")

# Mount the static files directory
current_dir = Path(__file__).parent
app.mount("/static", StaticFiles(directory=os.path.join(Path(__file__).parent,
          "static")), name="static")

# In-memory activity database
activities = {
    "Chess Club": {
        "description": "Learn strategies and compete in chess tournaments",
        "schedule": "Fridays, 3:30 PM - 5:00 PM",
        "max_participants": 12,
        "participants": ["michael@mergington.edu", "daniel@mergington.edu"]
    },
    "Programming Class": {
        "description": "Learn programming fundamentals and build software projects",
        "schedule": "Tuesdays and Thursdays, 3:30 PM - 4:30 PM",
        "max_participants": 20,
        "participants": ["emma@mergington.edu", "sophia@mergington.edu"]
    },
    "Gym Class": {
        "description": "Physical education and sports activities",
        "schedule": "Mondays, Wednesdays, Fridays, 2:00 PM - 3:00 PM",
        "max_participants": 30,
        "participants": ["john@mergington.edu", "olivia@mergington.edu"]
    },
    "Soccer Team": {
        "description": "Join the school soccer team and compete in matches",
        "schedule": "Tuesdays and Thursdays, 4:00 PM - 5:30 PM",
        "max_participants": 22,
        "participants": ["liam@mergington.edu", "noah@mergington.edu"]
    },
    "Basketball Team": {
        "description": "Practice and play basketball with the school team",
        "schedule": "Wednesdays and Fridays, 3:30 PM - 5:00 PM",
        "max_participants": 15,
        from fastapi import FastAPI, HTTPException, Depends
        from fastapi.staticfiles import StaticFiles
        from fastapi.responses import RedirectResponse
        from pathlib import Path
        from typing import Dict, Any

        from . import models

        app = FastAPI(title="Mergington High School API",
                      description="API for viewing and signing up for extracurricular activities")

        # Mount the static files directory
        current_dir = Path(__file__).parent
        app.mount("/static", StaticFiles(directory=current_dir / "static"), name="static")

        # Original in-memory activities used to seed the database on first run
        _seed_activities = {
            "Chess Club": {
                "description": "Learn strategies and compete in chess tournaments",
                "schedule": "Fridays, 3:30 PM - 5:00 PM",
                "max_participants": 12,
                "participants": ["michael@mergington.edu", "daniel@mergington.edu"]
            },
            "Programming Class": {
                "description": "Learn programming fundamentals and build software projects",
                "schedule": "Tuesdays and Thursdays, 3:30 PM - 4:30 PM",
                "max_participants": 20,
                "participants": ["emma@mergington.edu", "sophia@mergington.edu"]
            },
            "Gym Class": {
                "description": "Physical education and sports activities",
                "schedule": "Mondays, Wednesdays, Fridays, 2:00 PM - 3:00 PM",
                "max_participants": 30,
                "participants": ["john@mergington.edu", "olivia@mergington.edu"]
            },
            "Soccer Team": {
                "description": "Join the school soccer team and compete in matches",
                "schedule": "Tuesdays and Thursdays, 4:00 PM - 5:30 PM",
                "max_participants": 22,
                "participants": ["liam@mergington.edu", "noah@mergington.edu"]
            },
            "Basketball Team": {
                "description": "Practice and play basketball with the school team",
                "schedule": "Wednesdays and Fridays, 3:30 PM - 5:00 PM",
                "max_participants": 15,
                "participants": ["ava@mergington.edu", "mia@mergington.edu"]
            },
            "Art Club": {
                "description": "Explore your creativity through painting and drawing",
                "schedule": "Thursdays, 3:30 PM - 5:00 PM",
                "max_participants": 15,
                "participants": ["amelia@mergington.edu", "harper@mergington.edu"]
            },
            "Drama Club": {
                "description": "Act, direct, and produce plays and performances",
                "schedule": "Mondays and Wednesdays, 4:00 PM - 5:30 PM",
                "max_participants": 20,
                "participants": ["ella@mergington.edu", "scarlett@mergington.edu"]
            },
            "Math Club": {
                "description": "Solve challenging problems and participate in math competitions",
                "schedule": "Tuesdays, 3:30 PM - 4:30 PM",
                "max_participants": 10,
                "participants": ["james@mergington.edu", "benjamin@mergington.edu"]
            },
            "Debate Team": {
                "description": "Develop public speaking and argumentation skills",
                "schedule": "Fridays, 4:00 PM - 5:30 PM",
                "max_participants": 12,
                "participants": ["charlotte@mergington.edu", "henry@mergington.edu"]
            """
            High School Management System API

            A super simple FastAPI application that allows students to view and sign up
            for extracurricular activities at Mergington High School.
            """

            from fastapi import FastAPI, HTTPException, Depends
            from fastapi.staticfiles import StaticFiles
            from fastapi.responses import RedirectResponse
            from pathlib import Path
            from typing import Dict, Any

            from . import models

            app = FastAPI(title="Mergington High School API",
                          description="API for viewing and signing up for extracurricular activities")

            # Mount the static files directory
            current_dir = Path(__file__).parent
            app.mount("/static", StaticFiles(directory=current_dir / "static"), name="static")

            # Original in-memory activities used to seed the database on first run
            _seed_activities = {
                "Chess Club": {
                    "description": "Learn strategies and compete in chess tournaments",
                    "schedule": "Fridays, 3:30 PM - 5:00 PM",
                    "max_participants": 12,
                    "participants": ["michael@mergington.edu", "daniel@mergington.edu"]
                },
                "Programming Class": {
                    "description": "Learn programming fundamentals and build software projects",
                    "schedule": "Tuesdays and Thursdays, 3:30 PM - 4:30 PM",
                    "max_participants": 20,
                    "participants": ["emma@mergington.edu", "sophia@mergington.edu"]
                },
                "Gym Class": {
                    "description": "Physical education and sports activities",
                    "schedule": "Mondays, Wednesdays, Fridays, 2:00 PM - 3:00 PM",
                    "max_participants": 30,
                    "participants": ["john@mergington.edu", "olivia@mergington.edu"]
                },
                "Soccer Team": {
                    "description": "Join the school soccer team and compete in matches",
                    "schedule": "Tuesdays and Thursdays, 4:00 PM - 5:30 PM",
                    "max_participants": 22,
                    "participants": ["liam@mergington.edu", "noah@mergington.edu"]
                },
                "Basketball Team": {
                    "description": "Practice and play basketball with the school team",
                    "schedule": "Wednesdays and Fridays, 3:30 PM - 5:00 PM",
                    "max_participants": 15,
                    "participants": ["ava@mergington.edu", "mia@mergington.edu"]
                },
                "Art Club": {
                    "description": "Explore your creativity through painting and drawing",
                    "schedule": "Thursdays, 3:30 PM - 5:00 PM",
                    "max_participants": 15,
                    "participants": ["amelia@mergington.edu", "harper@mergington.edu"]
                },
                "Drama Club": {
                    "description": "Act, direct, and produce plays and performances",
                    "schedule": "Mondays and Wednesdays, 4:00 PM - 5:30 PM",
                    "max_participants": 20,
                    "participants": ["ella@mergington.edu", "scarlett@mergington.edu"]
                },
                "Math Club": {
                    "description": "Solve challenging problems and participate in math competitions",
                    "schedule": "Tuesdays, 3:30 PM - 4:30 PM",
                    "max_participants": 10,
                    "participants": ["james@mergington.edu", "benjamin@mergington.edu"]
                },
                "Debate Team": {
                    "description": "Develop public speaking and argumentation skills",
                    "schedule": "Fridays, 4:00 PM - 5:30 PM",
                    "max_participants": 12,
                    "participants": ["charlotte@mergington.edu", "henry@mergington.edu"]
                }
            }


            @app.on_event("startup")
            def startup():
                # Create tables and seed activities on first run
                models.init_db(seed_activities=_seed_activities)


            def get_db():
                db = models.SessionLocal()
                try:
                    yield db
                finally:
                    db.close()


            @app.get("/")
            def root():
                return RedirectResponse(url="/static/index.html")


            @app.get("/activities")
            def get_activities(db=Depends(get_db)):
                """Return all activities and their details."""
                activities = db.query(models.Activity).all()
                result: Dict[str, Any] = {}
                for a in activities:
                    result[a.name] = {
                        "description": a.description,
                        "schedule": a.schedule,
                        "max_participants": a.max_participants,
                        "participants": [p.email for p in a.participants],
                    }
                return result


            @app.post("/activities/{activity_name}/signup")
            def signup_for_activity(activity_name: str, email: str, db=Depends(get_db)):
                """Sign up a student for an activity (persists to DB)."""
                activity = db.get(models.Activity, activity_name)
                if not activity:
                    raise HTTPException(status_code=404, detail="Activity not found")

                if any(p.email == email for p in activity.participants):
                    raise HTTPException(status_code=400, detail="Student is already signed up")

                if activity.max_participants is not None and len(activity.participants) >= (activity.max_participants or 0):
                    raise HTTPException(status_code=400, detail="Activity is full")

                participant = db.get(models.Participant, email)
                if not participant:
                    participant = models.Participant(email=email)
                    db.add(participant)

                activity.participants.append(participant)
                db.add(activity)
                db.commit()
                return {"message": f"Signed up {email} for {activity_name}"}


            @app.delete("/activities/{activity_name}/unregister")
            def unregister_from_activity(activity_name: str, email: str, db=Depends(get_db)):
                """Unregister a student from an activity (persists to DB)."""
                activity = db.get(models.Activity, activity_name)
                if not activity:
                    raise HTTPException(status_code=404, detail="Activity not found")

                participant = db.get(models.Participant, email)
                if not participant or all(p.email != email for p in activity.participants):
                    raise HTTPException(status_code=400, detail="Student is not signed up for this activity")

                # remove association
                activity.participants = [p for p in activity.participants if p.email != email]
                db.add(activity)
                db.commit()
                return {"message": f"Unregistered {email} from {activity_name}"}
