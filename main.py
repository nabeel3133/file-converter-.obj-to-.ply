import argparse
from converter import Converter

def main(args):

	objFile = Converter(args.input)	
	objFile.GetVertsAndTri()
	objFile.write_ply(args.output)

if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument('-i', '--input', default='./sample.obj',
						help='Input obj file')
	parser.add_argument('-o', '--output', default='./sample.ply',
						help='Output ply file')
	args = parser.parse_args()

	main(args)

