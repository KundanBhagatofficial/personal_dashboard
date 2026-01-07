from datetime import datetime, timezone
from zoneinfo import ZoneInfo, ZoneInfoNotFoundError


class DateTimeService:
    def __init__(self, tz: str):
        try:
            self.tz = ZoneInfo(tz)
        except ZoneInfoNotFoundError:
            raise ValueError(f"Invalid TimeZone: {tz}")

    def now(self):
        utc_now = datetime.now(timezone.utc)
        local_time = utc_now.astimezone(self.tz)
        return {
            "utc": utc_now.isoformat(),
            "local_time": local_time.isoformat(),
            "timezone": str(self.tz),
        }
