import os
from flask import Flask, render_template, request
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
    cursor.execute("SELECT * FROM wp_posts WHERE post_type='project' AND post_status='publish' ORDER BY post_date DESC")
    entries = cursor.fetchall()

    # Get About
    cursor.execute("SELECT * FROM wp_posts WHERE ID=1251")
    about = cursor.fetchone()
    
    return render_template('index.html', entries=entries, about=about)


@app.route('/wheres-my-car-privacy-policy/')
def wmc_privacy_policy():
    cursor = mysql.get_db().cursor()
    cursor.execute("SELECT * FROM wp_posts WHERE ID=1389")
    policy = cursor.fetchone()

    return render_template('wmc-privacy-policy.html', policy=policy)


def current_year():
    return datetime.now().year

app.jinja_env.globals.update(current_year=current_year)


def get_stack(post_id):
    cursor = mysql.get_db().cursor()
    # Get Stacks
    cursor.execute("SELECT wp_terms.name FROM wp_term_taxonomy, wp_term_relationships, wp_terms WHERE wp_term_relationships.object_id='"+ str(post_id) +"' AND wp_term_taxonomy.term_taxonomy_id=wp_term_relationships.term_taxonomy_id AND wp_term_taxonomy.taxonomy='skills' AND wp_term_taxonomy.term_id=wp_terms.term_id")
    stack = cursor.fetchall()

    return stack

app.jinja_env.globals.update(get_stack=get_stack)

# _pilotfish_meta_value_project_url_key
def get_meta_url(post_id):
    cursor = mysql.get_db().cursor()
    cursor.execute("SELECT meta_value FROM wp_postmeta WHERE post_id='"+ str(post_id) +"' AND meta_key='_pilotfish_meta_value_project_url_key'")
    meta = cursor.fetchone()

    return meta

app.jinja_env.globals.update(get_meta_url=get_meta_url)

# _pilotfish_meta_value_project_image_url_key
def get_meta_image_url(post_id):
    cursor = mysql.get_db().cursor()
    cursor.execute("SELECT meta_value FROM wp_postmeta WHERE post_id='"+ str(post_id) +"' AND meta_key='_pilotfish_meta_value_project_image_url_key'")
    meta = cursor.fetchone()

    return meta

app.jinja_env.globals.update(get_meta_image_url=get_meta_image_url)

# _pilotfish_meta_value_project_year_key
def get_meta_year(post_id):
    cursor = mysql.get_db().cursor()
    cursor.execute("SELECT meta_value FROM wp_postmeta WHERE post_id='"+ str(post_id) +"' AND meta_key='_pilotfish_meta_value_project_year_key'")
    meta = cursor.fetchone()

    return meta

app.jinja_env.globals.update(get_meta_year=get_meta_year)


if __name__ == "__main__":
    app.run(debug=True)