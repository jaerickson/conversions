from flask import Flask, url_for, render_template, request

app = Flask(__name__) 

@app.route("/")
def render_main():
    return render_template('dollartoeuro.html')

@app.route("/response")
def render_response():
    euro = float(request.args['euro'])
    reply = euro*.85   
    return render_template('response.html', response = reply)
    
if __name__=="__main__":
    app.run(debug=False, port=54321)
