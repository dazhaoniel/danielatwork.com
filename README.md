Daniel Zhao - Portfolio
=======================

# Introduction

This is a simple static one page website built with Flask and hosted on [Heroku](https://heroku.com). I was able to quickly moving from Bluehost to Heroku, thanks to the tutorials in [this post](https://ksylvest.com/posts/2014-05-02/deploying-wordpress-to-heroku).

I built it for [danielatwork.com](http://danielatwork.com) on top of my old WordPress website, but it can be used to power any static pages and can serve as a useful template for starting a one page portfolio site with MySQL and static media (JavaScript, CSS, HTML, etc).

# Dependencies

1. Flask: `pip install Flask`
2. Flask-MySQL: `pip install flask-mysql`

# Commands to run it locally

1. Initialize Database: `mysql -u -p test < wordpress.sql`

2. Start MySQL Server: `mysql.server start`

3. Run The Application: `python daniel.py`

# HTML Template

The HTML Template is from [Read Only by HTML5 Up](http://html5up.net/read-only)

# Site

[Daniel Zhao - Portfolio](http://danielatwork.com)
