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

Due to the significant size of the original dataset (the training set exceeds 4GB), we do not store raw data in this repository. To ensure all team members work on an identical data foundation without memory issues, follow these steps:

### 1. Source Data
Download the dataset from the [Kaggle Expedia Hotel Recommendations Competition](https://www.kaggle.com/competitions/expedia-hotel-recommendations/data). 
* Place the downloaded `train.csv` and `destinations.csv` into the `data/raw/` directory.

### 2. Data Sampling Strategy
To optimize for local development and high-signal events, we focus exclusively on **confirmed booking events** (`is_booking = 1`). This reduces the dataset from ~37M rows to a manageable **3.0M high-quality records**.

### 3. Generate the Dataset
Run the automated processing script to filter the data and prepare the working sample. This script uses **chunking** to ensure it runs efficiently on standard laptops with limited RAM:

```BASH
python src/data/make_dataset.py
````

**Expected Output:** The script will generate a consolidated file: `data/processed/train_bookings_sample.csv`. This file serves as the standardized foundation for all subsequent EDA and Modeling tasks.

---

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