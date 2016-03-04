import os
from flask import Flask, render_template
from flaskext.mysql import MySQL
from datetime import datetime

# Configuration
mysql = MySQL()

app = Flask(__name__)

app.config['MYSQL_DATABASE_HOST'] = 'localhost'
# app.config['MYSQL_DATABASE_PORT'] = 8889
# app.config['MYSQL_DATABASE_USER'] = 'root'
# app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
app.config['MYSQL_DATABASE_DB'] = 'test'

mysql.init_app(app)

app.config.from_envvar('DANIEL_SETTINGS', silent=True)


@app.route('/')
def index():
    cursor = mysql.connect().cursor()
    cursor.execute("SELECT * FROM wp_posts")
    entries = cursor.fetchone()
    current_year = datetime.now().year
    return render_template('index.html', entries=entries, year=current_year)


@app.route('/wheres-my-car-privacy-policy')
def wmc_privacy_policy():
    return render_template('wmc-privacy-policy.html')


if __name__ == "__main__":
    app.run(debug=True)