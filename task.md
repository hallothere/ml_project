# Project Task Board: Expedia Hotel Recommendations

## 1. Executive Summary: Story & Ticket Mapping
*Quick overview of all Epics and their associated Subtasks.*

* **[STORY-DATA] Data Foundation & Infrastructure**
    * [DATA-02] Initial Dataset Acquisition [DONE]
    * [DATA-01] Repository Structure & Data Protection [REVIEW]
    * [ENG-03] Reproducible Data Pipeline Script [REVIEW]
* **[STORY-STRATEGY] Strategic AI Product Framing**
    * [DOCS-01] Product Requirements Document (PRD.md) [REVIEW]
* **[STORY-EDA] Data Intelligence & Feature Engineering**
    * [ENG-01] Feature Engineering V1: Behavioral Buckets [IN PROGRESS]
    * [MODEL-01] Simple Baseline: Most Popular Cluster Ranking [DONE]
    * [EDA-01] Visual EDA & Target Leakage Audit [TO DO]
    * [RISK-01] Bias & Ethics Post-Mortem [TO DO]
* **[STORY-MODELS] Multi-Class Classification Engine**
    * [ENG-02] MAP@5 & Top-K Evaluation Engine [TO DO]
    * [MODEL-02] Baseline ML: Logistic Regression [TO DO]
    * [MODEL-03] Baseline ML: Decision Tree Classifier [TO DO]
    * [MODEL-04] High-Performance Model: Gradient Boosting [TO DO]
* **[STORY-PRESENTATION] Stakeholder Delivery & Storytelling**
    * [PRES-01] Data & Insight Synthesis [TO DO]
    * [PRES-02] Presentation Design & Business Storytelling [TO DO]
    * [PRES-03] Technical Dry Run [TO DO]
    * [PRES-04] Final Stakeholder Presentation [TO DO]

---

## 2. Detailed Story & Subtask Specifications

### [STORY-DATA] Data Foundation & Infrastructure
**Goal:** Establish a secure, reproducible, and manageable data environment for the team.

#### Ticket: [DATA-02] Initial Dataset Acquisition & Local Sync [STATUS: DONE]
* **Context:** The team needs access to the raw 37M row Expedia dataset.
* **Task:** Secure the data and set up local access.
* **Steps taken:** 1. Downloaded `train.csv` and `destinations.csv` from Kaggle.
* **Expected Result:** Data is accessible locally for all members.
* **Assignee:** Inbal

#### Ticket: [DATA-01] Repository Structure & Data Protection [STATUS: REVIEW]
* **Context:** A professional ML project needs a standardized folder structure that protects against accidental uploads of large datasets.
* **Task:** Initialize project directories and configure Git safety.
* **Steps taken:** 1. Created folder structure (`data/raw`, `data/processed`, `src/data`, `notebooks`).
    2. Implemented `.gitkeep` files to track empty data directories.
    3. Configured `.gitignore` with `data/**/*` to block large CSV files.
* **Expected Result:** A production-ready repository structure.
* **Assignee:** Daniela / Anita

#### Ticket: [ENG-03] Reproducible Data Pipeline Script [STATUS: REVIEW]
* **Context:** Raw 4GB data exceeds GitHub limits and local RAM. We need a standardized way to generate the 3M booking sample.
* **Task:** Implement `make_dataset.py` using pandas chunking.
* **Steps taken:** 1. Implemented chunk-based reading (500k rows/chunk).
    2. Added `is_booking == 1` filter logic.
    3. Integrated auto-directory creation.
* **Expected Result:** Identical 3,000,693-row CSV file via a single command.
* **Assignee:** Daniela

---

### [STORY-STRATEGY] Strategic AI Product Framing
**Goal:** Define the "North Star" of the project to ensure technical work aligns with business value.

#### Ticket: [DOCS-01] Product Requirements Document (PRD.md) [STATUS: REVIEW]
* **Context:** Need a strategic foundation.
* **Task:** Define the AI Product Framing.
* **Steps taken:** Documented User Persona, MAP@5 metric, and the 9-point PRD structure.
* **Expected Result:** A live document guiding all modeling decisions.
* **Assignee:** Daniela

---

### [STORY-EDA] Data Intelligence & Feature Engineering
**Goal:** Understand data distributions and transform raw logs into high-signal behavioral features.

