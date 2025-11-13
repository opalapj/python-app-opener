from pathlib import Path

import AppOpener as ao


def search_app_name(estimated_name):
    ao.open("find " + estimated_name)


def kill_app(name):
    ao.close(name)


def start_app(name):
    ao.open(name)


def save_app_names(pathname):
    ao.mklist(Path(pathname).name, str(Path(pathname).parent))


def main():
    search_app_name("outlook")
    save_app_names("data/app_names.json")
    start_app("OUTLOOK CLASSIC")
    # "OUTLOOK CLASSIC" does not work for killing.
    kill_app("OUTLOOK")


if __name__ == "__main__":
    main()
