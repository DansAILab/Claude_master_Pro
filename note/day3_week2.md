## Day 3 — Debugging buggy_sum.py

The function wasn't outputting the correct sum because the loop never reached the last number — `range(1, n)` always stops one *before* its second value, so with n=5 the loop only went through 1, 2, 3, 4, skipping 5 entirely.

At first I thought the fix was just changing the call to sum_of_first_n(6), but that doesn't actually fix the function — it just works around one specific case. The real fix was changing range(1, n) to range(1, n + 1) inside the function itself: adding 1 to the stop value pushes the cutoff one step further out, so n itself gets correctly included, no matter what number n actually is.

The 5-step detective method

1. Reproduce — run the bug again to confirm it happens consistently, not just once by chance.
2. Isolate — add debug prints (or similar) inside the code to see exactly what's happening at each step, narrowing down where things go wrong.
3. Hypothesize — based on what you observed, write down what you think is actually causing the problem.
4. Test the guess — fix one thing at a time and rerun, checking whether that specific fix actually helps.
5. Fix and verify — once everything's correct, remove any debug prints and run it one final time to confirm the real fix holds.