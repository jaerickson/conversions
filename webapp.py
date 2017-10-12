from flask import Flask, url_for, render_template, request

app = Flask(__name__) 

@app.route("/")
def render_home():
     return render_template('home.html')

@app.route("/euro")
def render_euro():
    return render_template('dollartoeuro.html')


@app.route("/response")
def render_response():
    euro = float(request.args['euro'])
    reply = euro*.85   
    return render_template('responseeuro.html', response = reply)
    
if __name__=="__main__":
    app.run(debug=False, port=54321)
    
@app.route("/sol")
def render_sol():
    return render_template('dollartosol.html')

@app.route("/response")
def render_response():
    sol = float(request.args['sol'])
    reply = sol*3.26
    return render_template('responsesol.html', response = reply)
    
if __name__=="__main__":
    app.run(debug=False, port=54321)
    
@app.route("/franc")
def render_franc():
    return render_template('dollartofranc.html')

@app.route("/response")
def render_response():
    franc = float(request.args['franc'])
    reply = franc*.97
    return render_template('responsefranc.html', response = reply)
    
if __name__=="__main__":
    app.run(debug=False, port=54321)
