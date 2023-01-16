from flask import Flask,render_template
import matplotlib.pyplot as plt
import numpy as np


app = Flask(__name__)

@app.route('/hi')
def matplotlib():
    x = np.linspace(0, 2 * np.pi, 200)
    y = np.sin(x)

    fig, ax = plt.subplots()
    ax.plot(x, y)
    return plt.show()

@app.route('/')
@app.route('/home')
def hello_world():
    return render_template('f1.html')

@app.route('/home/about/<username>')
def about_page(username):
     return f'<h1>This is the about page of {username}'

if __name__ == "__main__":
    app.run(debug=True)



