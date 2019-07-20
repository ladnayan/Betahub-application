import pymysql
def data_base_load():              #new
    db=pymysql.connect('localhost','nayan','1234','user_database')
    cursor=db.cursor()
    data_base={}
    sql='select*from data;'
    cursor.execute(sql)
    result=list(cursor.fetchall())
    for i in result:
        data_base[i[1]]=[i[0],i[2],i[3],i[4]]
    db.close()
    return(data_base)
