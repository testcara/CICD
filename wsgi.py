import os
import sys


sys.path.append(os.getcwd())
from app import create_app


application = create_app()

if __name__ == '__main__':
#	print "I am running run"
	application.run()
#	print "I am failed"

