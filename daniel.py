import os
from flask import Flask, render_template
from sqlite3 import dbapi2 as sqlite3

app = Flask(__name__)


app.config.update(dict(
    DATABASE=os.path.join(app.root_path, 'daniel.db'),
    DEBUG=True,
    SECRET_KEY='',
    USERNAME='admin',
    PASSWORD='admin'
))
app.config.from_envvar('FLASKR_SETTINGS', silent=True)

@app.route("/")
def index():
    # return "Hello World!"
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)