from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>This is my example Flask app</h1>"

@app.route('/about')
def about_page():
    return "<h1>This is a very interesting ABOUT page</h1>"

@app.route('/about/v2')
def about_v2_page():
    return "<h1>This is a very interesting ABOUT page?</h1>"

@app.route('/hello/<name>')
def hello_name(name):
    return f'Hello {name}!'

if __name__ == '__main__':
    app.run(debug=True, port=8181)
