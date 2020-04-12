from flask import Flask, request, render_template, url_for

app = Flask(__name__)


@app.route('/')
def content():
    data = [
        {
            'name' : 'tiger',
            'url' : url_for('static', filename='img/tiger.jpg')
        },
        {
            'name' : 'lion',
            'url' : url_for('static', filename='img/lion.jpg')
        },
        {
            'name' : 'cat',
            'url' : url_for('static', filename='img/cat.jpg')
        },
        {
            'name' : 'pig',
            'url' : url_for('static', filename='img/pig.jpg')
        },
        {
            'name' : 'dog',
            'url' : url_for('static', filename='img/dog.jpg')
        }
    ]
    return render_template('content.html', items=data)

@app.route('/about')
def about():
    return render_template('about.html')

app.run()