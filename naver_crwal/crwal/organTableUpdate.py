import sqlite3

conn = sqlite3.connect("disease2.db")
cur = conn.cursor()
m = Mecab()

with conn:
    organ_list = cur.execute("SELECT name FROM sqlite_master WHERE type = 'table';").fetchall()
    print(organ_list)

    for organ in range(4,195):
        key=0
        sql_str = "SELECT symtom FROM [" + organ_list[organ][0] + "]"
        sql_keys = "SELECT id FROM [" + organ_list[organ][0] + "]"

        symptom = cur.execute(sql_str).fetchall()
        keys = cur.execute(sql_keys).fetchall()
        for symtom in range(0, len(symptom)):
            if symptom[symtom][0]!=None:
                text=symptom[symtom][0]
                sql_str =  m.nouns(text)
                sql_udt= "UPDATE [" + organ_list[organ][0] + "] SET symtom = (?) where id = (?)"
                cur.execute(sql_udt,(",".join(m.nouns(text)),keys[key][0],))
                print(m.nouns(text))
            key+=1
'''
t=0
for row in cur.execute('SELECT id FROM [심장] '):
    i = row[0]
    t +=1
    cur2.execute('UPDATE [심장] SET name= (?) WHERE id= (?)', (t,i,))
'''