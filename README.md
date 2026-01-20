# AIPM ML Project - Expedia Hotel Recommendations (Regression Variant)

## Project Description
This project focuses on optimizing the user journey within the travel industry by improving hotel search relevance. Using the **Expedia Dataset**, we aim to predict the likelihood of a user booking a specific hotel cluster.

Our approach centers on **AI Product Thinking** to bridge the gap between algorithmic performance and business value. While the task is implemented as a **Regression Variant** to estimate booking probabilities, the project scope covers the entire product lifecycle:
- Identifying user friction points in the search-to-booking funnel.
- Aligning ML evaluation metrics (MSE/MAE) with business KPIs like Conversion Rate (CR).
- Assessing technical feasibility, data leakage, and potential bias to ensure a trustworthy user experience.

## The Way to Success: Deliverables & Workflow
The project is structured to simulate a real-world machine learning deployment, moving from strategic framing to technical execution:

1. **Strategic Framing:** Defining the Product Requirements Document (PRD), user personas, and success metrics.
2. **Data Intelligence:** Performing Exploratory Data Analysis (EDA) to identify data gaps and bias risks.
3. **ML Engineering (Decision Trees):** - [Decision Trees Regression](1_Decision_Trees_Visualization.ipynb)
   - [Decision Trees Classification](2_Decision_Trees_Classification.ipynb)
4. **Experimentation & Rationale:** Documenting model iterations and the decision-making process for the final architecture.
5. **Business Alignment:** Mapping ML performance back to product-level OKRs (Objectives and Key Results).
6. **Risk & Deployment:** Conducting failure mode analysis and defining a post-launch iteration roadmap.

## Objectives
By the end of this project, the following core competencies are demonstrated:

- **AI Product Leadership:** The ability to translate complex business problems into viable machine learning objectives.
- **ML Framing & Selection:** Expertise in justifying model types (Regression vs. Classification) and establishing rigorous baselines.
- **Analytical Reasoning:** Evaluating data feasibility and identifying risks such as data leakage or fairness concerns early in the process.
- **Technical Literacy:** Proficiency in implementing and tuning Decision Tree algorithms, including the interpretation of splitting criteria and model pruning.
- **Strategic Communication:** Translating technical trade-offs (e.g., latency vs. accuracy) into actionable insights for stakeholders.
- **Operational Excellence:** Managing the end-to-end ML lifecycle, from initial discovery to risk mitigation and long-term maintenance strategies.

## Set up your Environment

Please make sure you have cloned or forked the repo and set up a new virtual environment. The [requirements file](requirements.txt) contains all libraries and dependencies needed.

*Note: If there are errors during environment setup, try removing the versions from the failing packages in the requirements file (especially on M1/M2/M3 Macs).*

### **`macOS`** type the following commands: 

- Install the virtual environment and the required packages by following commands:

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

## Data

The dataset for this project is sourced from the [Kaggle Expedia Hotel Recommendations Competition](https://www.kaggle.com/competitions/expedia-hotel-recommendations/data) 
. It includes user logs, search queries, and hotel cluster information, providing a high-dimensional playground for learning feature engineering and model optimization.