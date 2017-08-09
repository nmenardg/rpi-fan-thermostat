from datetime import datetime
import os

from variables import ROOT_DIR


def record(target, inside_temp, outside_temp):
    now = datetime.utcnow()
    file_name = os.path.join(ROOT_DIR, 'records', str(now.year), datetime.utcnow().strftime('%Y-%m-%d') + '.record')
    with open(file_name, 'a') as file:
        file.write('{timestamp}:{target};{inside};{outside}\n'.format(
            timestamp=now.isoformat(),
            target=target,
            inside=inside_temp,
            outside=outside_temp,
        ))
