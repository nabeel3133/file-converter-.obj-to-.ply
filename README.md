# .obj to .ply file converter
Convert .obj file format to .ply file format with vertex colors.

## How to Run
```
git clone -b code_refactored https://github.com/nabeel3133/file-converter-.obj-to-.ply.git
cd file-converter-.obj-to-.ply
```
Run the following command
```
python convert.py --input [objfilename.obj] --output [plyfilename.ply]
```
### Example
```
python convert.py --input sample.obj --output sample.ply
```
The above code will take `sample.obj` and convert it to ply format with the output file named as `sample.ply`

**Note: Code cannot be used for obj files containing list of vertex normals and texture coordinates**
