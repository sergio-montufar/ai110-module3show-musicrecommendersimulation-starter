# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

**TuneMatch 1.0**

---

## 2. Intended Use  

Describe what your recommender is designed to do and who it is for. 

Prompts:  

- What kind of recommendations does it generate  
- What assumptions does it make about the user  
- Is this for real users or classroom exploration  

TuneMatch suggests 5 songs from a small catalog based on a user's preferred genre, mood, and energy level. It assumes the user knows their preferences upfront and can express them as a simple profile. This system is built for classroom exploration only — it is not designed for real users or production use.

---

## 3. How the Model Works  

Explain your scoring approach in simple language.  

Prompts:  

- What features of each song are used (genre, energy, mood, etc.)  
- What user preferences are considered  
- How does the model turn those into a score  
- What changes did you make from the starter logic  

Avoid code here. Pretend you are explaining the idea to a friend who does not program.

The system looks at three things about each song: its genre, its mood, and its energy level. It compares each one against what the user says they prefer. A genre match is worth the most points (+2.0) because genre is the strongest indicator of taste. A mood match adds a smaller bonus (+1.0). For energy, instead of a yes-or-no check, the system measures how close the song's energy is to what the user wants — the closer it is, the more points it earns (up to +1.0). All three scores are added together, every song in the catalog gets ranked by its total, and the top 5 are returned as recommendations.

---

## 4. Data  

Describe the dataset the model uses.  

Prompts:  

- How many songs are in the catalog  
- What genres or moods are represented  
- Did you add or remove data  
- Are there parts of musical taste missing in the dataset  

The catalog contains 20 songs spanning 14 genres (pop, lofi, rock, ambient, jazz, synthwave, indie pop, metal, classical, hip-hop, r&b, country, electronic, folk, funk, reggae, darkwave) and 15 moods. We expanded the original 10-song starter set by adding 10 new songs to increase genre and mood diversity. The dataset is still small and reflects one curator's taste — it lacks non-English music, has no songs longer than a few genres deep, and several genres are represented by only a single track.

---

## 5. Strengths  

Where does your system seem to work well  

Prompts:  

- User types for which it gives reasonable results  
- Any patterns you think your scoring captures correctly  
- Cases where the recommendations matched your intuition  

The system works well for users whose preferred genre has multiple songs in the catalog, such as lofi or pop listeners. In those cases, genre narrows the field and energy similarity provides meaningful differentiation between the remaining candidates. The scoring logic is also fully transparent — every recommendation comes with a plain-language explanation of exactly which features matched and how many points each contributed, making it easy to understand and trust the output.

---

## 6. Limitations and Bias 

Where the system struggles or behaves unfairly. 

Prompts:  

- Features it does not consider  
- Genres or moods that are underrepresented  
- Cases where the system overfits to one preference  
- Ways the scoring might unintentionally favor some users 


The system creates an inescapable filter bubble for users of single-song genres like metal, classical, or hip-hop. Since only one song exists in each of those categories, the same track is guaranteed to be the #1 recommendation every time regardless of other preferences. During the sensitivity test where mood scoring was removed, two users with identical genre and energy preferences but opposite moods (one wanting "chill" and the other wanting "focused") received exactly the same recommendations, revealing that the system can collapse meaningfully different listeners into a single profile. Additionally, the energy scoring structurally favors users with mid-range preferences (around 0.5) because the catalog contains songs across that range, while users at the extremes (very low or very high energy) face a narrower pool where even the "best match" scores poorly. This means the system doesn't fail equally for everyone, but instead it works best for users whose taste happens to align with the center of the dataset, which is itself a form of bias.

---

## 7. Evaluation  

How you checked whether the recommender behaved as expected. 

Prompts:  

- Which user profiles you tested  
- What you looked for in the recommendations  
- What surprised you  
- Any simple tests or comparisons you ran  

No need for numeric metrics unless you created some.

We tested five adversarial profiles: **Contradictory** (lofi + high energy), **Nothing Matches** (reggaeton, angry), **Nearly Identical** (pop vs indie pop), **Extreme Boundary** (energy: 0.0), and **Loyalty vs Vibes** (metal + low energy). The biggest surprise was the Nothing Matches profile — with no genre or mood hits in the catalog, the entire ranking collapsed to energy similarity alone, and the system still confidently returned five songs with no real connection to the user's taste. The Nearly Identical test was also revealing: Rooftop Lights (indie pop, happy) scored 2.0 points lower than Sunrise City (pop, happy) despite being a near-perfect vibe match, purely because "indie pop" != "pop" in an exact-match check.

---

## 8. Future Work  

Ideas for how you would improve the model next.  

Prompts:  

- Additional features or preferences  
- Better ways to explain recommendations  
- Improving diversity among the top results  
- Handling more complex user tastes  

1. **Fuzzy genre matching** — Treat related genres (like "pop" and "indie pop") as partial matches instead of all-or-nothing, so users discover songs just outside their stated preference.
2. **Diversity constraint** — Instead of returning the top 5 by score alone, ensure the results include at least 2 different genres or moods so the recommendations don't all sound the same.
3. **Multi-preference profiles** — Allow users to specify more than one favorite genre or mood, reflecting how most people actually listen to music across different contexts and activities.

---

## 9. Personal Reflection  

A few sentences about your experience.  

Prompts:  

- What you learned about recommender systems  
- Something unexpected or interesting you discovered  
- How this changed the way you think about music recommendation apps  

Building this system showed me that recommendation isn't just a math problem. The design choices behind the scoring (what gets points, how much, and what gets ignored) encode assumptions about what "good taste" looks like. The most surprising moment was seeing the system confidently recommend five songs to a reggaeton listener when it had zero reggaeton in the catalog; it didn't fail gracefully, it just pretended everything was fine. That made me think differently about apps like Spotify: when a recommendation feels off, it might not be a bug, but a bias baked into how the system was designed or what data it was trained on.
