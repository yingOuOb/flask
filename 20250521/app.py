from flask import Flask
from blue import blueprint
app = Flask(__name__)
app.register_blueprint(blueprint)

app.run()