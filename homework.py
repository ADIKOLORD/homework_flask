from flask import Flask, render_template

web = Flask(__name__)

@web.route('/')
def main_page():
    return render_template('index.html')