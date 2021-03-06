import os

from flask import Flask, render_template

app = Flask(__name__)
app.debug = True

# env = Environment(
#     loader=PackageLoader(__name__, 'templates'),
#     autoescape=select_autoescape(['html', 'xml'])
# )

@app.route('/')
def index():
    return render_template("index.html", menuActive="index")

@app.route('/sobre')
def sobre():
    return render_template('sobre.html', menuActive="about")

@app.route('/blog')
def blog():
    return render_template('blog.html')

@app.route('/contato')
def contato():
    return render_template('contato.html', menuActive="contact")

@app.route('/servicos')
def servicos():
    return render_template('servicos.html', menuActive="services")

if __name__ == '__main__':
    app.run(host='0.0.0.0')
