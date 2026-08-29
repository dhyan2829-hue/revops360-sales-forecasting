import pandas as pd
import numpy as np

def run_phase1_data_foundation():
    """
    Phase 1: Ingest raw CRM pipeline data, build dimensions, handle nulls, 
    and output clean records with stage probabilities.
    """
    df = pd.read_csv('data/raw_pipeline.csv')
    
    # 1. Date Transformations & Cycle Time
    df['created_date'] = pd.to_datetime(df['created_date'])
    df['close_date'] = pd.to_datetime(df['close_date'])
    df['sales_cycle_days'] = (df['close_date'] - df['created_date']).dt.days
    df['projected_close_date'] = df['close_date'].fillna(df['created_date'] + pd.Timedelta(days=30))
    
    # 2. Stage Probability Mapping for Weighted Forecasting
    stage_probabilities = {
        'Discovery': 0.10,
        'Qualification': 0.25,
        'Proposal': 0.50,
        'Negotiation': 0.75,
        'Closed Won': 1.00,
        'Closed Lost': 0.00
    }
    
    df['win_probability'] = df['stage'].map(stage_probabilities)
    df['weighted_forecast_val'] = df['deal_amount'] * df['win_probability']
    
    # Save processed dimensional dataset
    df.to_csv('data/cleaned_pipeline.csv', index=False)
    print("Phase 1 Complete: Dataset cleaned and saved to data/cleaned_pipeline.csv")

if __name__ == "__main__":
    run_phase1_data_foundation()
