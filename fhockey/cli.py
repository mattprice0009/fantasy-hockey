import os

import click


class FHockeyCommands(click.MultiCommand):

  plugin_folder = os.path.join(os.path.dirname(__file__), 'commands')

  def list_commands(self, ctx):
    rv = []
    for filename in os.listdir(self.plugin_folder):
      if filename.endswith(
          '.py'
      ) and '__init__' not in filename and 'command_helpers' not in filename and 'user_helpers' not in filename:
        rv.append(filename[:-3])
    rv.sort()
    return rv

  def get_command(self, ctx, name):
    ns = {}
    fn = os.path.join(self.plugin_folder, name + '.py')
    try:
      with open(fn) as f:
        code = compile(f.read(), fn, 'exec')
        eval(code, ns, ns)
    except IOError:
      print(
        '> Invalid command. Please type "fhockey --help" for help involving commands.'
      )
      return
    return ns[name]


@click.command(cls=FHockeyCommands)
def entry():
  pass
