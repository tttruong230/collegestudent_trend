from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/colleges")
def colleges():
  return render_template("colleges.html")

@app.route("/locations")
def locations():
  return render_template("locations.html")

@app.route("/statistics")
def stats():
  return render_template("statistics.html")

@app.route("/testscores")
def testscores():
  return render_template("testscores.html")

@app.route("/analysis")
def analysis():
  return render_template("analysis.html")

@app.route("/majors")
def majors():
  return render_template("major.html")

@app.route("/interests")
def interests():
  return render_template("interests.html")

@app.route("/otherfactors")
def otherfactors():
  return render_template("otherfactors.html")

@app.route("/html")
def static_page():
  return render_template("index.html")

if __name__== "__main__":
    app.run()