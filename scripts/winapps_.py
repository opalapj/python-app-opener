import winapps


def list_apps():
    for app in winapps.list_installed():
        print(app)


def search_app(name):
    for app in winapps.search_installed(name):
        print(app)


def main():
    list_apps()
    search_app("outlook")


if __name__ == "__main__":
    main()
