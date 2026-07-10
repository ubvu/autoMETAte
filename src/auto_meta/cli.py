# Shell for the CLI tool
import datetime as dt
import importlib.resources
import os

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

META_FUNCS = {
    "Basic": {
        "Title": get_title(),
        "Description": get_description(),
        "Version": get_version(),
        "Latest_commit": get_commit_date(),
    },
    "Software": {
        "URL": get_url(),
        "Platform": get_platform(),
        "Contributors": get_contributors,
        "Programming_langs": get_langs(),
        "License": get_license(),
        "Release_date": get_release_date(),
        "Contact_person": get_contact,
    },
}

META_PATH = os.path.join(os.getcwd(), "software_metadata.toml")


def main():
    # Check for metadata and make it or check time diff
    if not os.path.isfile(META_PATH):
        open(META_PATH, "w")
        data_folder = importlib.resources.files("auto_meta") / "data"
        with importlib.resources.as_file(
            data_folder / "software_metadata_template.toml"
        ) as f:
            with open(f) as file:
                template = tomlkit.load(file)
        with open(META_PATH, mode="wt", encoding="utf-8") as ft:
            tml_str = tomlkit.dumps(template)
            ft.write(tml_str)
    elif (dt.datetime.now().timestamp() - os.path.getmtime(META_PATH)) < 120:
        return 0
    # Load the metadata file and check which fields are empty
    with open(META_PATH, mode="rt", encoding="utf-8") as file:
        metadata = tomlkit.load(file)
        print(metadata)
    # These should only need to run once for any project
    # Any changes can be done manually by the user
    ## or a check could run to confirm they are the same
    empties = ["Title", "Description", "URL", "Platform", "License"]
    # All other functions should run everytime
    for section in META_FUNCS.keys():
        for field in META_FUNCS[section]:
            if (
                metadata[section][field] == "" and field in empties
            ) or field not in empties:
                if field in ["Contributors", "Contact_person"]:
                    metadata[section][field] = META_FUNCS[section][field](
                        metadata
                    )
                else:
                    metadata[section][field] = META_FUNCS[section][field]
                print(field, metadata[section][field])
            else:
                pass
    with open(META_PATH, mode="wt", encoding="utf-8") as fp:
        meta_full = tomlkit.dumps(metadata)
        fp.write(meta_full)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