#### Ticket: [ENG-01] Feature Engineering V1: Behavioral Buckets [STATUS: IN PROGRESS]
* **Context:** Raw dates and distances aren't "ML-ready."
* **Task:** Refine the `make_features()` function.
* **Implementation Steps:** 1. Create "Short vs Long" stay categories.
    2. Implement distance buckets (Near/Mid/Far/Very Far).
    3. Extract seasonal month/day-of-week signals.
* **Expected Result:** A centralized `src/features.py` module.
* **Assignee:** Inbal

#### Ticket: [MODEL-01] Simple Baseline: Most Popular Cluster Ranking [STATUS: DONE]
* **Context:** We need a "dumb" baseline to prove AI value.
* **Task:** Calculate the Top-5 most popular clusters per destination.
* **Expected Result:** A baseline MAP@5 score to beat.
* **Assignee:** Inbal

#### Ticket: [EDA-01] Visual EDA & Target Leakage Audit [STATUS: TO DO]
* **Context:** Ensuring features are valid and the model isn't "cheating."
* **Task:** Conduct visual analysis and feature validation.
* **Implementation Steps:**
    1. Audit features for "Search Context" vs "Post-Booking" data.
    2. Check for "Time-Travel" leakage in the training split.
    3. Visualize cluster distributions for class imbalance.
* **Expected Result:** 5-7 high-quality plots for the presentation.
* **Assignee:** Daniela

#### Ticket: [RISK-01] Bias & Ethics Post-Mortem [STATUS: TO DO]
* **Context:** AIPM requirement for ethical AI.
* **Task:** Analyze discrimination and popularity bias.
* **Implementation Steps:**
    1. Check for Popularity Bias in recommendations.
    2. Conduct Country-based fairness audit.
* **Expected Result:** A "Failure Mode" section in the documentation.
* **Assignee:** Daniela

---

### [STORY-MODELS] Multi-Class Classification Engine
**Goal:** Develop and evaluate models from simple statistical baselines to high-performance algorithms.

#### Ticket: [ENG-02] MAP@5 & Top-K Evaluation Engine [STATUS: TO DO]
* **Context:** Standard metrics don't support "Top-5 Ranking."
* **Task:** Write a custom evaluation script.
* **Expected Result:** Python function for MAP@5 and Top-5 Hit Rate.
* **Assignee:** *Unassigned*

#### Ticket: [MODEL-02] Baseline ML: Logistic Regression [STATUS: TO DO]
* **Context:** Establishing a statistical linear baseline.
* **Task:** Implement a Logistic Regression classifier.
* **Implementation Steps:** 1. Preprocess features (Scaling/Encoding).
    2. Train on the 3M booking sample.
* **Expected Result:** A statistical benchmark performance score.
* **Assignee:** *Unassigned*

#### Ticket: [MODEL-03] Baseline ML: Decision Tree Classifier [STATUS: TO DO]
* **Context:** The first "intelligent" tree-based model.
* **Task:** Implement and tune a standard Decision Tree.
* **Implementation Steps:** 1. Chronological split.
    2. Fit `DecisionTreeClassifier`.
* **Expected Result:** Performance metrics and feature importance rankings.
* **Assignee:** *Unassigned*

#### Ticket: [MODEL-04] High-Performance Model: Gradient Boosting [STATUS: TO DO]
* **Context:** Capturing complex, non-linear traveler patterns.
* **Task:** Implement XGBoost or LightGBM.
* **Implementation Steps:** 1. Handle categorical features. 2. Hyperparameter optimization.
* **Expected Result:** Highest MAP@5 score for the presentation.
* **Assignee:** Anita

---

### [STORY-PRESENTATION] Stakeholder Delivery & Storytelling
**Goal:** Synthesize technical results into a business-focused presentation.

#### Ticket: [PRES-01] Data & Insight Synthesis [STATUS: TO DO]
* **Context:** Consolidating team results.
* **Task:** Gathering performance metrics and feature insights.
* **Assignee:** *Unassigned*

#### Ticket: [PRES-02] Presentation Design & Business Storytelling [STATUS: TO DO]
* **Context:** Final pitch preparation.
* **Task:** Create the Dark-Theme slide deck.
* **Assignee:** *Unassigned*

#### Ticket: [PRES-03] Technical Dry Run [STATUS: TO DO]
* **Context:** Ensuring a smooth flow.
* **Task:** Perform a full rehearsal with the team.
* **Assignee:** Daniela

#### Ticket: [PRES-04] Final Stakeholder Presentation [STATUS: TO DO]
* **Context:** Final delivery.
* **Task:** Present results and handle Q&A.
* **Assignee:** *Unassigned*