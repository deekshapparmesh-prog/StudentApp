from flask import Flask

app = Flask(__name__)


# Function for calculating total marks
def calculate_total(marks):
    return sum(marks)


# Flask home page
@app.route("/")
def home():
    return "Welcome to Student Management System!"


if __name__ == "__main__":
    app.run(debug=True)