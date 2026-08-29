# RevOps360 - Sales Pipeline & Revenue Forecasting Suite

## Executive Summary
RevOps360 unifies fragmented sales pipeline data into an automated ETL, analytics, and revenue forecasting layer to assist sales leadership with weekly and monthly operational planning.

## Key Phases Implemented
- **Phase 1 (Data Foundation):** Standardizes raw CRM pipeline ingest, handles date conversions, and maps stage win probabilities (`etl/data_cleaning.py`).
- **Phase 2 (Pipeline Analytics):** Performs funnel conversion tracking, cohort analysis by lead source, and bottleneck detection for stale deals (`etl/pipeline_analytics.py`).
- **Phase 3 (Forecasting Layer):** Calculates stage-weighted revenue forecasts, tracks actual vs. forecast variance, and executes conservative/base/aggressive scenario targets (`analytics/forecasting_model.py`).
- **Phase 4 (Executive Dashboarding):** Generates region drill-downs, weekly pipeline alerts, and board summary reports (`dashboards/EXECUTIVE_DASHBOARD.md`).

## Repository Architecture
- `data/raw_pipeline.csv`: Input CRM dataset.
- `etl/data_cleaning.py`: Phase 1 ETL script.
- `etl/pipeline_analytics.py`: Phase 2 bottleneck & funnel analytics script.
- `analytics/forecasting_model.py`: Phase 3 revenue forecast engine.
- `dashboards/EXECUTIVE_DASHBOARD.md`: Phase 4 board summary & drill-down report.
- `docs/KPI_Dictionary.md`: Business definitions for core metrics.
