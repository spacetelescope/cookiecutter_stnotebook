# !usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under a 3-clause BSD license.
#
from __future__ import print_function, division, absolute_import
import os
import pathlib
import invoke

#
# This script runs before the cookiecutter template has been installed
#
current_dir = os.path.abspath(os.curdir)  # current template project directory
git_user = '{{ cookiecutter.github_username }}'
repo_name = '{{ cookiecutter._repo_name }}'
branch_name = ' {{cookiecutter.branch_name }}'
repo_path = '{{ cookiecutter.repo_path }}'
path = pathlib.Path(repo_path).expanduser().resolve()

@invoke.task
def cleanup(ctx):
    print('Cleaning up template project')
    print('current dir', current_dir)
    #ctx.run("rm -rf notebooks")


@invoke.task(post=[cleanup])
def copynb(ctx):
    print('current dir', current_dir)
    print('cp path', f'{path.parent}')
    #ctx.run(f"cp -r notebooks {path.parent}")


col = invoke.Collection(copynb)
ex = invoke.executor.Executor(col)
ex.execute('copynb')

