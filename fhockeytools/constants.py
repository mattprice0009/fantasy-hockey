WEEKS = {
  '23': {
    'start': '2024-03-18',
    'end': '2024-03-24'
  },
  '24': {
    'start': '2024-03-25',
    'end': '2024-03-31'
  },
  '25': {
    'start': '2024-04-01',
    'end': '2024-04-07'
  },
}
"""
Downloaded from https://media.nhl.com/public/news/17233
In Excel, I re-formatted the DATE column to YYYY-MM-DD.
Converted to CSV.
"""
SCHEDULE_FP_23_24 = 'res/2023-2024_schedule.csv'


class SCHEDULE_COLS:
  DAY = 'DAY'
  DATE = 'DATE'
  AWAY_TEAM = 'AWAY'
  HOME_TEAM = 'HOME'


OFF_DAYS = [ 'Mon', 'Wed', 'Fri', 'Sun']
