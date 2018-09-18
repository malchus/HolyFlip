import mysql.connector
import random
import json
import bible

db = mysql.connector.connect(host="localhost",
user="root", passwd="Jammer12", db="BibleDiscovery")


def randomV():
    rcursor = db.cursor()
    trans = 'kjv'
    randombook = random.choice(bible.books)

    sql = ("SELECT chapter,count(chapter) FROM BibleDiscovery.scripture" +
        " WHERE trans = %s AND bookname = %s group by chapter")
    rcursor.execute(sql, (trans, randombook))
    rv = rcursor.fetchall()
    payload = []
    content = {}
    for result in rv:
        content = {'cnum': result[0], 'vnum': result[1]}
        payload.append(content)
        content = {}
    randomchapter = random.choice(payload)
    randomverse = random.randint(1, randomchapter["vnum"])
    return Vget(trans, randombook, str(randomchapter["cnum"]), str(randomverse))


def Vget(trans, book, chapter, verse):
    mycursor = db.cursor()
    sql = ("SELECT bookname, chapter,verse,text" +
        " FROM BibleDiscovery.scripture WHERE trans = %s " +
        "AND bookname = %s AND chapter=%s AND verse=%s ")
    mycursor.execute(sql, (trans, book, chapter, verse))
    rv = mycursor.fetchall()
    payload = []
    content = {}
    for result in rv:
        content = {'bookname': result[0], 'chapter': result[1],
            'verse': result[2], 'text': result[3]}
        payload.append(content)
        content = {}
    return (json.dumps(payload))

