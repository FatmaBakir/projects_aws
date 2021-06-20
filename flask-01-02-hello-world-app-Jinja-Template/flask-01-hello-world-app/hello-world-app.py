from flask import Flask

app = Flask( __name__)


@app.route("/")
def head():
    return "Hello World! I love FLASK!!"

@app.route("/second")
def second():
    return "This is the second page! I'm still loving Flask!"

@app.route("/third")
def third():
    return "This is my third page! Aaand, I am loving Flask even more!!"

@app.route("/third/subthird")
def subthird():
    return "This is the sub-page of third page!"

@app.route("/forth/<string:id>")
def forth(id):
    return f"ID of this page is {id}"



if __name__ == "__main__":
    app.run(debug=True)
