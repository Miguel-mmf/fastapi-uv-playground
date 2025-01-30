from datetime import datetime

import pytz


def get_current_datetime() -> str:
    tz = pytz.timezone("America/Sao_Paulo")
    return datetime.now(tz).isoformat()
