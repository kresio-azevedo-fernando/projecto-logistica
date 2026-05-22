"""
ETL Pipeline — Logistics Optimisation Project
==============================================
Author: Kresio Azevedo Fernando
Portfolio: kresio-azevedo-fernando.github.io

Purpose:
    Extracts data from Excel dataset, transforms and cleans it,
    and loads it into a SQLite database ready for SQL analysis
    and Power BI dashboard consumption.

Usage:
    python etl_pipeline.py

Output:
    logistics.db — SQLite database with cleaned tables
"""

import pandas as pd
import sqlite3
import os
from datetime import datetime


# ── CONFIGURATION ────────────────────────────────────────────
EXCEL_PATH = "../dados/dataset-anonimizado.xlsx"
DB_PATH    = "logistics.db"


# ── EXTRACT ──────────────────────────────────────────────────
def extract(path: str) -> dict[str, pd.DataFrame]:
    """Load all sheets from the Excel file."""
    print(f"[EXTRACT] Reading: {path}")
    xl = pd.ExcelFile(path)
    sheets = {}
    for sheet in xl.sheet_names:
        sheets[sheet] = xl.parse(sheet)
        print(f"  ✓ Sheet '{sheet}' — {len(sheets[sheet])} rows")
    return sheets


# ── TRANSFORM ────────────────────────────────────────────────
def transform(sheets: dict[str, pd.DataFrame]) -> dict[str, pd.DataFrame]:
    """Clean, standardise and enrich each table."""
    print("\n[TRANSFORM] Cleaning and standardising data...")
    cleaned = {}

    for name, df in sheets.items():
        # Standardise column names
        df.columns = (
            df.columns
            .str.strip()
            .str.lower()
            .str.replace(" ", "_")
            .str.replace(r"[^\w]", "", regex=True)
        )

        # Remove fully empty rows
        df = df.dropna(how="all")

        # Add audit columns
        df["_loaded_at"] = datetime.utcnow().isoformat()

        cleaned[name] = df
        print(f"  ✓ '{name}' cleaned — {len(df)} rows, {len(df.columns)} columns")

    return cleaned


# ── LOAD ─────────────────────────────────────────────────────
def load(tables: dict[str, pd.DataFrame], db_path: str) -> None:
    """Write all tables to SQLite."""
    print(f"\n[LOAD] Writing to: {db_path}")
    conn = sqlite3.connect(db_path)

    for table_name, df in tables.items():
        safe_name = table_name.lower().replace(" ", "_")
        df.to_sql(safe_name, conn, if_exists="replace", index=False)
        print(f"  ✓ Table '{safe_name}' — {len(df)} rows loaded")

    conn.close()
    print(f"\n[DONE] Database ready: {db_path}")


# ── VALIDATE ─────────────────────────────────────────────────
def validate(db_path: str) -> None:
    """Quick row-count check on every table."""
    print("\n[VALIDATE] Row counts:")
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    tables = cursor.execute(
        "SELECT name FROM sqlite_master WHERE type='table'"
    ).fetchall()
    for (t,) in tables:
        count = cursor.execute(f"SELECT COUNT(*) FROM '{t}'").fetchone()[0]
        print(f"  {t}: {count} rows")
    conn.close()


# ── MAIN ─────────────────────────────────────────────────────
def run():
    print("=" * 55)
    print(" ETL Pipeline — Logistics Optimisation")
    print(f" Started: {datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')} UTC")
    print("=" * 55)

    if not os.path.exists(EXCEL_PATH):
        print(f"\n[ERROR] File not found: {EXCEL_PATH}")
        print("Place the Excel dataset in the 'dados/' folder and retry.")
        return

    sheets = extract(EXCEL_PATH)
    tables = transform(sheets)
    load(tables, DB_PATH)
    validate(DB_PATH)

    print("\n[PIPELINE COMPLETE]")
    print(f"  Database: {DB_PATH}")
    print(f"  Tables:   {list(tables.keys())}")
    print("  Next step: open sql-analysis.ipynb in Google Colab")


if __name__ == "__main__":
    run()
