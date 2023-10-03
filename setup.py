from setuptools import find_packages, setup


dependencies = ['click']

pkg_name = 'fhockey'

setup(
  name=pkg_name,
  version='0.0.1',
  author='Matt Price',
  description='Useful tools for fantasy hockey managers',
  long_description=__doc__,
  package_data={
    pkg_name: [
      'res/2023-2024_schedule.csv', 'res/FetchLeagueScoreboard_response_2023-2024.json'
    ]
  },
  packages=find_packages(where='.', exclude=['tests']),
  include_package_data=True,
  zip_safe=False,
  platforms='any',
  install_requires=dependencies,
  entry_points={
    'console_scripts': [ f'{pkg_name} = {pkg_name}.cli:entry', ],
  }
)
