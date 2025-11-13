import subprocess


def start_app(exec_path):
    subprocess.Popen(exec_path)


def main():
    start_app("C:/Program Files/Microsoft Office/root/Office16/OUTLOOK.EXE")


if __name__ == "__main__":
    main()
