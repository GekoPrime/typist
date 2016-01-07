import sys
import string

def istitle(line):
	return set(line).issubset(set(' IVXLC\r\f\n')) and len(set(line).intersection(set('IVXLC'))) > 0

def isempty(line):
	return set(line).issubset(set(string.whitespace))

file = open(sys.argv[1])

lastline = ''
for line in file:
	if isempty(line):
		print ''
		continue
	if istitle(line):
		print 'I:' + line,
	elif istitle(lastline):
		print 'S:' + line,
	else:
		print ' :' + line,
	lastline = line
