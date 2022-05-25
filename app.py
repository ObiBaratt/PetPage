from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', msg='Hello This is Roka\'s Homepage.')


@app.route('/snow')
def snow():
    return render_template('snow.html')


if __name__ == "__main__":
    app.run(debug=True)
