from flask import Flask, render_template, redirect, request, make_response
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('base.html')

app.run(debug=True)