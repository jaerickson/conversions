from flask import Flask, url_for, render_template, request

app = Flask(__name__) 

@app.route("/")
def render_home():
     return render_template('home.html')

@app.route("/e")
def render_euro():
    return render_template('dollartoeuro.html')


@app.route("/responseeuro.html")
def render_responseeuro():
    euro = float(request.args['euro'])
    reply = euro*.85   
    return render_template('responseeuro.html', response = reply)
    
if __name__=="__euro__":
    app.run(debug=False, port=54321)
    
@app.route("/s")
def render_sol():
    return render_template('dollartosol.html')

@app.route("/responsesol")
def render_responsesol():
    sol = float(request.args['sol'])
    reply = sol*3.26
    return render_template('responsesol.html', response = reply)
    
if __name__=="__sol__":
    app.run(debug=False, port=54321)
    
@app.route("/f")
def render_franc():
    return render_template('dollartofranc.html')

@app.route("/responsefranc")
def render_responsefranc():
    franc = float(request.args['franc'])
    reply = franc*.97
    return render_template('responsefranc.html', response = reply)
    
if __name__=="__franc__":
    app.run(debug=False, port=54321)
