#!/usr/bin/env python3

from flask import Flask, render_template, request
from flask_babel import Babel, gettext, _, refresh


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

@babel.localeselector
def get_locale():
    """ get locale from request """
    locale = request.args.get('locale')
    if locale and locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])

@app.route('/', strict_slashes=False)
def home():
    """ home page """
    return render_template('4-index.html')
if __name__ == "__main__":
    app.run(debug=True)
