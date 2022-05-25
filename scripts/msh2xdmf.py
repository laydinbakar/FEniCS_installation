#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--mesh_name', dest='mesh_name', default="mesh", type=str, help='Name of the mesh file without .xml')
parser.add_argument('--dim', dest='dim', default=3, help='Dimension')

args = parser.parse_args()
mesh_name = str(args.mesh_name)
dim = int(args.dim)

import meshio
if dim==3:
  msh = meshio.read(mesh_name+".msh")
  for cell in msh.cells:
      if cell.type == "triangle":
          triangle_cells = cell.data
      elif  cell.type == "tetra":
          tetra_cells = cell.data
  
  for key in msh.cell_data_dict["gmsh:physical"].keys():
      print(key)
      if key == "triangle":
          triangle_data = msh.cell_data_dict["gmsh:physical"][key]
      elif key == "tetra":
          tetra_data = msh.cell_data_dict["gmsh:physical"][key]
  tetra_mesh = meshio.Mesh(points=msh.points, cells={"tetra": tetra_cells})
  triangle_mesh =meshio.Mesh(points=msh.points,
                             cells=[("triangle", triangle_cells)],
                             cell_data={"name_to_read":[triangle_data]})
  meshio.write(mesh_name+"_mesh.xdmf", tetra_mesh)
  meshio.write(mesh_name+"_bcs.xdmf", triangle_mesh)
  print(mesh_name+"_mesh.xdmf")
  print(mesh_name+"_bcs.xdmf")
elif dim==2:
  import numpy
  msh = meshio.read(mesh_name+".msh")
  print(msh.points)
  TwoDpoints= msh.points
  TwoDpoints = numpy.delete(TwoDpoints, obj=2, axis=1) # Removes the 2D points'
  print(TwoDpoints)
  for cell in msh.cells:
      if cell.type == "line":
          line_cells = cell.data
      elif  cell.type == "triangle":
          triangle_cells = cell.data
  
  for key in msh.cell_data_dict["gmsh:physical"].keys():
      print(key)
      if key == "line":
          line_data = msh.cell_data_dict["gmsh:physical"][key]
      elif key == "triangle":
          triangle_data = msh.cell_data_dict["gmsh:physical"][key]
#triangle_mesh = meshio.Mesh(points=msh.points, cells={"triangle": triangle_cells})
#line_mesh =meshio.Mesh(points=msh.points,
  triangle_mesh = meshio.Mesh(points=TwoDpoints, cells={"triangle": triangle_cells})
  line_mesh =meshio.Mesh(points=TwoDpoints,
                             cells=[("line", line_cells)],
                             cell_data={"name_to_read":[line_data]})
  meshio.write(mesh_name+"_mesh.xdmf", triangle_mesh)
  meshio.write(mesh_name+"_bcs.xdmf", line_mesh)
  print(mesh_name+"_mesh.xdmf")
  print(mesh_name+"_bcs.xdmf")
else:
  import numpy as np
  msh = meshio.read(mesh_name+".msh")
  
  line_cells = []
  for cell in msh.cells:
      if cell.type == "triangle":
          triangle_cells = cell.data
      elif  cell.type == "line":
          if len(line_cells) == 0:
              line_cells = cell.data
          else:
              line_cells = np.vstack([line_cells, cell.data])
  
  line_data = []
  for key in msh.cell_data_dict["gmsh:physical"].keys():
      if key == "line":
          if len(line_data) == 0:
              line_data = msh.cell_data_dict["gmsh:physical"][key]
          else:
              line_data = np.vstack([line_data, msh.cell_data_dict["gmsh:physical"][key]])
      elif key == "triangle":
          triangle_data = msh.cell_data_dict["gmsh:physical"][key]
  
  triangle_mesh = meshio.Mesh(points=msh.points, cells={"triangle": triangle_cells})
  line_mesh =meshio.Mesh(points=msh.points,
                             cells=[("line", line_cells)],
                             cell_data={"name_to_read":[line_data]})
#  meshio.write("mesh.xdmf", triangle_mesh)
#  
#  meshio.xdmf.write("mf.xdmf", line_mesh)
  meshio.write(mesh_name+"_mesh.xdmf", triangle_mesh)
  meshio.xdmf.write(mesh_name+"_bcs.xdmf", line_mesh)
  print(mesh_name+"_mesh.xdmf")
  print(mesh_name+"_bcs.xdmf")
