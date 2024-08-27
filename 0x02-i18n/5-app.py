#!/usr/bin/env python3

from flask import Flask, render_template, request, g
from flask_babel import Babel, gettext, _, refresh


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

class Config:
    """ configuration settings for babel """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"

refresh()
app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)
refresh()

def get_user():
    """ get user's dic if found """
    user = request.args.get('login_as')
    if not user:
        return None
    return users.get(int(user))

@app.before_request
def before_request():
    """ handles user login """
    user = get_user()
    g.user =  user

@babel.localeselector
def get_locale():
    """ get locale from request """
    locale = request.args.get('locale')
    if locale and locale in app.config['LANGUAGES']:
        return locale
    if g.user and g.user.get('locale') in app.config['LANGUAGES']:
        return g.user.get('locale')

    return request.accept_languages.best_match(app.config['LANGUAGES'])

@app.route('/', strict_slashes=False)
def home():
    """ home page """
    return render_template('5-index.html',
            name=g.user.get('name') if g.user else None)
if __name__ == "__main__":
    app.run(debug=True)
