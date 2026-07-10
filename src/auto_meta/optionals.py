import glob
import importlib
import json
import os
import re

from git import Repo


def get_contributors(metadata, max_commits=800):
    # The info is extracted from across all commits
    # Open the metadata folder to get the current contrib list and lastest date
    contributors = metadata["Software"]["Contributors"]
    # Marker must be left to say which have been checked (date range)
    # Initialize the repository object - this connects to the git repo
    repo = Repo(search_parent_directories=True)
    # Iterate through commits starting from the most recent (HEAD)
    # max_count limits how many commits we process to avoid overwhelming data

    for commit in repo.iter_commits(max_count=max_commits):
        if (
            str(commit.committed_datetime)
            == metadata["Basic"]["Latest_commit"]
        ):
            pass
        else:
            if metadata["Software"]["privacy"]:
                contributors.append(f"{commit.author.name}")
            else:
                contributors.append(
                    f"{commit.author.name}, <{commit.author.email}>"
                )

    contributors = list(set(contributors))

    return contributors


def get_url():
    # Initialise the Repo object
    repo = Repo(search_parent_directories=True)
    # Extract the Git repository URL
    repo_url = repo.remotes.origin.url

    return str(repo_url)


def get_platform():
    # Open up the metadata and use the url value
    # Initialise the Repo object
    repo = Repo(search_parent_directories=True)
    # Extract the Git repository URL
    repo_url = repo.remotes.origin.url

    platform = re.findall(r"\/(\w+).", repo_url)[0]

    return platform


def get_langs():
    # The whole project needs to be spidered
    # Check each file type against this dict
    data_folder = importlib.resources.files("auto_meta") / "data"
    with importlib.resources.as_file(data_folder / "languages.json") as f:
        with open(f) as file:
            lang_dict = json.loads(file.read())

    # Go to parent folder and recursively glob to get all files
    files_list = glob.glob("**", root_dir=os.getcwd(), recursive=True)
    lang_list = []
    for file in files_list:
        try:
            lang_list.append(lang_dict["." + file.split(".")[-1]])
        except Exception as e:
            print(e)
    lang_list = list(set(lang_list))

    return lang_list


def get_license():
    # Check for license file and take the type from the first line
    try:
        with open(os.path.join(os.getcwd(), "LICENSE")) as file:
            license = file.readlines()
        return license[0].split("\n")[0]
    except FileNotFoundError:
        print("""There is no license for this project.
              That will make publishing and sharing your work difficult.""")
        return ""


def get_release_date():
    repo = Repo(search_parent_directories=True)
    # repo = Repo(repo_path)
    try:
        # Get the latest tag (most recent one)
        latest_tag = repo.tags.sort(key=lambda x: x.commit.committed_datetime)[
            -1
        ]
        # Get the commit associated with the tag
        commit = latest_tag.commit
        # Get the date of the commit
        release_date = commit.committed_datetime
    except TypeError:
        release_date = ""

    return release_date


def get_contact(metadata):
    if metadata["Software"]["privacy"]:
        contact = "redacted"
    else:
        # Open up repo object and take the email of the most
        ## recent commit maker
        repo = Repo(search_parent_directories=True)
        for commit in repo.iter_commits(max_count=1):
            contact = commit.author.email

    return contact
