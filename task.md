### **Column: DONE (Completed Tasks)**

#### **Ticket: [DATA-01] Initial Dataset Acquisition & Local Sync**
**Description:**
* **Context:** The team needs access to the raw 37M row Expedia dataset.
* **Task:** Secure the data and set up safety guardrails for GitHub.
* **Steps taken:** 1. Downloaded `train.csv` and `destinations.csv` from Kaggle.
    2. Configured `.gitignore` to prevent multi-GB files from being pushed to the remote.
**Expected Result:** Data is accessible locally for all members; Repo remains lightweight.
**Assignee:** Inbal

#### **Ticket: [DATA-02] Technical Sampling (3M Booking Subset)**
**Description:**
* **Context:** Full dataset processing is too memory-intensive for local laptops.
* **Task:** Extract high-value signals (confirmed bookings).
* **Steps taken:** Filtered raw data where `is_booking = 1`, resulting in a stable 3,000,693 record CSV.
**Expected Result:** A manageable training set that retains the core "conversion" signal.
**Assignee:** Nils

#### **Ticket: [DOCS-01] Product Requirements Document (PRD.md) Finalization**
**Description:**
* **Context:** Need a strategic "North Star" for the project.
* **Task:** Define the AI Product Framing (Classification vs. Regression error fix).
* **Steps taken:** Documented User Persona, MAP@5 metric, and the 9-point PRD structure.
**Expected Result:** A live document that guides all modeling and business decisions.
**Assignee:** Daniela

#### **Ticket: [MODEL-01] Simple Baseline: Most Popular Cluster Ranking**
**Description:**
* **Context:** We need a "dumb" baseline to prove that AI actually adds value.
* **Task:** Calculate the Top-5 most popular clusters per destination.
* **Expected Result:** A baseline MAP@5 score to beat with ML.
**Assignee:** Nils

#### **Ticket: [ENG-03] Reproducible Data Pipeline Script**
**Description:**
* **Context:** The raw 4GB dataset exceeds GitHub limits and local RAM capacities. To ensure all team members work on the exact same data foundation, we need a standardized local processing script.
* **Task:** Implement a data processing script (`make_dataset.py`) using pandas chunking to filter for booking events.
* **Implementation Steps:**
    1. Read `data/raw/train.csv` in chunks of 500,000 rows to optimize memory usage.
    2. Apply a filter for `is_booking == 1`.
    3. Export the consolidated filtered results to `data/processed/train_bookings_sample.csv`.
    4. Ensure the script handles directory creation and provides progress logs.
* **Expected Result:** Every team member generates an identical 3,000,693-row CSV file, ensuring reproducibility across all models and EDAs.
**Assignee:** Daniela

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

#### **Ticket: [EDA-01] Visual EDA & Target Leakage Audit**
**Description:**
* **Context:** Ensuring our features are valid and the model isn't "cheating."
* **Task:** Visual analysis of the 3M sample.
* **Steps:** 1. Plot Cluster distributions. 
    2. Check for "Data Leakage" (Is info available at search time?).
**Expected Result:** 5-7 high-quality plots for the final presentation.
**Assignee:** *Unassigned*

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