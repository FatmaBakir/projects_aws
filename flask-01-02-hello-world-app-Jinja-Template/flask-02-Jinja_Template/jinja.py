from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def head():
    return render_template("index.html", number1 = 20, number2 = 40)

@app.route("/sum")
def sum():
    var1, var2 = 23, 45
    return render_template("body.html", num1 = var1, num2 = var2, num3 = var1 + var2)

if __name__ == "__main__":
    # app.run(debug=True)
    app.run(host="0.0.0.0", port=80)