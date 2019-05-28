import sqlite3

conn = sqlite3.connect("disease2.db")
cur = conn.cursor()
cur.execute("SELECT * from disease")


counter={} #각 단어 카운팅
temp={} # 하나의 레코드에서 중복된 단어 처리를 위한 딕셔너리


for row in cur.execute('SELECT symtom FROM [심장] '):
    if row[0]==None:
        continue
    for r in row[0].split(','):
        r=r.strip()
        if temp.get(r,False)==False: 
            #레코드에서 아직 카운팅이 안된 단어
            temp[r] = True
            counter[r] = counter.get(r,0) + 1
    temp={}

counter_sorted_keys = sorted(counter, key=counter.get, reverse=True)
sorted_counter={}
cnt=0
for r in counter_sorted_keys:
    print (r, counter[r])
    sorted_counter[r]=counter[r]
    cnt+=1
    if(cnt>20):
         break
