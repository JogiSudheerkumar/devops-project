from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello from Sudheer! I'm learning DevOps!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
if __name__ == "__main__":
    app.run(debug=True)
