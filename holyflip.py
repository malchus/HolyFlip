from flask import Flask
from flask import render_template
import verse
from verse import Vget


app = Flask(__name__)


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
    return (v)






