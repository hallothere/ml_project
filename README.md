# AI Product Project - Expedia Hotel Recommendations (Classification)

## Project Description
This project focuses on optimizing the user journey within the travel industry by improving hotel search relevance. Using the **Expedia Dataset**, we aim to classify which hotel cluster a user is most likely to book.

Our approach centers on **AI Product Thinking** to bridge the gap between algorithmic performance and business value. By framing this as a **Multi-class Classification** task, we aim to provide personalized recommendations that:
- Reduce search friction in the booking funnel.
- Align ML evaluation metrics (MAP@5, Hit Rate) with business KPIs like Conversion Rate (CR).
- Address technical feasibility, including handling highly imbalanced data and preventing data leakage.

## The Way to Success: Deliverables & Workflow
The project is structured to simulate a real-world machine learning deployment, moving from strategic framing to technical execution:

1. **Strategic Framing:** Defining the Product Requirements Document (PRD), user personas, and success metrics.
2. **Data Intelligence:** Performing Exploratory Data Analysis (EDA) to identify patterns, data gaps, and bias risks.
3. **ML Engineering:** Implementing baseline models (Popularity/Decision Trees) and advanced iterations (Gradient Boosting).
4. **Experimentation & Rationale:** Documenting model iterations and the decision-making process for the chosen features and hyperparameters.
5. **Business Alignment:** Mapping ML performance back to product-level OKRs (Objectives and Key Results).
6. **Risk & Deployment:** Conducting failure mode analysis and defining a post-launch iteration roadmap.

## Objectives
By the end of this project, the following core competencies are demonstrated:

- **AI Product Leadership:** Translating complex business problems into viable multi-class classification objectives.
- **ML Framing & Selection:** Justifying the use of Decision Trees/Gradient Boosting for tabular data and establishing a strong baseline.
- **Analytical Reasoning:** Evaluating data feasibility and identifying risks such as class imbalance or data leakage.
- **Technical Literacy:** Proficiency in implementing and tuning Classifiers and custom ranking metrics.
- **Strategic Communication:** Translating technical trade-offs into actionable insights for stakeholders.
- **Operational Excellence:** Managing the end-to-end ML lifecycle, from initial discovery to ethical risk mitigation.

---

## Set up your Environment

Please make sure you have cloned or forked the repo and set up a new virtual environment. The [requirements file](requirements.txt) contains all libraries and dependencies needed.

*Note: If there are errors during environment setup, try removing the versions from the failing packages in the requirements file (especially on M1/M2/M3 Macs).*

### **`macOS`** type the following commands: 
- Install the virtual environment and the required packages by following commands.

    ```BASH
    pyenv local 3.11.3
    python -m venv .venv
    source .venv/bin/activate
    pip install --upgrade pip
    pip install -r requirements.txt
    ```
### **`WindowsOS`** type the following commands :

- Install the virtual environment and the required packages by following commands.

   For `PowerShell` CLI :

    ```PowerShell
    pyenv local 3.11.3
    python -m venv .venv
    .venv\Scripts\Activate.ps1
    python -m pip install --upgrade pip
    pip install -r requirements.txt
    ```

    For `Git-Bash` CLI :
  
    ```BASH
    pyenv local 3.11.3
    python -m venv .venv
    source .venv/Scripts/activate
    python -m pip install --upgrade pip
    pip install -r requirements.txt
    ```
     **`Note:`**
    If you encounter an error when trying to run `pip install --upgrade pip`, try using the following command:

    ```Bash
    python.exe -m pip install --upgrade pip
    ```

---

## Data Pipeline & Reproducibility
Due to the significant size of the original dataset (exceeding 4GB), we do not store raw data in this repository. We use a standardized pipeline to ensure consistency and memory efficiency across the team.

### 1. Environment Update
Before running the pipeline, ensure your virtual environment is active and all dependencies (including `pyarrow` for Parquet support) are up to date:

```BASH
pip install -r requirements.txt
```

### 2. Source Data
Download the dataset from the Kaggle Expedia Competition.

Place train.csv and destinations.csv into the data/raw/ directory.

### 3. Processing & Optimization Strategy
The automated script make_dataset.py transforms the raw data into our "Single Source of Truth":

- Filtering: Focuses on confirmed bookings (is_booking = 1).

- Merging: Enriches logs with latent features from destinations.csv.

- Cleaning: Removes records with missing destination signals (approx. 12k rows).

- Memory Optimization: Uses chunking for low-RAM processing and casts features to float32.

- High-Speed Storage: Saves the result in Parquet format for optimized loading.

### 4. Generate the Dataset
- Run the following command to create the model-ready dataset:
```BASH
python src/data/make_dataset.py
```

**Expected Output:** The script generates data/processed/df_model.parquet. This file (~2.98M rows) is the mandatory foundation for all EDA and Modeling tasks.

## Project Structure
```text
├── data
│   ├── raw             # Original Kaggle files (train.csv, destinations.csv)
│   └── processed       # Filtered 3M booking sample
├── notebooks           # EDA and Model experiments
├── src
│   ├── data            # make_dataset.py (Processing script)
│   ├── features        # make_features.py (Feature engineering modules)
│   └── evaluation      # evaluation.py (MAP@5 scoring logic)
├── PRD.md              # Product Requirements Document
└── requirements.txt    # Project dependencies
```