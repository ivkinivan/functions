from flask import Flask, render_template


app = Flask(__name__)
app.debug = True


@app.route("/")
def index():
    return render_template('project.html')

@app.route("/line_func")
def line_func():
    return render_template('line_func.html')

@app.route("/exponential_func")
def exponential_func():
    return render_template('exponential_func.html')

@app.route("/fractional_linear_func")
def fractional_linear_func():
    return render_template('fractional_linear_func.html')

@app.route("/power_func")
def power_func():
    return render_template('power_func.html')

@app.route("/quadratic_func")
def quadratic_func():
    return render_template('quadratic_func.html')

@app.route("/trigonometric_func")
def trigonometric_func():
    return render_template('trigonometric_func.html')