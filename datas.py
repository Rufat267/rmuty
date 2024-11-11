import sqlite3

db = sqlite3.connect('foods.db')
db_user = sqlite3.connect("users.db")
cursor = db.cursor()
cursor_user = db_user.cursor()

async def start_db():
    cursor.execute('''
CREATE TABLE IF NOT EXISTS foods(
                   type TEXT,
                   price TEXT,
                   name TEXT,
                   photo TEXT,
                   ingridients TEXT)

''')
async def start_user_db():
    cursor_user.execute('''
CREATE TABLE IF NOT EXISTS users(
                   name TEXT,
                   phone_num INTEGER,
                   id INTEGER)

''')

async def add_to_db(type,price,name,photo,ingri):
    cursor.execute('''
INSERT INTO foods(type,price,name,photo,ingridients)
                   VALUES(?,?,?,?,?)
''',(type,price,name,photo,ingri)
    )
    db.commit()




async def show_foods():
    cursor.execute('SELECT * FROM foods')
    datas = cursor.fetchall()
    return datas

async def add_to_user_db(name,phone_num,id):
    cursor_user.execute('''
INSERT INTO users(name,phone_num,id)
                   VALUES(?,?,?)''',
    (name,phone_num,id)
    )
    db_user.commit()

     


