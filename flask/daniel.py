import os
from flask import Flask, render_template, g
from flaskext.mysql import MySQL
from sqlite3 import dbapi2 as sqlite3
from datetime import datetime

# Configuration
app = Flask(__name__)

app.config.update(dict(
    DATABASE=os.path.join(app.root_path, 'daniel.db'),
    DEBUG=True,
    SECRET_KEY='development key',
    USERNAME='admin',
    PASSWORD='admin'
))

app.config.from_envvar('DANIEL_SETTINGS', silent=True)


def connect_db():
    rv = sqlite3.connect(app.config['DATABASE'])
    rv.row_factory = sqlite3.Row
    return rv


def get_db():
    """Opens a new database connection if there is none yet for the
    current application context.
    """
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db


@app.route('/')
def index():
    db = get_db()
    cur = db.execute('select * from dp_entries order by last_updated desc')
    entries = cur.fetchall()
    current_year = datetime.now().year
    return render_template('index.html', entries=entries, year=current_year)


@app.route('/wheres-my-car-privacy-policy')
def wmc_privacy_policy():
    return render_template('wmc-privacy-policy.html')


if __name__ == "__main__":
    app.run(debug=True)