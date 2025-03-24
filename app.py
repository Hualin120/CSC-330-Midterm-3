from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/fact/<name>')
def fact(name):
    Animal = {'dog': 'woof', 'cat': 'Meow', 'elephant': 'trumpet?'}
    if name in Animal:
        return f'{Animal.get(name)}'
    else:
        return "It's not in the dictionary."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
