import pandas as pd

from app.models import DataSeries
from app.validate import validate_row


def extract(file_path):
    dataframe = pd.read_csv(file_path)
    return dataframe


def transform(dataframe):
    # Rename column
    dataframe = dataframe.rename(columns={"observation_date": "date"})

    # Convert from wide → long format
    t_dataframe = dataframe.melt(
        id_vars=["date"],
        var_name="series_id",
        value_name="value"
    )

    return t_dataframe

def validate(dataframe):
    valid_rows = []
    invalid_rows = []
    for index, row in dataframe.iterrows():
        valid, error = validate_row(row)
        if not valid:
            #Rows with either date or value missing
            invalid_rows.append(row)
            print(f"row {index}: {error}")
        else:
            valid_rows.append(row)

    return valid_rows, invalid_rows

def load(valid_rows, db_session):
    #loads rows into session
    for index, row in valid_rows:
        entry = DataSeries(date=pd.to_datetime(row["date"]).date(), value=row["value"], series_id=row["series_id"])
        db_session.add(entry)

    # Commit all loads at once
    try:
        db_session.commit()
    except Exception as e:
        print(f"Commit failed: {e}")
        db_session.rollback()

    return len(valid_rows)

def run_etl(file_path, db):

    print("Starting ETL pipeline...")

    #Extract
    df = extract(file_path)
    total_rows = len(df)
    print(f"Extracted {total_rows} rows")

    #Transform
    df_transformed = transform(df)
    print(f"Transformed data shape: {df_transformed.shape}")

    #Validate
    valid_rows, invalid_rows = validate(df_transformed)

    print(f"Valid rows: {len(valid_rows)}")
    print(f"Invalid rows: {len(invalid_rows)}")

    #Load
    inserted_rows = load(valid_rows, db)
    print(f"Loaded {inserted_rows} rows")

    #Operation report
    report = {
        "Rows extracted": total_rows,
        "Rows transformed": len(df_transformed),
        "Valid rows ": len(valid_rows),
        "Invalid rows ": len(invalid_rows),
        "Rows inserted": len(inserted_rows)
    }

    print("ETL pipeline complete")
    print(report)

    return report