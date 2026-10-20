import math
from flask import Flask, render_template,request
 
app=Flask(__name__)
 
@app.route('/')
def index():
    titulo="PWA"
    lista=["pedro","Luis","Pablo"]
    return render_template("index.html",titulo=titulo,lista=lista)
 
@app.route("/operasBas", methods=["GET", "POST"])
def operasBas(): 
    n1 = 0
    n2 = 0
    res = 0
    operacion = 'sumar'
    if request.method == 'POST':
        n1 = float(request.form['n1'])
        n2 = float(request.form['n2'])
        operacion = request.form['operacion']
        
        if operacion == 'sumar':
            res = n1 + n2
        elif operacion == 'restar':
            res = n1 - n2
        elif operacion == 'multiplicar':
            res = n1 * n2
            
    return render_template("operasBas.html", n1=n1, n2=n2, res=res, operacion=operacion)
 
@app.route("/distancia", methods=["GET", "POST"])
def distancia():
    x1 = y1 = x2 = y2 = distancia = 0
    
    if request.method == 'POST':
        x1 = float(request.form['x1'])
        y1 = float(request.form['y1'])
        x2 = float(request.form['x2'])
        y2 = float(request.form['y2'])
        
        distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
        
    return render_template("distancia.html", x1=x1, y1=y1, x2=x2, y2=y2, distancia=distancia)
 
@app.route("/hola")
def func():
    return "Hola..."
 
@app.route("/user/<string:user>")
def user(user):
    return "Hola: "+user
 
@app.route("/numero/<int:n>")
def numero(n):
    return "Numero: {}".format(n)
 
@app.route("/user/<int:id>/<string:username>")
def username(id,username):
    return "ID: {} nombre: {}".format(id,username)
 
@app.route("/suma/<float:n1>/<float:n2>")
def suma(n1,n2):
    return "la suma es: {}".format(n1+n2)
 
 
if __name__=="__main__":
    app.run(debug=True)