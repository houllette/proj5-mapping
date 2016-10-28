import flask
from flask import render_template

import logging

# Our own module
import POI_list
import secrets

###
# Globals
###
app = flask.Flask(__name__)
import CONFIG

app = flask.Flask(__name__)
import CONFIG
app.secret_key = CONFIG.secret_key  # Should allow using session variables

###
# Pages
###

@app.route("/")
@app.route("/index")
def index():
  app.logger.debug("Main page entry")
  flask.session["key"] = secrets.dev_key
  flask.session["points"] = POI_list.process()

  return flask.render_template('index.html')


@app.errorhandler(404)
def page_not_found(error):
    app.logger.debug("Page not found")
    return flask.render_template('404.html'), 404

@app.errorhandler(403)
def page_forbidden(error):
    app.logger.debug("Forbidden")
    return flask.render_template('403.html'), 403

@app.errorhandler(500)
def server_bust(error):
    app.logger.debug("Server Error")
    return flask.render_template('500.html'), 500


if __name__ == "__main__":
    # Standalone.
    app.debug = True
    app.logger.setLevel(logging.DEBUG)
    print("Opening for global access on port {}".format(CONFIG.PORT))
    app.run(port=CONFIG.PORT, host="0.0.0.0")
else:
    # Running from cgi-bin or from gunicorn WSGI server,
    # which makes the call to app.run.  Gunicorn may invoke more than
    # one instance for concurrent service.
    app.debug=False