from flask import Flask

app = Flask(__name__)


app.config['SECRET_KEY'] = 'cdyXU_wvqFLE9hMfsFwKFA'

from flaskapp import routes