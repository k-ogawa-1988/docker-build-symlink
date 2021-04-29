from datetime import datetime


def print_with_time(*values: object):
    dt = datetime.now().isoformat()

    print(f'[{dt}] ', *values)
