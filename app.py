from flask import Flask, render_template

from controllers.munro_controller import munros_blueprint
from controllers.region_controller import regions_blueprint


app = Flask(__name__)

app.register_blueprint(munros_blueprint)
app.register_blueprint(regions_blueprint)

@app.route("/")
def main():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
