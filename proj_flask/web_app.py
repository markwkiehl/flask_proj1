#web_app.py

from flask import jsonify, request, render_template, redirect, url_for

from proj_flask import app

# define a navigation bar
#pip install Flask-Navigation
#https://flask-navigation.readthedocs.io/en/latest/
from flask_navigation import Navigation
nav = Navigation()
nav.init_app(app)
nav.Bar('top', [
    nav.Item('Home', 'index'),
    nav.Item('Posts', 'url_posts'),
    nav.Item('Redirect', 'url_redirect'),
    nav.Item('URL Query', 'url_query', {'scope': 'USA'}),
    nav.Item('JSON', 'url_json'),
    nav.Item('Static', 'url_static'),
    nav.Item('XML', 'url_xml'),
])

# Get the content from topics.xml file
from proj_flask.class_xml_topics import XmlTopics
import os
basedir = os.path.abspath(os.path.dirname(__file__))
class_file_path = os.path.join(basedir, 'static/xml/topics.xml')

data_json = {
    "chartData": {
        "labels": [
        "sunday",
        "monday",
        "tuesday",
        "wednesday",
        "thursday",
        "friday",
        "saturday"
        ],
    "thisWeek": [
        20000,
        14000,
        12000,
        15000,
        18000,
        19000,
        22000
        ]
    }
}

site = {'sitename': 'SavvyFlaskSolutions'}

@app.route('/')
def index():
    return render_template('index.html', site=site, menu='home')

@app.route('/xml', methods=['GET'])
def url_xml():
    c_topics = XmlTopics(class_file_path)
    topics_all = c_topics.get()
    if request.args.get('topic') == None:
        topics = None
    else:
        topics = c_topics.get(request.args.get('topic'))
    return render_template('xml.html', site=site, topics=topics, topics_all=topics_all)

@app.route('/posts')
def url_posts():
    user = {'username': 'Mark'}
    posts = [
        {
            'author': {'username': 'John'},
            'month': 'Jan',
            'year': '2020',
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'month': 'Dec',
            'year': '2019',
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('posts.html', site=site, menu='posts', user=user, posts=posts)


@app.route('/redirect')
def url_redirect():
    return redirect('/redirected')

@app.route('/redirected')
def redirected():
    return render_template('redirect.html')


@app.route('/url_query', methods=['GET'])
def url_query():
    scope = request.args.get('scope', 'unspecified')
    msg = 'url_query scope = {scope}'
    return msg, 200, {'Content-Type': 'text/plain; charset=utf-8'}


@app.route('/json')
def url_json():
    #return jsonify(data_json)
    return render_template('json.html', name=data_json)


@app.route('/static')
def url_static():
    file_include = 'sample-html-elements.html'
    return render_template('static.html', file_include=file_include)


# ----------- under development ..

@app.route("/chart")
def chart_form():
    #return render_template('chart.html')
    return render_template('chart-ajax.html')


@app.route("/chart-handler", methods=['POST']) 
def chart_post():
    return jsonify(data_json)


@app.route('/hello', methods=['GET', 'POST'])
def hello():
    # POST request
    if request.method == 'POST':
        print('Incoming..')
        print(request.get_json())  # parse as JSON
        return 'OK', 200

    # GET request
    else:
        message = {'greeting':'GET from ' + __name__}
        return jsonify(message)  # serialize and use JSON headers


#test_request_context() tells Flask to behave as though it’s handling a request even while we use a Python shell.
#with app.test_request_context():
#    print('url_for(json) = ', url_for('json'))


# to allow for debugging and auto-reload
if __name__ == "__main__":
    app.run(host="0.0.0.0",port=8000,debug=True)
