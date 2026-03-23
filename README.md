Data Quality Auditor (Python)

 Project Overview

This project was developed to streamline Quality Assurance workflows for large-scale data evaluation projects. It uses the Pandas library to automate the identification of anomalies in search relevance datasets.

Problem Solved: In high-volume data labeling, manual audits for missing metadata or inconsistent relevance scores are time-consuming and prone to human error. This script automates the first pass of QA, allowing the evaluator to focus on complex edge cases.

 Key Features

*Automated Flagging: Detects low-relevance scores that require secondary review.
*Metadata Validation: Identifies "null" or missing result titles and descriptions to ensure data integrity for NLP model training.
*Efficiency: Reduces manual review time by filtering out "clean" data and highlighting only the high-risk samples.

 Tech Stack 
 
*Language: Python 
*Library: Pandas (Data Manipulation) 

########################################################################################

 How to Run
To test this script locally, follow these steps:

1. Clone the repository:
   ```bash
   git clone [https://github.com/odomdworks-lang/data-quality-auditor.git](https://github.com/odomdworks-lang/data-quality-auditor.git)

2. Install dependencies:
Ensure you have Python installed, then install the Pandas library:
   ```bash
   pip install -r requirements.txt

  Expected Output
  
The script will generate a summary of the data audit, specifically flagging rows that fail the "Low Relevance" or "Incomplete Metadata" checks.
