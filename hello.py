from flask import Flask, render_template
app = Flask(__name__)
@app.route('/login')
def home():
    return render_template('index.html')

@app.route('/login')
def home():
    return render_template('signup.html')





if __name__ == '__main__':
    app.run(debug=True)
