# Data ETL Pipeline (Python + PostgreSQL)

## Overview

A Python-based ETL (Extract, Transform, Load) pipeline designed to process structured time-series data and store it in a PostgreSQL database.

The pipeline reads raw CSV data, validates and transforms records, then loads clean data into a relational database while logging errors and maintaining data integrity.

This project was built to simulate real-world data engineering workflows similar to those used in large-scale economic data platforms.

## Features

- Extracts data from CSV files
- Validates data for correctness (dates, numeric values, missing fields)
- Transforms data into a consistent format
- Loads data into PostgreSQL using SQLAlchemy
- Logs invalid records for debugging and auditing
- Prevents duplicate entries using database constraints
- Provides summary metrics after each run

## Data Validation Rules

- Date must be a valid ISO format (YYYY-MM-DD)
- Series ID must not be null
- Value must be numeric
- Duplicate records (date + series_id) are not inserted

```
ETL_pipeline/
├── app/
│ ├── db.py
│ ├── etl.py
│ ├── models.py
│ ├── validate.py
│ └── config.py
├── data/
│ └── sample_economic_data.csv
├── sql/
│ └── schema.sql
├── logs/
│ └── errors.log
├── imports.txt
├── README.md
└── main.py
```