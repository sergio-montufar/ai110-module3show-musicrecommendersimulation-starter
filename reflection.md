# Reflection

## Comparing Profile Outputs

The Contradictory profile (lofi, chill, energy: 0.95) and the Loyalty vs Vibes profile (metal, aggressive, energy: 0.30) both expose the same underlying behavior from opposite directions. The lofi user gets calm songs despite wanting high energy, and the metal user gets an intense song despite wanting low energy — in both cases, genre's +2.0 bonus drowns out the energy signal. This makes sense because the scoring math guarantees it: the maximum energy score (+1.0) can never overcome a genre match (+2.0), so the system always prioritizes what you say you like over how you want it to feel.

The Nothing Matches profile (reggaeton, angry) and the Nearly Identical profile (pop, happy) reveal different failure modes. The reggaeton user gets results ranked purely by energy because genre and mood contribute zero points — the system has no way to say "I don't have anything for you." The pop user gets Sunrise City ranked far above Rooftop Lights even though both songs sound similar to a human ear. One profile fails because nothing matches; the other fails because the system's definition of "match" is too rigid. Both point to the same root cause: exact string matching can't capture how music actually relates.
