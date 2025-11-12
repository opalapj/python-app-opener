import psutil


def search_executable(estimated_name):
    """
    Returns list of pairs name -> exe from running processes for given app (estimated name).
    """
    processes = []
    for process in psutil.process_iter(attrs=["name", "exe"]):
        if estimated_name.upper() in process.info["name"].upper():
            print(process.info["name"], " -> ", process.info["exe"])
            processes.append(process)
    return processes


def kill_app(process):
    process.kill()


def start_app(exec_path):
    """
    Use executable path founded by search_executable function.
    """
    psutil.Popen(exec_path)


def main():
    processes = search_executable("outlook")
    kill_app(processes[0])
    start_app(processes[0].exe())
    start_app("C:/Program Files/Microsoft Office/root/Office16/OUTLOOK.EXE")


if __name__ == "__main__":
    main()
