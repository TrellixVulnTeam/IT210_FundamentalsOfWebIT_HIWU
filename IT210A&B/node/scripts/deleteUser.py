#!/usr/bin/python
import MySQLdb
import sys


db = MySQLdb.connect(
		host = "192.168.12.136",  #your host, usually localhost
		user = "myusername",		#your db username
		passwd = "123456",		#your db password
		db = "it210b")				#the db you want to connect to.

#You need to create a Cursor Object. 
#It lets you execute your queries.

cursor = db.cursor()

#Use all the SQL you want
cursor.execute("DELETE FROM users WHERE userName = '" + sys.argv[1] + "'")
db.commit()

db.close()
