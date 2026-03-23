import pandas as pd

# 1. Sample Data: Simulating the type of data you handle at Appen or Clickworker
data = {
    'query': ['laptop charger', 'wireless mouse', 'mechanical keyboard', 'usb-c hub'],
    'result_title': ['Universal AC Adapter', 'Logitech M185', 'Razer BlackWidow', 'null'],
    'relevance_score': [0.95, 0.88, 0.45, 0.00],
    'has_description': [True, True, True, False]
}

df = pd.DataFrame(data)

def audit_data(row):
    """Flags data that needs manual review based on QA protocols."""
    reasons = []
    # Flag low relevance scores (below 0.50)
    if row['relevance_score'] < 0.50:
        reasons.append("Low Relevance Score")
    # Flag missing content (null values)
    if row['result_title'] == 'null' or not row['has_description']:
        reasons.append("Incomplete Metadata")
    
    return ", ".join(reasons) if reasons else "Pass"

# 2. Run the Audit
df['QA_Status'] = df.apply(audit_data, axis=1)

# 3. Output the results
print("--- QA Audit Results ---")
print(df[['query', 'relevance_score', 'QA_Status']])

# Export to CSV for a professional report
# df.to_csv('qa_audit_report.csv', index=False)
