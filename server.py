# pip is a package manager for for python (like npm is for javascript)

# sudo easy_install pip
# pip install flask
from flask import Flask, render_template, request

from forms import SignUpForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'myTestKey'

@app.route('/')
def home():
    return 'hello world'

@app.route('/about')
def about():
    # templates
    # jinja is passing in variables from here

    fruits = [
        {
            "name": "apple", 
            "cost": 50
        }, 
        {
            "name": "banana", 
            "cost": 25
        },
        {
            "name": "pear", 
            "cost": 30
        }
    ]
    return render_template('about.html', author="Brandon", sunny=False, fruits=fruits)

@app.route('/blog/<int:blog_id>')
def blogpost(blog_id):
    return 'this is blog post number ' + str(blog_id)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignUpForm()
    if form.is_submitted():
        result = request.form
        return render_template('user.html', result=result)
    return render_template('signup.html', form=form)

if __name__ == '__main__':
    app.run() 