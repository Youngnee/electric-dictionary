"""
name: insert_word
插入词典
"""
import pymysql

f = open("dict.txt")
connfd = pymysql.connect("localhost", "root",
                         "123456", "elec_dic")
cursor = connfd.cursor()

for line in f:
    tmp = line.split(" ")
    word = tmp[0]  # 获取单词
    mean = " ".join(tmp[1:]).strip()

    sql = 'insert into words (word,mean) VALUES ("%s", "%s")' % (word, mean)

    try:
        cursor.execute(sql)
        connfd.commit()
    except Exception as e:
        connfd.rollback()
f.close()
