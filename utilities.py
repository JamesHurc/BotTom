import json

with open('config.json') as json_data_file: #Open the config json file
    data = json.load(json_data_file)


logLevel = data['logLevel']

def log(msg, level):
    if level >= logLevel:
    	if level == 1 or level == 2:
        	print("<LOG> : " + msg)
    	if level == 3:
    		print("<URGENT> : " + msg)