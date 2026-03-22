from app.etl import run_etl
from app.db import SessionLocal, init_db
from app.config import DATA_FILE

if __name__ == '__main__':

    # Creates "data_series" table from model
    init_db()

    # Opens db session
    db = SessionLocal()

    # Tries to run the pipeline
    try:
        run_etl(DATA_FILE, db)
    finally:
        db.session.close()