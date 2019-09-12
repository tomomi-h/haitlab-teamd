import re
import json
import os
import sqlite3
class Json():
	def __init__(self):
		self.file_list = []
		self.brand_set = set()
		self.file_db_query = []
		self.brand_db_query = []
		self.conn = sqlite3.connect('logoweb/db.sqlite3')
		self.c = self.conn.cursor()
	def json_to_db(self):
		FILE_PATH = os.getcwd()+"/logocrawl/logocrawl.txt"
		regex = re.compile(r'(\"https:\/\/worldvectorlogo\.com\/logo\/)((\d|\w)+)-((((\d|\w)|-)+))*\"')
		text = []
		f = open(FILE_PATH,"r")
		while True:
			line = f.readline()
			if not line: break
			text.append(line)
		f.close()
		for line in text:
			matchobj = regex.search(line)
			if not matchobj == None :
				print(matchobj.groups())
				brand_name = matchobj.group(2)
				if not matchobj.group(4) == None :
					file_name = matchobj.group(2)+"-"+matchobj.group(4)
				else:
					file_name = brand_name
				self.file_list.append(file_name)
				self.brand_set.add(brand_name)
				self.file_db_query.append((file_name,brand_name))
	def getFileList(self):
		return self.file_list
	def getBrandList(self):
		return self.brand_list
	def createDB(self): #do this once
		self.c.execute('''CREATE TABLE logobrand
			(key integer primary key autoincrement,
			brandname text)''')
		self.c.execute('''CREATE TABLE logofile 
			(key integer primary key autoincrement,
			filename text,
			brandname text,
			CONSTRAINT brand_file FOREIGN KEY(brandname)
			REFERENCES logobrand(brandname));
			''')
	def db_insert(self):
		print(self.brand_set)
		self.brand_db_query = list(self.brand_set)
		print(self.brand_db_query)
		for i in range(len(self.brand_db_query)):
			self.brand_db_query[i] = (self.brand_db_query[i],)
		print(self.brand_db_query)
		print(self.file_db_query)
		self.c.executemany('INSERT INTO logobrand(brandname) VALUES (?)', self.brand_db_query)
		self.c.executemany('INSERT INTO logofile(filename,brandname) VALUES(?,?)', self.file_db_query)
		for row in self.c.execute('SELECT * from logofile'):
			print(row)
		self.conn.commit()