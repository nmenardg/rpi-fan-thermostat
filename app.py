from flask import Flask, render_template

from thermostat import config
from thermostat import record

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html',
                           target_temp=config.fan_section['target_temp'],
                           records=record.get_last(hours=24),
                           )

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
