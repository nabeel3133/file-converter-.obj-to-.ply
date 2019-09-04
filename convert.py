#!/usr/bin/env python3
import argparse
import os

import d3.model.tools as mt
import functools as fc
from d3.model.basemodel import Vector

def PLYwithRGB(objFile, plyFile):
	fileToMake = plyFile[:len(plyFile)-4]
	fileToMake = fileToMake+"WithRGB.ply"

	objFileOpened = open(objFile,"r")
	plyFileOpened = open(plyFile,"r")
	fileToMake = open(fileToMake, "w")
	objFileData = []

	for line in objFileOpened:
		w = []
		w = line[:-1].split(' ')    #Splitting each line by space and putting in list

		if(len(w)==7):  #Checking if there are 7 elements in list
			#Removing the first 4 elements of list 
			w.remove(w[0])   
			w.remove(w[0])
			w.remove(w[0])
			w.remove(w[0])

			#Multiplying the remaining elements of list with 255 and converting to int
			w[0] = int(float(w[0])*255)
			w[1] = int(float(w[1])*255)
			w[2] = int(float(w[2])*255)

			objFileData.append(w)  #Appending list to objFile

		else:
			break

	objFileOpened.close()
	
	vertex_count = 0
	vertCounter = 0
	for line in plyFileOpened:
		vertCounter += 1
		if(vertCounter == 4):
			VertList = []
			VertList = line[:-1].split(' ')    #Splitting each line by space and putting in list
			vertex_count = int(VertList[2])
			break

	plyFileOpened.close()
	plyFileOpened = open(plyFile,"r")

	plyFileCounter = 0
	objDataCounter = 0
	for line in plyFileOpened:
		plyFileCounter += 1
		if(plyFileCounter <= 7):
			fileToMake.write(line)
		elif(plyFileCounter >= 8 and plyFileCounter <= 10):
			fileToMake.write('property uchar red\n')		
			fileToMake.write('property uchar green\n')		
			fileToMake.write('property uchar blue\n')
			fileToMake.write(line)
			plyFileCounter += 3
		elif(plyFileCounter >=11 and plyFileCounter <= 13):
			fileToMake.write(line)
		elif(plyFileCounter >= 14 and plyFileCounter <= vertex_count+13 and objDataCounter <= len(objFileData)-1):
			line = line.replace('\n','')
			fileToMake.write(line+" "+str(objFileData[objDataCounter][0])+" "+str(objFileData[objDataCounter][1])+" "+str(objFileData[objDataCounter][2])+"\n")
			objDataCounter += 1
		elif(plyFileCounter >= vertex_count+14):
			fileToMake.write(line)

	plyFileOpened.close()
	fileToMake.close()

def check_path(path, should_exist):
	""" Check that a path (file or folder) exists or not and return it.
	"""
	path = os.path.normpath(path)
	if should_exist != os.path.exists(path):
		msg = "path " + ("does not" if should_exist else "already") + " exist: " + path
		raise argparse.ArgumentTypeError(msg)
	return path

def main(args):

	if (args.from_up is None) != (args.to_up is None):
		raise Exception("from-up and to-up args should be both present or both absent")

	up_conversion = None
	if args.from_up is not None:
		up_conversion = (args.from_up, args.to_up)

	output = args.output if args.output is not None else '.' + args.type

	result = mt.convert(args.input, output, up_conversion)

	if args.output is None:
		print(result)
	else:
		with open(args.output, 'w') as f:
			f.write(result)

if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.set_defaults(func=main)
	parser.add_argument('-v', '--version', action='version', version='1.0')
	parser.add_argument('-i', '--input', metavar='input',
						type=fc.partial(check_path, should_exist=True),
						help='Input file')
	parser.add_argument('-o', '--output', metavar='output',
						help='Output path')
	parser.add_argument('-t', '--type', metavar='type',
						help='Export type, useless if output is specified')
	parser.add_argument('-fu', '--from-up', metavar='fup', default=None,
						help="Initial up vector")
	parser.add_argument('-tu', '--to-up', metavar='fup', default=None,
						help="Output up vector")
	args = parser.parse_args()
	args.func(args)

	objFile = args.input
	plyFile = args.output
	PLYwithRGB(objFile,plyFile)

