from flask import Flask
from flask_dance.contrib.twitter import make_twitter_blueprint,twitter
from flask import render_template
import verse
from verse import Vget
import json


app = Flask(__name__)
app.config['SECRET_KEY'] = 'something'

@app.route('/')
def index():
    statement = {'say': 'sup girl'}
    return render_template('holyflip.html', statement=statement)


@app.route('/flip')
def flip():
    return verse.randomV()


@app.route('/api/verse/<trans>/<book>/<chapter>/<verse>')
def verseget(trans, book, chapter, verse):
    v = Vget(trans, book, chapter, verse)
    return json.dumps(v)



if __name__ == '__main__':
		app.run(debug=True)


