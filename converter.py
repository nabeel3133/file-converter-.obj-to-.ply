import numpy as np

class Converter:
	def __init__(self, obj_file):
		self.obj_file = open(obj_file,'r')

	def GetVertsAndTri(self):
		vertices_list = []
		tri_list = []
		for i, line in enumerate(self.obj_file):
			if(line[0] == 'v'):
				vertices = line.strip('\n').split(" ")
				vertices_list.append(vertices[1:])
			elif (line[0] == 'f'):
				tri = line.strip('\n').split(" ")
				tri_list.append(tri[1:])
			else:
				continue

		self.vertices = np.array(vertices_list, dtype=np.float32)
		self.tri = np.array(tri_list, dtype=np.int)

	def write_ply(self, wfp):
		n_vertex = self.vertices.shape[0]
		n_cols = self.vertices.shape[1]
		header = ''
		if (n_cols == 6):
			header = """ply\nformat ascii 1.0\nelement vertex {}\nproperty float x\nproperty float y\nproperty float z\nproperty uchar red\nproperty uchar green\nproperty uchar blue\nelement face {}\nproperty list uchar int vertex_indices\nend_header"""
		elif (n_cols == 3):
			header = """ply\nformat ascii 1.0\nelement vertex {}\nproperty float x\nproperty float y\nproperty float z\nelement face {}\nproperty list uchar int vertex_indices\nend_header"""
		
		n_face = self.tri.shape[0]
		header = header.format(n_vertex, n_face)

		with open(wfp, 'w') as f:
			f.write(header + '\n')
			for i in range(n_vertex):
				if (n_cols == 3):
					x,y,z = self.vertices[i, :]
					f.write('{:.4f} {:.4f} {:.4f}\n'.format(x, y, z))
				elif (n_cols == 6):
					x,y,z,r,g,b = self.vertices[i, :]
					if (int(r) == 0 or int(g) == 0 or int(b) == 0):
						r = r*255
						g = g*255
						b = b*255
					f.write('{:.4f} {:.4f} {:.4f} {:d} {:d} {:d}\n'.format(x, y, z, int(r), int(g), int(b)))
			for i in range(n_face):
				idx1, idx2, idx3 = self.tri[i, :]
				f.write('3 {} {} {}\n'.format(idx1 - 1, idx2 - 1, idx3 - 1))