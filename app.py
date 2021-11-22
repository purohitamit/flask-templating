from flask import Flask, render_template

app = Flask(__name__)

@app.route('/ben/<letter>')
def ben(letter):
     return render_template('ben.html', users = ["ben", "harry", "bob", "jay", "matt", "bill"], letter = letter)

@app.route('/harry')
def harry():
    return render_template('harry.html')

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')