from flask import Flask, redirect, url_for
from flask_dance.contrib.twitter import make_twitter_blueprint,twitter
from flask import render_template
import verse
from verse import Vget
import json


app = Flask(__name__)
app.config['SECRET_KEY'] = 'something'

twitter_blueprint = make_twitter_blueprint( api_key='FdRZkTGFZmqMyr5W3iiBBPLjS', api_secret='GZ0Ead9Pn3CAQPW6KkiNOtZcKoYWf5DnZkTMqHjDuf9AQ0pw5X')

app.register_blueprint(twitter_blueprint, url_prefix="/login")

@app.route("/")
def index():
    if not twitter.authorized:
        return redirect(url_for("twitter.login"))
    resp = twitter.get("account/settings.json")
    assert resp.ok
    return "You are @{screen_name} on Twitter".format(screen_name=resp.json()["screen_name"])



@app.route('/holyflip')
def indexflip():
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


