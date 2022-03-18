# !usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under a 3-clause BSD license.
#
from __future__ import print_function, division, absolute_import
import os
import re
import pathlib

#
# This script runs before the cookiecutter template has been installed
#
current_dir = pathlib.Path().resolve()
git_user = '{{ cookiecutter.github_username }}'
repo_name = '{{ cookiecutter._repo_name }}'
branch_name = '{{ cookiecutter.branch_name }}'.lower().replace(' ', '_')
branch_name = f"nb_{branch_name}"
repo_path = pathlib.Path('{{ cookiecutter.repo_path }}').expanduser().resolve()
clonedir = repo_path.parent if repo_path == current_dir else repo_path
repo_dir = clonedir / repo_name

# Checks that invoke is installed.

try:
    import invoke
    from invoke.exceptions import UnexpectedExit, Exit
except ImportError as e:
    raise ImportError('cannot import invoke. Did you run \'pip install invoke\'?') from e


@invoke.task
def branchgit(ctx):
    """ Checkout or create a new branch """
    res = ctx.run("git branch -l", hide='out')
    has_branch = f'{branch_name}' in res.stdout
    # check out the branch
    if has_branch:
        print(f'Checking out branch: {branch_name}')
        ctx.run(f"git checkout {branch_name}")
    else:
        print(f'Creating git branch: {branch_name}')
        ctx.run(f"git checkout -b {branch_name}")

@invoke.task
def addremote(ctx):
    """ Set up the remote upstream """
    # get origin and upstream remotes
    ores = ctx.run("git config --get remote.origin.url", hide='out')
    st_origin = 'github.com/spacetelescope' in ores.stdout
    user_origin = f'github.com/{git_user}' in ores.stdout
    try:
        upres = ctx.run("git config --get remote.upstream.url", hide='out')
    except UnexpectedExit:
        st_upstream = None
    else:
        st_upstream = 'github.com/spacetelescope' not in upres.stdout

    # set new upstream if needed
    if not st_origin and user_origin and not st_upstream:
       print('Adding remote upstream to https://github.com/spacetelescope/notebooks')
       ctx.run("git remote add upstream https://github.com/spacetelescope/notebooks")


@invoke.task(post=[branchgit, addremote])
def clonegit(ctx):
    """ Clones the notebooks git repo """

    os.chdir(clonedir)
    print(f'Cloning git repo: {repo_name}')

    try:
        ctx.run(f"git clone http://github.com/{git_user}/{repo_name} --depth=1")
    except UnexpectedExit as e:
        print('Unexpected failure during git clone:\n {0}'.format(e.result.stderr))
    os.chdir(repo_name)


@invoke.task(post=[branchgit])
def updategit(ctx):
    """ Update an existing notebooks git repo """

    if not repo_dir.exists():
        raise Exit(f'The repo directory {repo_dir} does not exist.  Check you are in the correct directory.')

    os.chdir(repo_dir)
    ctx.run("git checkout master")
    ctx.run("git fetch")
    ctx.run("git pull")


@invoke.task
def createconda(ctx):
    """ Create a conda environment """

    env = 'notebooks_env'
    currentenv = os.getenv("CONDA_DEFAULT_ENV")

    res = ctx.run("conda info -e", hide='out')
    has_env = "notebooks_env" in res.stdout
    if not has_env:
        print('Creating conda environment')
        with ctx.cd(repo_dir):
            ctx.run("conda env create -f environment.yml")


col = invoke.Collection(clonegit, updategit, createconda)
ex = invoke.executor.Executor(col)

# validate the notebook_name
nb_name = '{{ cookiecutter.notebook_name }}'
if not re.match("^[A-Za-z_]*$", nb_name):
    raise ValueError(f'Invalid notebook_name: {nb_name}.  It can only consist of letters and underscores.')

repo_exists = '{{ cookiecutter.repo_exists_locally }}'
if repo_exists in {'yes', 'y'}:
    ex.execute('updategit')
else:
    ex.execute('clonegit')

create_conda = '{{ cookiecutter.create_conda }}'
if create_conda in {'yes', 'y'}:
    ex.execute('createconda')


