#coding=utf-8
import psycopg2
def select_banco_str(sql):
    con = psycopg2.connect(host= 'localhost',
                    database= 'chaves',
                    user= 'postgres',
                    password= '123456789') 
    cur = con.cursor()
    cur.execute(sql)
    recset = cur.fetchall()
    return recset
    con.close()    
texto = 'André Silva'
sql = '''select * from usuarios where nome = '%s' ''' % (texto)
ret = select_banco_str(sql)
for s in ret:
    print s[1].decode('UTF-8')