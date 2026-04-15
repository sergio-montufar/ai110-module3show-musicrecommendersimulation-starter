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

    # Starter example profile
    user_prefs = {"genre": "hip-hop", "mood": "happy", "energy": 0.9}

    recommendations = recommend_songs(user_prefs, songs, k=5)

    print("\n" + "=" * 50)
    print("  🎵 Top Recommendations")
    print("=" * 50)

    for rank, (song, score, explanation) in enumerate(recommendations, 1):
        print(f"\n  #{rank}  {song['title']} by {song['artist']}")
        print(f"       Genre: {song['genre']} | Mood: {song['mood']} | Energy: {song['energy']}")
        print(f"       Score: {score:.2f} / 4.00")
        print(f"       Why:   {explanation}")
        print("  " + "-" * 46)


if __name__ == "__main__":
    main()
