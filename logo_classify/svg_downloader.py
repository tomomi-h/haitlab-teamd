import json_to_db
import os
from requests import get
import cairosvg
PATH = os.getcwd()+"/res/"
def printProgress (iteration, total, prefix = '', suffix = '', decimals = 1, barLength = 100):
	formatStr = "{0:." + str(decimals) + "f}"
	percent = formatStr.format(100 * (iteration / float(total)))
	filledLength = int(round(barLength * iteration / float(total)))
	bar = '#' * filledLength + '-' * (barLength - filledLength)
	sys.stdout.write('\r%s |%s| %s%s %s' % (prefix, bar, percent, '%', suffix)),
	if iteration == total:
		sys.stdout.write('\n')
	sys.stdout.flush()

if __name__ == '__main__':
	db = json_to_db.Json()
	#db.createDB() #Only Once
	db.json_to_db()
	db.db_insert()
	print(db.file_list)
	for filepath in db.file_list:
		url = "https://worldvectorlogo.com/download/"+filepath+".svg"
		print(url)
		with open(PATH+filepath+".svg", "wb") as file:
			response = get(url)
			file.write(response.content)
		path = os.getcwd()+"/res/"
		file_name = filepath
		cairosvg.svg2png(url=path+file_name+".svg", 
                		write_to=path+file_name+".png", 
                		dpi = 100
               			)

