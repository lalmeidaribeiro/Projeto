from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")
    
@app.route('/listacursos')
def listacursos():
    return render_template("listacursos.html")
app.run()