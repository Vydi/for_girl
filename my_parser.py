import sqlite3

conn = sqlite3.connect('post.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS tab_1 (id integer Primary key autoincrement, post text)''')
cursor.execute('''CREATE TABLE IF NOT EXISTS tab_2 (id integer Primary key autoincrement, sub text)''')


def parser_fun():
    import requests
    from bs4 import BeautifulSoup

    url = 'https://mysekret.ru/komplimenty/korotkie-komplimenty-devushke-150-fraz-kotorye-mozhno-napisat-v-sms-pod-foto-v-kommentarii.html'

    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    quotes = soup.find_all('ul', class_='subb')
    all_compliment = []
    for i in quotes:
        for p in i.findAll('li'):
            all_compliment.append(p.text)

    return all_compliment


def db_post():
    for i in parser_fun():
        cursor.execute('''INSERT INTO tab_1 (post) VALUES(?)''', (i,))
    conn.commit()
    print('Success post')


def post_for_tg():
    cursor.execute('''SELECT post FROM tab_1''')
    k = cursor.fetchall()
    all_posts = []
    for i in k:
        all_posts.append(i[0])
    return all_posts


def add_subb(user_id):
    cursor.execute('''SELECT sub FROM tab_2 WHERE sub = ?''', (user_id,))
    k = cursor.fetchall()
    if len(k) > 0:
        print('Уже есть в бд')
    else:
        cursor.execute('''INSERT INTO tab_2 (sub) VALUES(?)''', (user_id,))
        conn.commit()


def all_sub_f():
    all_sub = []
    cursor.execute('''SELECT sub FROM tab_2''')
    k = cursor.fetchall()
    for i in k:
        all_sub.append(i[0])
    return all_sub
# post_for_tg()
# db_post()
