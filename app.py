from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def start():
    return render_template('start.html')

@app.route('/home')
def home():
    return render_template('home.html')

import os

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))  # Renderが指定するPORTを取得
    app.run(host='0.0.0.0', port=port, debug=True)
