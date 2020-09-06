from flask_frozen import Freezer
from server import app

# https://medium.com/@francescaguiducci/how-to-build-a-simple-personal-website-with-python-flask-and-netlify-d800c97c283d
freezer = Freezer(app)

if __name__ == '__main__':
    freezer.freeze()