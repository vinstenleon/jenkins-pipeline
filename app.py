from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template('static.html')  # render a template
    
if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
