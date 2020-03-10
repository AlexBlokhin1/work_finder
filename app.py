from flask import Flask, render_template
import responder
from flask_cors import CORS

ALLOWED_HOSTS = {r"/":    {"origins": "*"}}

app = Flask(__name__, static_folder='static/')

cors = CORS(app, resources=ALLOWED_HOSTS)

api = responder.API(allowed_hosts=[])
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route("/", methods=['post', 'get'])
def home():
    return 'its working'


if __name__ == "__main__":
    app.run(host='0.0.0.0')
