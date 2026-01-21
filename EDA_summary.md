# EDA Summary — Expedia Hotel Recommendations (Booking-Focused)

## Objective
Support the design of a hotel cluster ranking model aligned with booking outcomes and evaluated using Mean Average Precision @ 5 (MAP@5).

---

## Data Scope
- Random subsample of **500,000 search events** drawn from the full `train.csv`
- Filtered to **41,211 booking events** (`is_booking = 1`)
- All **100 hotel clusters** remain represented

---

## Key Findings

### 1. Target Structure & Feasibility
- Booking events exhibit a **long-tailed class distribution**
- A small number of hotel clusters dominate booking volume
- All clusters are still represented, supporting multi-class ranking
- The structure aligns well with **ranking-based evaluation (MAP@5)**

---

### 2. Geographic Signal
- Booking demand is highly concentrated in a small number of countries
- Preferred hotel clusters vary by user geography
- Geography primarily affects **ranking order**, not cluster presence  
**→ Strong primary signal**

---

### 3. Party Size & Family Context
- Bookings are dominated by solo travelers and couples
- ~19% of bookings involve children
- Family vs non-family bookings show **ranking shifts**, not completely distinct clusters  
**→ Meaningful contextual signal**

---

### 4. Temporal Signal
- Clear seasonality with peak demand in summer months
- Most stays are short (1–3 nights)
- Longer stays exhibit **distinct hotel cluster preferences**  
**→ Length of stay influences ranking**

---

### 5. Distance Signal
- Distance spans from local to long-haul travel with a long-tailed distribution
- ~34% of bookings have missing distance values
- Missing distance is **informative** and associated with different cluster rankings  
**→ Use distance buckets + missing indicator**

---

### 6. Device & Commercial Context
- Device type (mobile vs desktop) shows limited differentiation
- **Package bookings** exhibit clearly different cluster preferences  
**→ Package context is a strong signal; device is secondary**

---

## EDA-Backed Feature Recommendations

### Strong keep
- User geography (country / region)
- Destination identifiers
- Party size & child presence
- Length of stay & check-in month
- Distance buckets + distance-missing flag
- Package indicator

### Secondary / cautious
- Device type
- Marketing channel
- City-level identifiers
- Hotel attributes (potential exposure bias)

### Exclude
- `user_id`
- `is_booking`
- Target-derived fields

---

## Conclusion
Booking-focused EDA confirms that hotel cluster choice is driven by contextual factors that influence **ranking**, not single outcomes. A probabilistic, ranking-based modeling approach evaluated using MAP@5 is appropriate.
