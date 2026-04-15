from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass

@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float

@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool

class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        # TODO: Implement recommendation logic
        return self.songs[:k]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        # TODO: Implement explanation logic
        return "Explanation placeholder"

def load_songs(csv_path: str) -> List[Dict]:
    """Reads a CSV file and returns a list of song dictionaries with numeric fields converted."""
    import csv

    numeric_fields = {"id": int, "energy": float, "tempo_bpm": float,
                      "valence": float, "danceability": float, "acousticness": float}
    songs = []
    with open(csv_path, newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            for field, convert in numeric_fields.items():
                row[field] = convert(row[field])
            songs.append(row)
    return songs

def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, str]:
    """Scores a single song against user preferences and returns (score, explanation)."""
    score = 0.0
    reasons = []

    # Genre match: +2.0
    if song["genre"] == user_prefs["genre"]:
        score += 2.0
        reasons.append(f"genre match ({song['genre']}) (+2.0)")

    # Mood match: +1.0 (disabled for sensitivity test)
    # if song["mood"] == user_prefs["mood"]:
    #     score += 1.0
    #     reasons.append(f"mood match ({song['mood']}) (+1.0)")

    # Energy similarity: 0.0 to +1.0
    energy_score = 1.0 - abs(song["energy"] - user_prefs["energy"])
    score += energy_score
    reasons.append(f"energy similarity (+{energy_score:.2f})")

    explanation = "; ".join(reasons) if reasons else "no strong match"
    return score, explanation


def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """Scores all songs, sorts by score descending, and returns the top k results."""
    scored = [(song, *score_song(user_prefs, song)) for song in songs]
    scored.sort(key=lambda x: x[1], reverse=True)
    return scored[:k]
