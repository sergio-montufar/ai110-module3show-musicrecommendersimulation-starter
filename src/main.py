"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from src.recommender import load_songs, recommend_songs


def main() -> None:
    songs = load_songs("data/songs.csv")
    print(f"Loaded songs: {len(songs)}")

    test_profiles = [
        {"name": "Contradictory",    "genre": "lofi",      "mood": "chill",      "energy": 0.95},
        {"name": "Nothing Matches",  "genre": "reggaeton", "mood": "angry",      "energy": 0.50},
        {"name": "Nearly Identical", "genre": "pop",       "mood": "happy",      "energy": 0.79},
        {"name": "Extreme Boundary", "genre": "ambient",   "mood": "chill",      "energy": 0.0},
        {"name": "Loyalty vs Vibes", "genre": "metal",     "mood": "aggressive", "energy": 0.30},
    ]

    for profile in test_profiles:
        label = profile.pop("name")
        user_prefs = profile

        recommendations = recommend_songs(user_prefs, songs, k=5)

        print("\n" + "=" * 50)
        print(f"  🎵 Test: {label}")
        print(f"  Profile: genre={user_prefs['genre']}, mood={user_prefs['mood']}, energy={user_prefs['energy']}")
        print("=" * 50)

        for rank, (song, score, explanation) in enumerate(recommendations, 1):
            print(f"\n  #{rank}  {song['title']} by {song['artist']}")
            print(f"       Genre: {song['genre']} | Mood: {song['mood']} | Energy: {song['energy']}")
            print(f"       Score: {score:.2f} / 4.00")
            print(f"       Why:   {explanation}")
            print("  " + "-" * 46)


if __name__ == "__main__":
    main()
