from flask import Flask

app = Flask(__name__)


@app.route('/')
def test():
    return 'zebra mussel detected!!'


if __name__ == '__main__':
    app.run()
