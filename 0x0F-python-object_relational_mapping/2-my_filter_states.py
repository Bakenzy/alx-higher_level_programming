#!/usr/bin/python3
"""This script attempts to filer all the states to find the one
that meets a particular query"""
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
    cursor.execute("SELECT * FROM states\
    WHERE `name` LIKE '{:s}' ORDER BY `id` ASC".format(state))
    results = cursor.fetchall()
    cursor.close()
    db.close()
    for result in results:
        print(result)
