from flask import Flask, render_template, request


def create_app():
    app = Flask(__name__)

    app.config.from_pyfile('settings.py')

    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/json', methods=['GET'])
    def get_json():
        return {'data': {'k': 'v'}}

    @app.route('/web_page_title', methods=['POST'])
    def get_web_page_title():
        url = request.json.get('url')
        try:
            import re
            import requests
            response = requests.get(url)
            match = re.search(r'<title>(?P<title>.+)</title>', response.text, re.MULTILINE)
            if match:
                return {'title': match.group('title')}
            else:
                return {'err': 'can not get the web page title.'}
        except BaseException as e:
            return {'err': str(e)}

    return app


if __name__ == '__main__':
    create_app().run(debug=True)
