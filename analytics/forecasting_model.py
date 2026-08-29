import pandas as pd

def run_phase3_forecasting():
    """
    Phase 3: Weighted pipeline forecast model, actual vs forecast variance,
    and scenario planning (Conservative, Base, Aggressive).
    """
    df = pd.read_csv('data/cleaned_pipeline.csv')
    
    total_pipeline = df['deal_amount'].sum()
    base_weighted_forecast = df['weighted_forecast_val'].sum()
    actual_closed_won = df[df['win_status'] == 'Won']['actual_closed_amount'].sum()
    
    # Forecast Variance Calculation
    variance_val = actual_closed_won - base_weighted_forecast
    variance_pct = (variance_val / base_weighted_forecast) * 100 if base_weighted_forecast > 0 else 0
    
    # Scenario Modeling
    conservative_target = base_weighted_forecast * 0.85
    aggressive_target = base_weighted_forecast * 1.15
    
    print("=== PHASE 3: REVENUE FORECASTING & VARIANCE REPORT ===")
    print(f"Total Unweighted Pipeline Value : ${total_pipeline:,.2f}")
    print(f"Base Weighted Forecast          : ${base_weighted_forecast:,.2f}")
    print(f"Actual Closed-Won Revenue       : ${actual_closed_won:,.2f}")
    print(f"Forecast Variance ($)           : ${variance_val:,.2f}")
    print(f"Forecast Variance (%)           : {variance_pct:.2f}%")
    print("\n--- Scenario Planning Targets ---")
    print(f"Conservative Target (85%)       : ${conservative_target:,.2f}")
    print(f"Base Target (100%)              : ${base_weighted_forecast:,.2f}")
    print(f"Aggressive Target (115%)        : ${aggressive_target:,.2f}")

if __name__ == "__main__":
    run_phase3_forecasting()
