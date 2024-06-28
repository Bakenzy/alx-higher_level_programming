#!/usr/bin/python3
"""This script pritns out all the states
in the database which begines with an N"""
import MySQLdb
import sys
if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    db = MySQLdb.connect(host="localhost", user=username,
                         password=password, database=database, port=3306)
    cursor = db.cursor()
    cursor.execute('SELECT * FROM states ORDER BY `id` ASC')
    results = cursor.fetchall()
    cursor.close()
    db.close()
    for result in results:
        if result[1][0] == "N":
            print(result)
