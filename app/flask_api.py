from flask import Flask
from flask_restful import Api
from resources.health import HealthCheck
from waitress import serve


# flask app
app = Flask(__name__)

# disable slash trailing
app.url_map.strict_slashes = False

api = Api(app)

api.add_resource(HealthCheck, "/personal-app/health")

if __name__ == "main":
    #serve(app, host="0.0.0.0", port=5000)
    app.run(debug=True, host="localhost", port=5000)
