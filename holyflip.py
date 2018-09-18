from flask import Flask
from flask import render_template
import mysql.connector
import json
import random
import bible
import verse

db = mysql.connector.connect(host="localhost",
user="root", passwd="Jammer12", db="BibleDiscovery")


app = Flask(__name__)


@app.route('/')
def hello_world():
    statement = {'say': 'sup girl'}
    return render_template('holyflip.html', statement=statement)


@app.route('/api/verse/<trans>/<book>/<chapter>/<verse>')
def verse(trans, book, chapter, verse):
    mycursor = db.cursor()
    sql = "SELECT bookname, chapter,verse,text FROM BibleDiscovery.scripture WHERE trans = %s AND bookname = %s AND chapter=%s AND verse=%s "
    mycursor.execute(sql, (trans, book, chapter, verse))
    rv = mycursor.fetchall()
    payload = []
    content = {}
    for result in rv:
        content = {'bookname': result[0], 'chapter': result[1], 'verse': result[2], 'text': result[3]}
        payload.append(content)
        content = {}
    return (json.dumps(payload))


@app.route('/modtest')
def modtest():
    return randomverse()


def randomverse():
    rcursor = db.cursor()
    trans='kjv'
    randombook = random.choice(bible.books)
   
    sql = "SELECT chapter,count(chapter) FROM BibleDiscovery.scripture WHERE trans = %s AND bookname = %s group by chapter"
    rcursor.execute(sql,(trans,randombook))
    rv=rcursor.fetchall()
    payload=[]
    content = {}
    for result in rv:
        content = {'cnum':result[0],'vnum':result[1]}

        payload.append(content)
        content={}
    randomchapter= random.choice(payload)

    randomverse = random.randint(1,randomchapter["vnum"])
  
    return("{} {}:{}".format(randombook, str(randomchapter["cnum"]), str(randomverse)))



