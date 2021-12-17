import multiprocessing
from pathlib import Path

current_path = Path().absolute()
bind = "192.168.100.12:8000"
workers = multiprocessing.cpu_count() * 2 + 1
pythonpath = str(current_path) + "/project"


def on_exit(server):
    print('log : gunicorn conf - server stop ')
