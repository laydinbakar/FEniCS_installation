# Convert `msh` file into `xdmf` format
We need [this script](https://github.com/laydinbakar/FEniCS_installation/blob/main/scripts/msh2xdmf.py) to convert a mesh from `msh` to `xdmf` format. Download it into the directory where your mesh file is in.
Later, run the following command on Ubuntu Terminal on the same directory.
```
python3 msh2xdmf.py --mesh_name mesh-file-name --dim 2
python3 msh2xdmf.py --mesh_name mesh-file-name --dim 3

```
for a 2D mesh or a 3D mesh respectively.
If you get error saying you do not have meshio installed, run,
```
sudo apt-get update
sudo apt-get install python3-meshio
```
and repeat running `msh2xdmf.py` script as explained above.

Finally, you will have 4 more files as 
* `mesh-file-name_mesh.xdmf`
* `mesh-file-name_mesh.h5`
* `mesh-file-name_bcs.xdmf`
* `mesh-file-name_bcs.h5`
These files will include mesh and boundary information.

# Read xdmf file into FEniCS

```
# Read mesh and boundary files
mesh=Mesh()
with XDMFFile("msh-file-name_mesh.xdmf") as infile:
  infile.read(mesh)
dim=mesh.topology().dim()
print("Mesh dimension: "+str(dim))
mvc = MeshValueCollection("size_t", mesh, dim)
with XDMFFile("msh-file-name_mf.xdmf") as infile:
  infile.read(mvc, "name_to_read")
boundaries=cpp.mesh.MeshFunctionSizet(mesh, mvc)

# Define discretized domains
QUAD_DEG=2
dx = dx(metadata={"quadrature_degree":QUAD_DEG})
ds = ds(metadata={"quadrature_degree":QUAD_DEG})
```

# Write xdmf file from FEniCS
```
# Write output
xdmffile_u = XDMFFile('output-directory/u.xdmf')
xdmffile_u.parameters["flush_output"] = True
xdmffile_u.parameters.update(
{
    "functions_share_mesh": True,
    "rewrite_function_mesh": False
})
xdmffile_u.write(u)
```
