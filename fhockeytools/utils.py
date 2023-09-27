from datetime import datetime, timedelta

from constants import WEEKS


# Return list of dates within specified range, including start/end dates
def date_range(start, end):
  earliest = datetime.strptime(start.replace('-', ' '), '%Y %m %d')
  latest = datetime.strptime(end.replace('-', ' '), '%Y %m %d')
  num_days = (latest - earliest).days + 1
  all_days = [latest - timedelta(days=x) for x in range(num_days)]
  all_days.reverse()

  dates = []
  # Return as String, yyyy-mm-dd
  for d in all_days:
    dates.append(str(d)[:10])
  return dates


def get_dates_for_week_key(week_key):
  if week_key not in WEEKS:
    raise RuntimeError(f'ERROR - week key "{week_key}" not configured')
  return date_range(WEEKS[week_key]['start'], WEEKS[week_key]['end'])
