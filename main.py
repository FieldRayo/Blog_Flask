from myblog import app

@app.route('/')
def index():
    return '<h1>Hdsello World!</h1>'

if __name__ == "__main__":
    app.run()