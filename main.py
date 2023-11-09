from flask import Flask, render_template

app = Flask(__name__)

print(__name__)
print(app)

# PYTHON DECORATORS
# def decorator(function):
    # def wrapper_function():
        # function()
   #  return wrapper_function



@app.route("/")
# @decorator
def hello():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
