from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")
    
@app.route('/Contato')
def Contato():
    return render_template("Contato.html")

@app.route('/DetalheCurso')
def DetalheCurso():
    return render_template("DetalheCurso.html")

@app.route('/Disciplina')
def Disciplina():
    return render_template("Disciplina.html")

@app.route('/ListaCursos')
def ListaCursos():
    return render_template("ListaCursos.html")
   
@app.route('/Login')
def Login():
    return render_template("Login.html")

@app.route('/Noticias')
def Noticias():
    return render_template("Noticias.html")
     
app.run()