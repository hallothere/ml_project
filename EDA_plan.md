## Phase 2 (next, local only)
* Create larger raw sample (300k–500k)
* Filter to bookings
* EDA focused on top-k stability

## Phase 3 (group decision)
* Baseline: top-5 frequent clusters
* First model: probabilistic classifier
* Output: ranked top-5 clusters

## Phase 4 (evaluation)
* MAP@5 on validation split
* Compare against baseline

## Bottom line (very important)
**MAP@5:**
* confirms booking-only focus
* reframes success as ranking, not guessing
* lowers pressure on exact accuracy
* raises importance of product realism
