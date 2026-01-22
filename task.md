### **Column: DONE (Completed Tasks)**

#### **Ticket: [DATA-01] Repository Structure & Data Protection**
**Description:**
* **Context:** A professional ML project needs a standardized folder structure that protects against accidental uploads of large datasets.
* **Task:** Initialize project directories and configure Git safety.
* **Steps taken:** 1. Created folder structure (`data/raw`, `data/processed`, `src/data`, `notebooks`).
    2. Implemented `.gitkeep` files to track empty data directories.
    3. Configured `.gitignore` with `data/**/*` to block large CSV files while allowing placeholder files.
**Expected Result:** A production-ready repository structure that is consistent for all team members.
**Assignee:** Daniela

#### **Ticket: [DOCS-01] Product Requirements Document (PRD.md) Finalization**
**Description:**
* **Context:** Need a strategic "North Star" for the project.
* **Task:** Define the AI Product Framing (Classification vs. Regression error fix).
* **Steps taken:** Documented User Persona, MAP@5 metric, and the 9-point PRD structure.
**Expected Result:** A live document that guides all modeling and business decisions.
**Assignee:** Daniela

#### **Ticket: [DATA-02] Initial Dataset Acquisition & Local Sync**
**Description:**
* **Context:** The team needs access to the raw 37M row Expedia dataset.
* **Task:** Secure the data and set up local access.
* **Steps taken:** 1. Downloaded `train.csv` and `destinations.csv` from Kaggle.
**Expected Result:** Data is accessible locally for all members.
**Assignee:** Inbal

#### **Ticket: [ENG-03] Reproducible Data Pipeline Script**
**Description:**
* **Context:** The raw 4GB dataset exceeds GitHub limits and local RAM capacities. We need a standardized way to generate our 3M-record booking sample locally.
* **Task:** Implement a data processing script (`make_dataset.py`) using pandas chunking.
* **Steps taken:** 1. Implemented chunk-based reading (500k rows/chunk).
    2. Added `is_booking == 1` filter logic.
    3. Integrated auto-directory creation for `data/processed/`.
**Expected Result:** Every team member generates an identical 3,000,693-row CSV file via a single terminal command.
**Assignee:** Daniela

#### **Ticket: [MODEL-01] Simple Baseline: Most Popular Cluster Ranking**
**Description:**
* **Context:** We need a "dumb" baseline to prove that AI actually adds value.
* **Task:** Calculate the Top-5 most popular clusters per destination.
* **Expected Result:** A baseline MAP@5 score to beat with ML.
**Assignee:** Nils

---

### **Column: IN PROGRESS**

#### **Ticket: [ENG-01] Feature Engineering V1: Behavioral Buckets**
**Description:**
* **Context:** Raw dates and distances aren't "ML-ready."
* **Task:** Refine the `make_features()` function.
* **Steps to implement:** 1. Create "Short vs Long" stay categories (Inbal's logic).
    2. Implement distance buckets (Near/Mid/Far/Very Far).
    3. Extract seasonal month/day-of-week signals.
**Expected Result:** A centralized `src/features.py` module used by all notebooks.
**Assignee:** Inbal

---

### **Column: TO DO (Pending Tasks)**

#### **Ticket: [EDA-01] Visual EDA & Target Leakage Audit**
**Description:**
* **Context:** Ensuring our features are valid and the model isn't "cheating" by using future information.
* **Task:** Conduct a visual analysis and feature validation.
* **Implementation Steps:**
    1. Audit features for "Search Context" vs "Post-Booking" data.
    2. Check for "Time-Travel" leakage in the training split.
    3. Visualize cluster distributions to identify class imbalance.
**Expected Result:** A leakage-free feature set and 5-7 high-quality plots for the presentation.
**Assignee:** Daniela

#### **Ticket: [MODEL-02] Baseline ML: Decision Tree Classifier**
**Description:**
* **Context:** The first "intelligent" model to test our features.
* **Task:** Implement and tune a standard Decision Tree.
* **Implementation Steps:**
    1. Chronological split (Training on past, testing on "future").
    2. Fit `DecisionTreeClassifier`.
    3. Evaluate using the MAP@5 engine.
**Expected Result:** Baseline ML performance metrics and feature importance rankings.
**Assignee:** *Unassigned*

#### **Ticket: [MODEL-03] High-Performance Model: Gradient Boosting (XGBoost/LightGBM)**
**Description:**
* **Context:** Capturing complex, non-linear traveler patterns.
* **Task:** Implement a Gradient Boosting model (Anita's focus).
* **Implementation Steps:** 1. Handle categorical features (LabelEncoding or native CatBoost).
    2. Hyperparameter optimization (Depth, Learning Rate).
**Expected Result:** A model achieving the highest MAP@5 score for the presentation.
**Assignee:** Anita

#### **Ticket: [ENG-02] MAP@5 & Top-K Evaluation Engine**
**Description:**
* **Context:** Standard Scikit-Learn metrics don't support "Top-5 Ranking."
* **Task:** Write a custom evaluation script.
* **Expected Result:** A Python function that outputs MAP@5 and Top-5 Hit Rate.
**Assignee:** *Unassigned*

#### **Ticket: [DOCS-02] Final Presentation & Business Storytelling**
**Description:**
* **Context:** Final pitch on Monday.
* **Task:** Create the Dark-Theme slide deck.
* **Goal:** Connect ML results back to "The Efficient Traveler" persona.
**Expected Result:** A professional presentation ready for the stakeholders.
**Assignee:** *Unassigned*

#### **Ticket: [RISK-01] Bias & Ethics Post-Mortem**
**Description:**
* **Context:** AIPM requirement for ethical AI.
* **Task:** Analyze if the model discriminates or suffers from extreme popularity bias.
**Expected Result:** A "Failure Mode" section in the final documentation.
**Assignee:** *Unassigned*