import os
from flask import Flask, render_template
from flaskext.mysql import MySQL
from datetime import datetime

# Configuration
mysql = MySQL()

app = Flask(__name__)

app.config['MYSQL_DATABASE_HOST'] = 'localhost'
# app.config['MYSQL_DATABASE_PORT'] = 8889
app.config['MYSQL_DATABASE_USER'] = 'root'
# app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
app.config['MYSQL_DATABASE_DB'] = 'test'

mysql.init_app(app)

app.config.from_envvar('DANIEL_SETTINGS', silent=True)


@app.route('/')
def index():
    cursor = mysql.get_db().cursor()
    # Get Projects
    cursor.execute('''SELECT * FROM wp_posts
        WHERE post_type='project' 
        AND post_status='publish' 
        ORDER BY post_date DESC''')
    entries = cursor.fetchall()
    # LEFT JOIN test.wp_term_relationships
    # ON wp_posts.ID=wp_term_relationships.object_id
    # Get About
    cursor.execute('''SELECT * FROM wp_posts WHERE ID=1251''')
    about = cursor.fetchone()
    
    return render_template('index.html', entries=entries, about=about)


@app.route('/wheres-my-car-privacy-policy/')
def wmc_privacy_policy():
    cursor = mysql.get_db().cursor()
    cursor.execute('''SELECT * FROM wp_posts WHERE ID=1389''')
    policy = cursor.fetchone()

    return render_template('wmc-privacy-policy.html', policy=policy)


def current_year():
    return datetime.now().year

app.jinja_env.globals.update(current_year=current_year)


def get_stack(post_id):
    cursor = mysql.get_db().cursor()
    # Get Stacks
    cursor.execute('''SELECT wp_term_taxonomy.term_id, taxonomy FROM wp_term_relationships
        LEFT JOIN wp_term_taxonomy
        ON wp_term_relationships.term_taxonomy_id=wp_term_taxonomy.term_taxonomy_id
        WHERE object_id =1454''')
    stack = cursor.fetchall()

    return stack

app.jinja_env.globals.update(get_stack=get_stack)


if __name__ == "__main__":
    app.run(debug=True)