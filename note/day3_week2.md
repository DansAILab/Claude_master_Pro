## Day 3 — Debugging buggy_sum.py

The function wasn't outputting the correct sum because the loop never reached the last number — `range(1, n)` always stops one *before* its second value, so with n=5 the loop only went through 1, 2, 3, 4, skipping 5 entirely.

At first I thought the fix was just changing the call to sum_of_first_n(6), but that doesn't actually fix the function — it just works around one specific case. The real fix was changing range(1, n) to range(1, n + 1) inside the function itself: adding 1 to the stop value pushes the cutoff one step further out, so n itself gets correctly included, no matter what number n actually is.
