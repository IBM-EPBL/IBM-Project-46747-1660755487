from flask import Flask

app=Flask(__name__)

@app.route('/')
@app.route('/lakshmi')
def home():
    return"Hello Lakshmi!"

if __name__=="__main__":
    app.run(debug=True)