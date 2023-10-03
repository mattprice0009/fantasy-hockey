import json
from datetime import datetime, timedelta, timezone

from fhockey.utils import get_path


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


def get_dates_for_week_key(week_key, season):
  """
  This file should be a formatted response object from:
  `curl "https://www.fleaflicker.com/api/FetchLeagueScoreboard?sport=NHL&league_id=12091"`
  """
  fp = get_path(f'res/FetchLeagueScoreboard_response_{season}.json')
  with open(fp, 'r') as reader:
    d = json.load(reader)
    all_weeks = {}
    for period in d['eligibleSchedulePeriods']:
      week = str(period['ordinal'])
      start_ts = int(period['low']['startEpochMilli']) / 1000
      end_ts = int(period['high']['startEpochMilli']) / 1000
      start = datetime.utcfromtimestamp(start_ts).replace(tzinfo=timezone.utc
                                                          ).strftime('%Y-%m-%d')
      end = datetime.utcfromtimestamp(end_ts).replace(tzinfo=timezone.utc
                                                      ).strftime('%Y-%m-%d')
      all_weeks[week] = { 'end': end, 'start': start}
    return date_range(all_weeks[week_key]['start'], all_weeks[week_key]['end'])
