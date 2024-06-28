#!/usr/bin/python3
"""The script handles an SQL injection in tryng to filter all
the states that have a given name and stop malicious attacks"""
import MySQLdb
import sys
if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state = sys.argv[4]
    db = MySQLdb.connect(host="localhost", user=username, password=password,
                         database=database, port=3306)
    cursor = db.cursor()
    cursor.execute('SELECT * FROM states WHERE `name` = %(name)s\
            ORDER BY `id` ASC', {'name': state})
    results = cursor.fetchall()
    cursor.close()
    db.close()
    for result in results:
        print(result)
