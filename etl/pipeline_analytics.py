import pandas as pd

def run_phase2_pipeline_analytics():
    """
    Phase 2: Funnel stage conversion, lead source cohort tracking, 
    and stage bottleneck detection.
    """
    df = pd.read_csv('data/cleaned_pipeline.csv')
    
    print("=== PHASE 2: PIPELINE ANALYTICS REPORT ===")
    
    # 1. Stage Funnel Distribution
    print("\n--- Funnel Stage Breakdown ---")
    print(df['stage'].value_counts())
    
    # 2. Lead Source Cohorts
    cohort = df.groupby('lead_source').agg(
        total_deals=('opp_id', 'count'),
        total_pipeline=('deal_amount', 'sum'),
        avg_deal_size=('deal_amount', 'mean')
    ).reset_index()
    print("\n--- Lead Source Cohort Analysis ---")
    print(cohort.to_string(index=False))
    
    # 3. Bottleneck Detection (Deals stuck > 25 days in Qualification/Proposal)
    bottlenecks = df[(df['stage'].isin(['Qualification', 'Proposal'])) & (df['days_in_stage'] > 25)]
    print("\n--- BOTTLENECK ALERT: Deals Stuck > 25 Days ---")
    print(bottlenecks[['opp_id', 'rep_name', 'stage', 'days_in_stage', 'deal_amount']].to_string(index=False))

if __name__ == "__main__":
    run_phase2_pipeline_analytics()
