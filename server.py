import flask
from flasgger import Swagger

from api import say_hello


title = 'Say Hello API'

app = flask.Flask(__name__)
app.config['SWAGGER'] = {
    'title': title,
    'openapi': "3.0.0",
    "specs_route": "/"
}
swagger = Swagger(app, template_file='swagger.yaml')


@app.route('/health')
def health():
    return "ok"


@app.route('/say_hello', methods=['POST'])
def run_python():

    print(f"Handling request {flask.request}")

    # To read data
    name = flask.request.form.get('name')
    # To read files
    # filestr = flask.request.files['input'].read()

    if name is None:
        return flask.jsonify({'message': 'no name specified'}), 400

    return flask.jsonify({'message': say_hello(name)}), 200


if __name__ == "__main__":
    app.run(debug=False, port=8899, host='0.0.0.0')
