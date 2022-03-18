# cookiecutter_stnotebook
This repo is a cookiecutter project for generating a new Jupyter notebook template for the Space Telescope Science Institute (STScI) [notebooks]((https://github.com/spacetelescope/notebooks)) repository.

- [cookiecutter_stnotebook](#cookiecutter_stnotebook)
  - [Prerequisites](#prerequisites)
  - [Creating a new template notebook](#creating-a-new-template-notebook)
  - [Cookiecutter Prompts](#cookiecutter-prompts)
    - [Template Output](#template-output)
    - [Example](#example)
  - [Replaying a Project](#replaying-a-project)
  - [Custom User Default Prompts](#custom-user-default-prompts)

## Prerequisites

Before you can create a new notebook template, you must meet the following prereqs:

1. Project Requirements.  This repo requires the [invoke](https://docs.pyinvoke.org/en/stable/index.html) and [cookiecutter](https://cookiecutter.readthedocs.io/en/1.7.2/index.html) python packages.  Run the following command to install:

```
pip install -U invoke cookiecutter
```
2. An existing Github Account.  [Sign up here](https://github.com/).
3. Fork the [spacetelescope/notebooks](https://github.com/spacetelescope/notebooks) repo into your Github user account. See [Fork A Repo](https://docs.github.com/en/get-started/quickstart/fork-a-repo) for details.

## Creating a new template notebook

1. In a new shell terminal, run

```
cookiecutter https://github.com/havok2063/cookiecutter_stnotebook
```

2. Follow the on-screen terminal prompts. See [Cookiecutter Prompts](#cookiecutter-prompts) for details.

3. Once completed, you will a have new template notebook which you can further customize.  You will also have a new active git branch in the `notebooks` repo. See the [Example](#example) below.

4. If you created a conda environment during project generation, or have an existing one, activate it with
```
conda activate notebooks_env
```

5. Navigate to your new notebook directory and run
```
jupyter notebook
```
6. Start customizing your notebook.

## Cookiecutter Prompts

When creating a new notebook project, it asks a series of input prompts (`prompt[default_value]`) to be used during template generation.  It prompts for the following inputs:

- **full_name**: Your full name
- **email**: Your professional email
- **github_username**: Your Github username
- **repo_exists_locally**: Whether or not the `notebooks` repo is already checked out locally
- **repo_path**: The top level directory where the repository is to be checked out, or is currently located
- **create_conda**:  Whether or not to create a new conda environment.  Default is "No".
- **branch_name**: A branch name for your new notebook. It will be prepended by the `nb_` prefix.
- **category**:  The category of notebook.  Default is "MAST".
- **mission**: A mission your notebook is most relevant for.
- **notebook_name**: The name of your notebook.  It must only consist of letters and underscores.  Default is the input `branch_name`.
- **short_description**: A short description of your notebook

### Template Output
The project creates a new notebook directory in the repository at `notebooks/[category]/[mission]/[notebook_name]/`. The directory contains two files:

- **requirements.txt**: A file of all required packages.
- **nb_[notebook_name].ipynb**: A template notebook for customization

### Example

Let's run through an example of creating a new notebook of spectral line fitting for JWST data for MAST.  In this scenario, we do not have the `notebooks` repo already checked out, and we already have a conda environment set up.

Starting from our home directory, we run the cookiecutter command and follow the on-screen prompt, seen below:
```bash
cd  # start from home dir and run cookiecutter
cookiecutter https://github.com/havok2063/cookiecutter_stnotebook

full_name [John Doe]: Brian Cherinka
email [myemail@here.com]: bcherinka@stsci.edu
github_username [gituser]: havok2063
Select repo_exists_locally:
1 - no
2 - yes
Choose from 1, 2 [1]: 1  # choose default "no" option
repo_path [.]:  # tell it to clone the repo in my current directory
Select create_conda:
1 - no
2 - yes
Choose from 1, 2 [1]: 1  # choose default "no" option
branch_name [mynotebook]: spectralfit
category [MAST]: # choose default
mission [JWST]: # choose default
notebook_name [spectralfit]: beginner_spectralfit # modify notebook name
short_description [A basic notebook template]: A beginner notebook for spectral fitting
```
The project will clone and checkout my fork of the `notebooks` repository, create a new branch, and add the `spacetelescope` remote upstream if it doesn't already exist.
```
Cloning git repo: notebooks
Cloning into 'notebooks'...
warning: redirecting to https://github.com/havok2063/notebooks/
Creating git branch: nb_spectralfit
Switched to a new branch 'nb_spectralfit'
Adding remote upstream to https://github.com/spacetelescope/notebooks
Cleaning up template project
```
A new notebook directory is generated at `notebooks/MAST/JWST/beginner_spectralfit`.

```bash
cd notebooks  # cd into the repo and check git status
(base) ➜  notebooks git:(nb_spectralfit) ✗ git status
On branch nb_spectralfit
Untracked files:
  (use "git add <file>..." to include in what will be committed)
	notebooks/MAST/JWST/

# cd into the new notebook repo
cd notebooks/notebooks/MAST/JWST/beginner_spectralfit
```
Now we can activate our conda environment and run start Jupyter
```bash
conda activate notebooks_env
jupyter notebook
```
We should see a new `nb_beginner_spectralfit.ipynb` template notebook, that looks like the following:

![Example Notebook](https://raw.githubusercontent.com/havok2063/cookiecutter_stnotebook/14fe469e1b63db46ffc129e550f5e3ec9c41de3e/example/template_notebook.png)

## Replaying a Project

When cookiecutter runs, it saves your prompt inputs to easily replay the project at a later time.  To reuse your previous inputs, specify the `replay` argument:
```
cookiecutter --replay https://github.com/havok2063/cookiecutter_stnotebook
```

## Custom User Default Prompts

To customize the default prompt inputs, you can create a user config file in your home directory at `~/.cookiecutterrc`.  Inside this file, specify any desired default prompts under the `default_context` key, for example:
```
default_context:
    full_name: "Brian Cherinka"
    email: "bcherinka@stsci.edu"
    github_username: "havok2063"
    repo_exists_locally: "yes"
    repo_path: "~/Work/git/havok2063"
```
