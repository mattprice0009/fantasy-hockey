import pkg_resources


ROOT_DIR = __name__.replace('.utils', '')


def get_path(fp, pkg=''):
  if not pkg:
    pkg = ROOT_DIR
  return pkg_resources.resource_filename(pkg, fp)
