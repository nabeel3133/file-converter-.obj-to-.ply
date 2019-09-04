# .obj to .ply file converter
Convert .obj file format to .ply file format with vertex colors.

## Command to Run
Run the following command in the root folder 
```
python convert.py --input [objfilename.obj] --output [plyfilename.ply]
```
### Example
```
python convert.py --input sample.obj --output sample.ply
```
The above code will take "sample.obj" and convert it to ply format with the output files named:
1. "sample.ply" without vertex colors 
2. "sampleWithRGB.ply" with vertex colors

**Note: Code cannot be used for obj files containing vertex normals and vertex textures**
