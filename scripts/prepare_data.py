"""
Optional helper: prepares aggregated CSVs from Superstore for quick sanity checks.
Usage:
    python scripts/prepare_data.py data/superstore.csv
Outputs:
    data/agg_monthly_sales.csv
    data/agg_category_sales.csv
    data/top10_products.csv
"""
import sys
import pandas as pd
from pathlib import Path

def main(path):
    df = pd.read_csv(path, parse_dates=['Order Date'])
    # Monthly sales
    monthly = (df
               .assign(month=df['Order Date'].dt.to_period('M').dt.to_timestamp())
               .groupby('month', as_index=False)['Sales'].sum())
    monthly.to_csv('data/agg_monthly_sales.csv', index=False)

    # Category sales
    cat = df.groupby('Category', as_index=False)['Sales'].sum().sort_values('Sales', ascending=False)
    cat.to_csv('data/agg_category_sales.csv', index=False)

    # Top 10 products
    top = (df.groupby('Product Name', as_index=False)['Sales'].sum()
             .sort_values('Sales', ascending=False)
             .head(10))
    top.to_csv('data/top10_products.csv', index=False)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python scripts/prepare_data.py data/superstore.csv")
        raise SystemExit(1)
    main(sys.argv[1])
