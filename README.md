# cookiecutter_stnotebook
This repo

## Prerequities

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

3. Once complete, you

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
- **notebook_name**: The name of your notebook
- **short_description**: A short description of your notebook

### Example

Let's run through an example



## Replaying a Project

When cookiecutter runs, it saves your prompt inputs to easily replay the project at a later time.  To reuse your previous inputs, specify the `replay` argument:
```
cookiecutter --replay https://github.com/havok2063/cookiecutter_stnotebook
```

## Custom User Default Prompts

To customize the default prompt inputs, you