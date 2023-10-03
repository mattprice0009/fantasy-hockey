import json
from datetime import datetime, timezone


def get_scoring_week_dates(season='2023-2024'):
  """
  This file should be a formatted response object from:
  `curl "https://www.fleaflicker.com/api/FetchLeagueScoreboard?sport=NHL&league_id=12091"`
  """
  with open(f'res/FetchLeagueScoreboard_response_{season}.json', 'r') as reader:
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
      print(week, str(start), str(end))
      all_weeks[week] = { 'end': end, 'start': start}
    return all_weeks
