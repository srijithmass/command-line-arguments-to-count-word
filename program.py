'''
python program for getting the word count from the contents of a file using command line arguments.
Develpoed By: SRIJITH R
RegisterNumber: 21004191
'''
# in python file "program.py"

import sys
f1=open(sys.argv[1])
data=f1.read()
word=data.split()
print("The word count is",len(word))
f1.close()