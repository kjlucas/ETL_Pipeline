from datetime import datetime
from typing import Tuple, Optional


def validate_row(row: dict) -> Tuple[bool, Optional[str]]:
    try:
        #Validate the Date value
        date_str = row.get("observation_date")
        if not date_str:
            return False, "Missing date"

        datetime.strptime(date_str, "%Y-%m-%d")

        #Validate the "value" value
        value = row.get("value")
        if value is None or value == "":
            return False, "Missing value"

        float(value)

        return True, None

    except ValueError:
        return False, "Invalid format"