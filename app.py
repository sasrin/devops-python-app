from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, DevOps!"

if __name__ == "_main_":
    # Run the app on 0.0.0.0 to make it accessible outside the container
    app.run(host='0.0.0.0', port=5000)