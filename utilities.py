logLevel = 1

def log(msg, level):
    if level >= logLevel:
    	if level == 1 or level == 2:
        	print("<LOG> : " + msg)
    	if level == 3:
    		print("<URGENT> : " + msg)