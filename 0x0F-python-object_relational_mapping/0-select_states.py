#!/usr/bin/python3
# Lists all states from the database hbtn_0e_0_usa.
# Usage: ./0-select_states.py <mysql username> \
#                             <mysql password> \
#                             <database name>
if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    connection = MySQLdb.connect("localhost", argv[1], argv[2], argv[3])
    cursor = connection.cursor()
    command = """SELECT * FROM states
                ORDER BY states.id ASC"""
    cursor.execute(command)
    data = cursor.fetchall()
    for row in data:
        print(row)
    connection.close()
