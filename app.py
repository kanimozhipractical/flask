from flask import Flask ,render_template

app=Flask(__name__)

@app.route('/')

def home():
    return render_template('index.html')
# @app.route('/index')
# def index():
#     return '<h1> Welcome to home page</h1>'

# @app.route('/about')
# def about():
#     return '<h1> Welcome to ABOUT Page</h1> <p> this is  paragraph tag</p>'

# @app.route('/contact')
# def contact():
#     return '<h1> Welcome to CONTACT Page</h1> <p> contact us</p>'

# @app.route('/users/<name>')
# def users(name):
#     return '<h1> Welcome {} </h1>'.format(name[3])

if __name__=='__main__':
    app.run(debug=True)
