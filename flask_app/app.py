from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('hello.html')

@app.route('/greet')
def greet():
    return render_template('form.html')

if __name__ == '__main__':
    app.run(debug=True)
