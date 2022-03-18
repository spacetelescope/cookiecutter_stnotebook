# !usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under a 3-clause BSD license.
#
from __future__ import print_function, division, absolute_import
import pathlib
import invoke

#
# This script runs before the cookiecutter template has been installed
#
current_dir = pathlib.Path().resolve()  # current template project directory
repo_name = '{{ cookiecutter._repo_name }}'
repo_path = pathlib.Path('{{ cookiecutter.repo_path }}').expanduser().resolve()
clonedir = repo_path.parent if repo_path == current_dir else repo_path
repo_dir = clonedir if clonedir.parts[-1] == repo_name else clonedir / repo_name
nb_name = '{{ cookiecutter.notebook_name }}'


@invoke.task
def cleanup(ctx):
    """ Remove the template project directory """
    print('Cleaning up template project')
    with ctx.cd(current_dir.parent):
        ctx.run(f"rm -rf {current_dir}")

@invoke.task(post=[cleanup])
def copynb(ctx):
    """ Copy the template notebook into the repo """
    ctx.run(f"cp -r notebooks {repo_dir}")


col = invoke.Collection(copynb)
ex = invoke.executor.Executor(col)
ex.execute('copynb')

