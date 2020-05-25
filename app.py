from flask import Flask, render_template


def create_app():
    app = Flask(__name__)

    app.config.from_pyfile('settings.py')

    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/json', methods=['GET'])
    def get_json():
        return {'data': {'k': 'v'}}

    return app


if __name__ == '__main__':
    create_app().run(debug=True)
