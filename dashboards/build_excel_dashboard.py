import pandas as pd

# Load raw pipeline data
df = pd.read_csv('data/raw_pipeline.csv')

# Calculate stage win probabilities
stage_prob = {
    'Discovery': 0.10,
    'Qualification': 0.25,
    'Proposal': 0.50,
    'Negotiation': 0.75,
    'Closed Won': 1.00,
    'Closed Lost': 0.00
}
df['win_probability'] = df['stage'].map(stage_prob)
df['weighted_forecast_val'] = df['deal_amount'] * df['win_probability']

# Write directly to Excel Dashboard
with pd.ExcelWriter('dashboards/RevOps360_Executive_Dashboard.xlsx', engine='openpyxl') as writer:
    # Summary Dashboard Sheet
    summary_stage = df.groupby('stage')[['deal_amount', 'weighted_forecast_val']].sum().reset_index()
    summary_stage.to_excel(writer, sheet_name='Executive Dashboard', index=False, startrow=2)
    
    # Raw Data Sheet
    df.to_excel(writer, sheet_name='Data_Pipeline', index=False)

print("Dashboard created successfully!")
