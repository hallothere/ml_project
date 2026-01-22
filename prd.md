# Product Requirements Document (PRD) — Expedia Smart Search

## 1. Problem Statement
Expedia users are currently overwhelmed by an extensive inventory of hotel options, leading to "choice paralysis." Current search results rely on static filters that ignore complex user intent. This high cognitive load results in **search friction**, leading to dropped sessions and a lower **Conversion Rate (CR)**.

**The AI Opportunity:** By implementing a multi-class classification model, we predict the specific "Hotel Cluster" a user is most likely to book. Transitioning to a personalized ranking will shorten the path to purchase and increase booking efficiency.

## 2. User Persona: "The Efficient Traveler"
- **Context:** A traveler who knows their destination but is undecided on the specific property.
- **Pain Point:** Irrelevance (scrolling through family hotels on a business trip) and Time Loss (spending 15+ minutes comparing similar options).
- **Goal:** Find the "right" hotel cluster within the first 5 search results.

## 3. Scope & Technical Constraints
### In-Scope
- **Model:** Multi-class Decision Tree / Gradient Boosting Classifier.
- **Feature Engineering:** Deriving stay duration, seasonality, and distance buckets.
- **Offline Evaluation:** Validating against historical data before UI implementation.

### Out-of-Scope
- Real-time pricing optimization or dynamic discounting.
- UI/UX front-end redesign (focus is on the ranking logic).
- Inventory management (assuming availability for predicted clusters).

### Constraints & Assumptions
- **Data Sampling:** To manage computational load, we focus on **confirmed booking events (`is_booking = 1`)**, utilizing a high-signal subset of ~3M records.
- **Class Imbalance:** Certain clusters are disproportionately popular; the model must account for this to avoid "mass-market" bias.
- **Latency:** Predictions must be generated in milliseconds for live search integration.

## 4. Success Metrics (The Mapping)

| Metric Type | Metric Name | Purpose |
| :--- | :--- | :--- |
| **ML (Primary)** | **MAP@5** | **North Star.** Measures ranking quality. Rewards the model more if the booked hotel is at Rank #1 vs #5. |
| **ML (Secondary)** | **Top-5 Hit Rate** | Diagnostic. Was the booked hotel anywhere in our top 5 predicted clusters? |
| **Product (UX)** | **Mean Time to Book** | Goal: Reduce time spent from first search to confirmed booking. |
| **Business** | **Booking Conversion Rate** | The ultimate goal: Increase the % of users who complete a booking. |



## 5. Feature Engineering Strategy
To ensure consistent model performance and capture traveler intent, we implemented modular feature creation:
- **Stay Duration:** Categorized into "Short Stay" (≤ 3 nights) vs. "Long Stay" (> 3 nights).
- **Distance Buckets:** Near (≤300km), Mid (300-1000km), Far (1000-3000km), Very Far (>3000km).
- **Seasonality:** Extracted from `date_time` to capture peak holiday vs. off-season patterns.

## 6. Ethical, Risk & Failure Analysis
*This section addresses potential failure modes and ethical considerations as part of our risk mitigation strategy.*

| Risk / Failure Mode | Impact | Mitigation Strategy |
| :--- | :--- | :--- |
| **Popularity Bias** | Model only suggests top-tier clusters, ignoring niche needs. | Implement a fallback for niche searches or use "Diversity Re-ranking." |
| **Data Leakage** | Over-optimistic results due to "future" hotel info. | Strict feature audits; excluding hotel-side metadata during training. |
| **Seasonality Decay** | Performance drops as travel trends shift. | Monthly retraining triggers and seasonal feature weightings. |
| **User Trust Risk** | Irrelevant Top-1 recommendation. | Prioritize **MAP@5** to ensure variety in the visible Top-5 results. |



## 7. Model Experimentation & Decision Rationale
- **Baseline:** Most popular cluster by destination (Benchmarking).
- **Iteration 1:** Standard Decision Tree to establish baseline feature importance.
- **Iteration 2:** Hyperparameter tuning (max_depth, min_samples_leaf) to combat overfitting.
- **Alternative:** Evaluation of CatBoost/LightGBM for handling categorical features if Laptops allow (Hardware Constraint).

## 8. Post-Launch Plan & Iteration Roadmap
- **Immediate (V1.1):** Evaluate the impact of "Distance Buckets" vs. raw distance values on MAP@5.
- **Mid-term (V2):** Integrate `destinations.csv` features to capture deeper destination intent fingerprints.

## 9. Maintenance & Operational Strategy
- **Retraining Trigger:** Automatic retraining if MAP@5 drops below a 5% threshold over 7 days.
- **Rollback Strategy:** Instant revert to the "Most Popular Cluster" baseline if the Booking Conversion Rate drops significantly during A/B testing.
- **Data Monitoring:** Continuous monitoring of feature distributions to detect "Data Drift" (e.g., changes in travel behavior).