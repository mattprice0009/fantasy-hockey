import argparse
import csv
import json

from constants import OFF_DAYS, SCHEDULE_COLS, SCHEDULE_FP_23_24
from utils import get_dates_for_week_key


class ScheduleTools:

  def team_games_in_many_weeks(self, week_keys_list):
    """ Run team_games_in_week multiple times, aggregating results """
    print('running weeks', week_keys_list)
    team_counts = {}
    for week_key in week_keys_list:
      self.team_games_in_week(week_key, team_counts)

    self.view_counts(team_counts)

  def team_games_in_week(self, week_key, team_counts={}):
    """ Get counts of total games played, and total off-day games, by team."""
    print('running week', week_key)
    d_range = set(get_dates_for_week_key(week_key))

    with open(SCHEDULE_FP_23_24, 'r') as csvfile:
      csvreader = csv.DictReader(csvfile, delimiter=',')
      for row in csvreader:
        if row[SCHEDULE_COLS.DATE] in d_range:
          for k in [SCHEDULE_COLS.AWAY_TEAM, SCHEDULE_COLS.HOME_TEAM]:
            if row[k] not in team_counts:
              team_counts[row[k]] = { 'offdays': 0, 'total_games': 0}
            team_counts[row[k]]['total_games'] += 1
            if row[SCHEDULE_COLS.DAY] in OFF_DAYS:
              team_counts[row[k]]['offdays'] += 1

  def view_counts(self, team_counts):
    """ Print out the counts object (output of team_games_in_week functions)"""
    # print(json.dumps(team_counts, sort_keys=True, indent=2, default=str))

    # Sort teams first by offdays, then by total games, then alphabetically
    sorted_teams = sorted(
      team_counts.items(),
      key=lambda kv: (kv[1]['offdays'], kv[1]['total_games'], kv[0]),
      reverse=True
    )

    for team_obj in sorted_teams:
      team_name = team_obj[0]
      offdays = team_obj[1]['offdays']
      tot = team_obj[1]['total_games']
      print(f'{team_name} - {offdays} offdays, {tot} total games')


if __name__ == '__main__':
  parser = argparse.ArgumentParser(description='Run some useful commands')
  parser.add_argument('-w', '--week', help='The week(s) to check', required=True)
  args = parser.parse_args()

  handler = ScheduleTools()
  if ',' in args.week:
    handler.team_games_in_many_weeks(args.week.split(','))
  else:
    handler.team_games_in_week(args.week)
