import numpy
import re
import sys

def read_text(file_name):
	file_object = open(file_name, "r")

	try:
		lines = file_object.readlines()
	finally:
		file_object.close()

	return lines


def main():
	#file_object = open("test.txt", "r")
	#try:
	#	lines = file_object.readlines()
	#finally:
	#	file_object.close()
	#i = 1;
	lines = read_text("test.txt")
	for line in lines:
		line = line.strip('\n')
		line = re.split(r'[\t]', line)
	#	print line.strip('\n')
	#	i = i + 1;
		print line
	

if __name__ == "__main__":
	main()