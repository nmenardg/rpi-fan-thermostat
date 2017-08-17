from datetime import datetime, timedelta
import os

iso_seconds_format = '%Y-%m-%dT%H:%M:%SZ'


def record(target, inside_temp, outside_temp):
    now = datetime.utcnow()
    dir_name = get_dir_name(now.year)
    os.makedirs(dir_name, exist_ok=True)
    file_name = get_file_name(now)
    with open(file_name, 'a') as file:
        file.write('{timestamp};{target};{inside};{outside}\n'.format(
            timestamp=now.strftime(iso_seconds_format),
            target=target,
            inside=inside_temp,
            outside=outside_temp,
        ))


def get_last(nb_hours):
    date = datetime.utcnow()
    past = date - timedelta(hours=nb_hours)
    hours = []
    while True:
        try:
            with open(get_file_name(date), 'r') as file:
                lines = file.readlines()
        except FileNotFoundError:
            return reversed(hours)

        for line in reversed(lines):
            splitted = line.split(';')
            date_str = splitted[0]
            try:
                line_date = datetime.strptime(date_str, iso_seconds_format)
            except ValueError:
                line_date = datetime.strptime(date_str, '%Y-%m-%dT%H:%M:%S.%f')
            if line_date < past:
                return reversed(hours)
            hours.append(splitted)
        date = date - timedelta(days=1)


def get_dir_name(year):
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'records', str(year))


def get_file_name(date):
    return os.path.join(get_dir_name(date.year), date.strftime('%Y-%m-%d') + '.record')
