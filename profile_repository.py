import json
from pathlib import Path
from .models import Profile


def load_profile(path: str = "data/profile.json") -> Profile:
    file_path = Path(path)
    if not file_path.exists():
        raise FileNotFoundError(f"Profile file not found: {file_path}")

    with file_path.open(encoding="utf-8") as f:
        data = json.load(f)

    return Profile(
        name=data.get("name", ""),
        title=data.get("title", ""),
        tech_skills=[s.lower() for s in data.get("tech_skills", [])],
        soft_skills=[s.lower() for s in data.get("soft_skills", [])],
    )
