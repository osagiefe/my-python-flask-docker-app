from flask import Flask,render_template
app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to cloud computing page"

@app.route("/thanks")
def instructor():
    instructor="Mr. Ayenco Scolfield"
    emailaddress="ayeniayokunle@gmail.com"
    return render_template('thanks.html',instructor=instructor, emailaddress=emailaddress)



if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8081, debug=True)