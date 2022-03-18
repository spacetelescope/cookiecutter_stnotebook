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
current_dir = pathlib.Path().resolve()  # current template project directory
git_user = '{{ cookiecutter.github_username }}'
repo_name = '{{ cookiecutter._repo_name }}'
branch_name = ' {{cookiecutter.branch_name }}'
repo_path = pathlib.Path('{{ cookiecutter.repo_path }}').expanduser().resolve()
clonedir = repo_path.parent if repo_path == current_dir else repo_path
repo_dir = clonedir if clonedir.parts[-1] == repo_name else clonedir / repo_name


@invoke.task
def cleanup(ctx):
    print('Cleaning up template project')
    print('current dir', current_dir)
    print('real dir', os.path.abspath(os.curdir))
    with ctx.cd(current_dir.parent):
        ctx.run(f"rm -rf {current_dir}")


@invoke.task(post=[cleanup])
def copynb(ctx):
    print('current dir', os.path.abspath(os.curdir))
    print('repo_path', repo_path)
    print('clone_dir', clonedir)
    print('copy path', f'{repo_dir}')
    ctx.run(f"cp -r notebooks {repo_dir}")


col = invoke.Collection(copynb)
ex = invoke.executor.Executor(col)
ex.execute('copynb')

