import sqlite3

conn = sqlite3.connect("disease2.db")
cur = conn.cursor()

organ_list=[]


with conn:
    organ_list = cur.execute("SELECT name FROM sqlite_master WHERE type = 'table';").fetchall()
    #print(organ_list)

    for organ in range(3,195):
        print(organ_list[organ][0])
        str = "DELETE FROM [" + organ_list[organ][0] + "]"
        print(str)
        print(organ)
        cur.execute(str)
        str2 = "INSERT INTO [" + organ_list[organ][0] + "] (id, symtom) SELECT id, symptom FROM disease WHERE organs LIKE '%" + organ_list[organ][0] +"%'"
        print(str2)
        cur.execute(str2)


    #st = cur.execute("SELECT organs FROM disease WHERE organs LIKE (?)", ('%가슴%',)).fetchall()
    #print(st)
