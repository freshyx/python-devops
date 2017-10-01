#!/usr/bin/env python
import difflib
import sys

try:
	baseFile = sys.argv[0]
	txtFile1 = sys.argv[1]
	txtFile2 = sys.argv[2]
except Exception,e:
	print "Error:" + str(e)
	print "Usage:" + baseFile + " diffFile.py filename1 filename2"
	sys.exit()

def readFile(filename):
	try:
		fileHandle = open(filename,'rb')
		text = fileHandle.read().splitlines()
		return text
	except IOError as error:
		print('Read file Error:' + str(error))
		sys.exit()
	finally:
		fileHandle.close()

if txtFile1 == "" or txtFile2 == "":
	print "Usage:" + baseFile + " diffFile.py filename1 filename2"
	sys.exit()

text1_lines = readFile(txtFile1)
text2_lines = readFile(txtFile2)

d = difflib.HtmlDiff()
print d.make_file(text1_lines,text2_lines)
