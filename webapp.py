from flask import Flask, url_for, render_template, request

app = Flask(__name__) 

@app.route("/")
def render_main():
     return render_template('home.html')

@app.route("/euro")
def render_main():
    return render_template('dollartoeuro.html')


@app.route("/response")
def render_response():
    euro = float(request.args['euro'])
    reply = euro*.85   
    return render_template('response.html', response = reply)
    
if __name__=="__main__":
    app.run(debug=False, port=54321)
    
@app.route("/sol")
def render_main():
    return render_template('dollartosol.html')

@app.route("/response")
def render_response():
    sol = float(request.args['sol'])
    reply = sol*3.26
    return render_template('response.html', response = reply)
    
if __name__=="__main__":
    app.run(debug=False, port=54321)
    
@app.route("/franc")
def render_main():
    return render_template('dollartofranc.html')

@app.route("/response")
def render_response():
    franc = float(request.args['franc'])
    reply = franc*.97
    return render_template('response.html', response = reply)
    
if __name__=="__main__":
    app.run(debug=False, port=54321)
