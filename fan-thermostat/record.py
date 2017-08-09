from datetime import datetime
import os


def record(target, inside_temp, outside_temp):
    now = datetime.utcnow()
    dir_name = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'records', str(now.year))
    os.makedirs(dir_name, exist_ok=True)
    file_name = os.path.join(dir_name, datetime.utcnow().strftime('%Y-%m-%d') + '.record')
    with open(file_name, 'a') as file:
        file.write('{timestamp}:{target};{inside};{outside}\n'.format(
            timestamp=now.isoformat(),
            target=target,
            inside=inside_temp,
            outside=outside_temp,
        ))
