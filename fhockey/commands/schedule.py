import csv
import json

import click
from fhockey.constants import OFF_DAYS, SCHEDULE_COLS
from fhockey.helpers import get_dates_for_week_key
from fhockey.utils import get_path


class ScheduleTools:

  def team_games_in_many_weeks(self, week_keys_list, season):
    """ Run team_games_in_week multiple times, aggregating results """
    team_counts = {}
    for week_key in week_keys_list:
      self.team_games_in_week(week_key, season, team_counts=team_counts)

    self.view_counts(team_counts)

  def team_games_in_week(self, week_key, season, team_counts={}, print_results=False):
    """ Get counts of total games played, and total off-day games, by team."""
    d_range = set(get_dates_for_week_key(week_key, season))

    fp = get_path(f'res/{season}_schedule.csv')
    with open(fp, 'r') as csvfile:
      csvreader = csv.DictReader(csvfile, delimiter=',')
      for row in csvreader:
        if row[SCHEDULE_COLS.DATE] in d_range:
          for k in [SCHEDULE_COLS.AWAY_TEAM, SCHEDULE_COLS.HOME_TEAM]:
            if row[k] not in team_counts:
              team_counts[row[k]] = { 'offdays': 0, 'total_games': 0}
            team_counts[row[k]]['total_games'] += 1
            if row[SCHEDULE_COLS.DAY] in OFF_DAYS:
              team_counts[row[k]]['offdays'] += 1

    if print_results:
      self.view_counts(team_counts)

  def view_counts(self, team_counts):
    """ Print out the counts object (output of team_games_in_week functions)"""

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
      print(f'{team_name} - {offdays} offday games, {tot} total games')


@click.command()
@click.option('--week', '-w', required=True, help='The week(s) to check')
@click.option(
  '--season',
  '-s',
  default='2023-2024',
  type=click.Choice(['2023-2024']),
  help='The NHL season'
)
def schedule(week, season):
  """View game counts by team"""
  handler = ScheduleTools()
  if ',' in week:
    handler.team_games_in_many_weeks(week.split(','), season)
  else:
    handler.team_games_in_week(week, season, print_results=True)
