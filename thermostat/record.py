from datetime import datetime
import os


def record(target, inside_temp, outside_temp):
    now = datetime.utcnow()
    dir_name = get_dir_name(now.year)
    os.makedirs(dir_name, exist_ok=True)
    file_name = get_file_name(now)
    with open(file_name, 'a') as file:
        file.write('{timestamp};{target};{inside};{outside}\n'.format(
            timestamp=now.isoformat(),
            target=target,
            inside=inside_temp,
            outside=outside_temp,
        ))


def get_last(hours):
    date = datetime.utcnow()
    while hours > 0:
        with open(get_file_name(date), 'r') as file:
            file.readlines()


def get_dir_name(year):
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'records', str(year))


def get_file_name(date):
    return os.path.join(get_dir_name(date), date.strftime('%Y-%m-%d') + '.record')
