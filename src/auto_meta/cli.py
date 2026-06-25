# Shell for the CLI tool
import datetime as dt
import os
import shutil

import tomlkit
from basics import get_commit_date, get_description, get_title, get_version
from optionals import (
    get_contact,
    get_contributors,
    get_langs,
    get_license,
    get_platform,
    get_release_date,
    get_url,
)

meta_funcs = {
    "Basic": {
        "Title": get_title(),
        "Description": get_description(),
        "Version": get_version(),
        "Latest_commit": get_commit_date(),
    },
    "Software": {
        "URL": get_url,
        "Platform": get_platform,
        "Contributors": get_contributors,
        "Programming_langs": get_langs,
        "License": get_license,
        "Release_date": get_release_date,
        "Contact_person": get_contact,
    },
}


def main():
    # Check for metadata and make it or check time diff
    meta_path = os.path.join(os.getcwd(), "software_metadata.toml")
    if not os.path.isfile(meta_path):
        open(meta_path, "w")
        # TODO: Find out where this code lives
        # TODO find out how to include the template file in the package
        shutil.copyfile("software_metadata_template.toml", meta_path)
    elif (dt.datetime.now().timestamp() - os.path.getmtime(meta_path)) < 120:
        return 0
    # Load the metadata file and check which fields are empty
    with open(meta_path, mode="rt", encoding="utf-8") as file:
        metadata = tomlkit.load(file)
        # These should only need to run once for any project
        # Any changes can be done manually by the user
        ## or a check could run to confirm they are the same
        empties = ["Title", "Description", "URL", "Platform", "License"]
        # All other functions should run everytime
        for section in ["Basic", "Software"]:
            for field in metadata[section]:
                if (
                    metadata[section][field] == "" and field in empties
                ) or field not in empties:
                    metadata[section][field] = meta_funcs[field]
                else:
                    pass
        for section in meta_funcs.keys():
            for field in meta_funcs[section]:
                if (
                    metadata[section][field] == "" and field in empties
                ) or field not in empties:
                    metadata[section][field] = meta_funcs[field]
                else:
                    pass
        with open(meta_path, mode="wt", encoding="utf-8") as fp:
            tomlkit.dump(metadata, fp)


if __name__ == "__main__":
    raise SystemExit(main())
