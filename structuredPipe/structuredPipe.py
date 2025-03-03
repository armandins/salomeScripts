#!/usr/bin/env python

###
### This file is generated automatically by SALOME v9.13.0 with dump python functionality
###

import sys
import salome

salome.salome_init()
import salome_notebook
notebook = salome_notebook.NoteBook()
sys.path.insert(0, r'C:/Users/Arman/Desktop/SalomeTraining')

###
### SHAPER component
###

from SketchAPI import *

from salome.shaper import model

model.begin()
partSet = model.moduleDocument()

### Create Part
Part_1 = model.addPart(partSet)
Part_1_doc = Part_1.document()

### Create Cylinder
Cylinder_1 = model.addCylinder(Part_1_doc, model.selection("VERTEX", "PartSet/Origin"), model.selection("EDGE", "PartSet/OX"), 0.1, 1)

### Create Sketch
Sketch_1 = model.addSketch(Part_1_doc, model.selection("FACE", "Cylinder_1_1/Face_3"))

### Create SketchLine
SketchLine_1 = Sketch_1.addLine(-0.025, -0.025, 0.025, -0.025)

### Create SketchLine
SketchLine_2 = Sketch_1.addLine(0.025, -0.025, 0.025, 0.025)

### Create SketchLine
SketchLine_3 = Sketch_1.addLine(0.025, 0.025, -0.025, 0.025)

### Create SketchLine
SketchLine_4 = Sketch_1.addLine(-0.025, 0.025, -0.025, -0.025)
Sketch_1.setCoincident(SketchLine_4.endPoint(), SketchLine_1.startPoint())
Sketch_1.setCoincident(SketchLine_1.endPoint(), SketchLine_2.startPoint())
Sketch_1.setCoincident(SketchLine_2.endPoint(), SketchLine_3.startPoint())
Sketch_1.setCoincident(SketchLine_3.endPoint(), SketchLine_4.startPoint())
Sketch_1.setPerpendicular(SketchLine_1.result(), SketchLine_2.result())
Sketch_1.setPerpendicular(SketchLine_2.result(), SketchLine_3.result())
Sketch_1.setPerpendicular(SketchLine_3.result(), SketchLine_4.result())

### Create SketchProjection
SketchProjection_1 = Sketch_1.addProjection(model.selection("VERTEX", "[Cylinder_1_1/Face_1][Cylinder_1_1/Face_3]__cc"), False)
SketchPoint_1 = SketchProjection_1.createdFeature()
Sketch_1.setHorizontalDistance(SketchLine_1.endPoint(), SketchAPI_Point(SketchPoint_1).coordinates(), 0.025)

### Create SketchProjection
SketchProjection_2 = Sketch_1.addProjection(model.selection("VERTEX", "[Cylinder_1_1/Face_1][Cylinder_1_1/Face_3]__cc"), False)
SketchPoint_2 = SketchProjection_2.createdFeature()
Sketch_1.setHorizontalDistance(SketchLine_1.startPoint(), SketchAPI_Point(SketchPoint_2).coordinates(), 0.025)

### Create SketchProjection
SketchProjection_3 = Sketch_1.addProjection(model.selection("VERTEX", "[Cylinder_1_1/Face_1][Cylinder_1_1/Face_3]__cc"), False)
SketchPoint_3 = SketchProjection_3.createdFeature()
Sketch_1.setVerticalDistance(SketchLine_1.startPoint(), SketchAPI_Point(SketchPoint_3).coordinates(), 0.025)

### Create SketchProjection
SketchProjection_4 = Sketch_1.addProjection(model.selection("VERTEX", "[Cylinder_1_1/Face_1][Cylinder_1_1/Face_3]__cc"), False)
SketchPoint_4 = SketchProjection_4.createdFeature()
Sketch_1.setVerticalDistance(SketchLine_3.startPoint(), SketchAPI_Point(SketchPoint_4).coordinates(), 0.025)

### Create SketchProjection
SketchProjection_5 = Sketch_1.addProjection(model.selection("VERTEX", "[Cylinder_1_1/Face_1][Cylinder_1_1/Face_3]__cc"), False)
SketchPoint_5 = SketchProjection_5.createdFeature()
Sketch_1.setVerticalDistance(SketchLine_3.endPoint(), SketchAPI_Point(SketchPoint_5).coordinates(), 0.025)
model.do()

### Create Extrusion
Extrusion_1 = model.addExtrusion(Part_1_doc, [model.selection("FACE", "Sketch_1/Face-SketchLine_1r-SketchLine_2f-SketchLine_3f-SketchLine_4f")], model.selection(), -1, 0, "Faces|Wires")

### Create Rotation
Rotation_1 = model.addRotation(Part_1_doc, [model.selection("SOLID", "Cylinder_1_1")], axis = model.selection("EDGE", "PartSet/OX"), angle = 45, keepSubResults = True)

### Create Smash
Smash_1 = model.addSmash(Part_1_doc, [model.selection("SOLID", "Rotation_1_1")], [model.selection("SOLID", "Extrusion_1_1")], keepSubResults = True)

### Create Plane
Plane_4 = model.addPlane(Part_1_doc, model.selection("FACE", "PartSet/XOZ"), model.selection("EDGE", "PartSet/OX"), 45)

### Create Plane
Plane_5 = model.addPlane(Part_1_doc, model.selection("FACE", "PartSet/XOZ"), model.selection("EDGE", "PartSet/OX"), 135)

### Create Split
Split_1 = model.addSplit(Part_1_doc, [model.selection("SOLID", "Smash_1_1_1")], [model.selection("FACE", "Plane_1"), model.selection("FACE", "Plane_2")], keepSubResults = True)

### Create Group
Group_1_objects = [model.selection("EDGE", "Split_1_1_4/Generated_Edge&Plane_2/Plane_2&Cylinder_1_1/Face_1"),
                   model.selection("EDGE", "Split_1_1_3/Generated_Edge&Plane_1/Plane_1&Cylinder_1_1/Face_1"),
                   model.selection("EDGE", "Split_1_1_2/Generated_Edge&Plane_2/Plane_2&Cylinder_1_1/Face_1"),
                   model.selection("EDGE", "[Split_1_1_2/Modified_Face&Cylinder_1_1/Face_1][Split_1_1_2/Modified_Face&Plane_1/Plane_1]"),
                   model.selection("EDGE", "[Split_1_1_3/Modified_Face&Plane_1/Plane_1][Extrusion_1_1/Generated_Face&Sketch_1/SketchLine_3]"),
                   model.selection("EDGE", "[Split_1_1_4/Modified_Face&Plane_2/Plane_2][Extrusion_1_1/Generated_Face&Sketch_1/SketchLine_1]"),
                   model.selection("EDGE", "[Split_1_1_2/Modified_Face&Plane_1/Plane_1][Extrusion_1_1/Generated_Face&Sketch_1/SketchLine_4]"),
                   model.selection("EDGE", "[Split_1_1_2/Modified_Face&Plane_2/Plane_2][Extrusion_1_1/Generated_Face&Sketch_1/SketchLine_4]")]
Group_1 = model.addGroup(Part_1_doc, "Edges", Group_1_objects)
Group_1.setName("n_len")
Group_1.result().setName("n_len")
Group_1.result().setColor(255, 0, 0)

### Create Group
Group_2_objects = [model.selection("EDGE", "Split_1_1_2/Generated_Edge&Plane_1/Plane_1&Cylinder_1_1/Face_2"),
                   model.selection("EDGE", "Split_1_1_4/Generated_Edge&Plane_2/Plane_2&Cylinder_1_1/Face_2"),
                   model.selection("EDGE", "Split_1_1_3/Generated_Edge&Plane_1/Plane_1&Cylinder_1_1/Face_2"),
                   model.selection("EDGE", "Split_1_1_2/Generated_Edge&Plane_2/Plane_2&Cylinder_1_1/Face_2"),
                   model.selection("EDGE", "Split_1_1_4/Generated_Edge&Plane_2/Plane_2&Cylinder_1_1/Face_3"),
                   model.selection("EDGE", "Split_1_1_3/Generated_Edge&Plane_1/Plane_1&Cylinder_1_1/Face_3"),
                   model.selection("EDGE", "Split_1_1_2/Generated_Edge&Plane_2/Plane_2&Cylinder_1_1/Face_3"),
                   model.selection("EDGE", "Split_1_1_2/Generated_Edge&Plane_1/Plane_1&Cylinder_1_1/Face_3")]
Group_2 = model.addGroup(Part_1_doc, "Edges", Group_2_objects)
Group_2.setName("n_axial")
Group_2.result().setName("n_axial")
Group_2.result().setColor(0, 255, 0)

### Create Group
Group_3_objects = [model.selection("EDGE", "[Split_1_1_4/Modified_Face&Cylinder_1_1/Face_1][Split_1_1_4/Modified_Face&Cylinder_1_1/Face_3]"),
                   model.selection("EDGE", "[Split_1_1_2/Modified_Face&Cylinder_1_1/Face_1][Split_1_1_2/Modified_Face&Cylinder_1_1/Face_3]"),
                   model.selection("EDGE", "[Split_1_1_3/Modified_Face&Cylinder_1_1/Face_1][Split_1_1_3/Modified_Face&Cylinder_1_1/Face_3]"),
                   model.selection("EDGE", "[Split_1_1_5/Modified_Face&Cylinder_1_1/Face_1][Split_1_1_5/Modified_Face&Cylinder_1_1/Face_3]"),
                   model.selection("EDGE", "[Split_1_1_5/Modified_Face&Cylinder_1_1/Face_3][Extrusion_1_1/Generated_Face&Sketch_1/SketchLine_2]"),
                   model.selection("EDGE", "[Split_1_1_4/Modified_Face&Cylinder_1_1/Face_3][Extrusion_1_1/Generated_Face&Sketch_1/SketchLine_1]"),
                   model.selection("EDGE", "[Split_1_1_2/Modified_Face&Cylinder_1_1/Face_3][Extrusion_1_1/Generated_Face&Sketch_1/SketchLine_4]"),
                   model.selection("EDGE", "[Split_1_1_3/Modified_Face&Cylinder_1_1/Face_3][Extrusion_1_1/Generated_Face&Sketch_1/SketchLine_3]"),
                   model.selection("EDGE", "[Split_1_1_4/Modified_Face&Cylinder_1_1/Face_1][Split_1_1_4/Modified_Face&Cylinder_1_1/Face_2]"),
                   model.selection("EDGE", "[Split_1_1_2/Modified_Face&Cylinder_1_1/Face_1][Split_1_1_2/Modified_Face&Cylinder_1_1/Face_2]"),
                   model.selection("EDGE", "[Split_1_1_5/Modified_Face&Cylinder_1_1/Face_1][Split_1_1_5/Modified_Face&Cylinder_1_1/Face_2]"),
                   model.selection("EDGE", "[Split_1_1_3/Modified_Face&Cylinder_1_1/Face_1][Split_1_1_3/Modified_Face&Cylinder_1_1/Face_2]"),
                   model.selection("EDGE", "[Split_1_1_3/Modified_Face&Cylinder_1_1/Face_2][Extrusion_1_1/Generated_Face&Sketch_1/SketchLine_3]"),
                   model.selection("EDGE", "[Split_1_1_5/Modified_Face&Cylinder_1_1/Face_2][Extrusion_1_1/Generated_Face&Sketch_1/SketchLine_2]"),
                   model.selection("EDGE", "[Split_1_1_4/Modified_Face&Cylinder_1_1/Face_2][Extrusion_1_1/Generated_Face&Sketch_1/SketchLine_1]"),
                   model.selection("EDGE", "[Split_1_1_2/Modified_Face&Cylinder_1_1/Face_2][Extrusion_1_1/Generated_Face&Sketch_1/SketchLine_4]")]
Group_3 = model.addGroup(Part_1_doc, "Edges", Group_3_objects)
Group_3.setName("n_circular")
Group_3.result().setName("n_circular")
Group_3.result().setColor(0, 0, 255)

### Create Group
Group_4_objects = [model.selection("FACE", "Split_1_1_4/Modified_Face&Cylinder_1_1/Face_3"),
                   model.selection("FACE", "Split_1_1_2/Modified_Face&Cylinder_1_1/Face_3"),
                   model.selection("FACE", "Split_1_1_3/Modified_Face&Cylinder_1_1/Face_3"),
                   model.selection("FACE", "Split_1_1_5/Modified_Face&Cylinder_1_1/Face_3"),
                   model.selection("FACE", "Extrusion_1_1/From_Face")]
Group_4 = model.addGroup(Part_1_doc, "Faces", Group_4_objects)
Group_4.setName("inlet")
Group_4.result().setName("inlet")
Group_4.result().setColor(255, 255, 0)

### Create Group
Group_5_objects = [model.selection("FACE", "Split_1_1_2/Modified_Face&Cylinder_1_1/Face_1"),
                   model.selection("FACE", "Split_1_1_4/Modified_Face&Cylinder_1_1/Face_1"),
                   model.selection("FACE", "Split_1_1_3/Modified_Face&Cylinder_1_1/Face_1"),
                   model.selection("FACE", "Split_1_1_5/Modified_Face&Cylinder_1_1/Face_1")]
Group_5 = model.addGroup(Part_1_doc, "Faces", Group_5_objects)
Group_5.setName("walls")
Group_5.result().setName("walls")
Group_5.result().setColor(0, 255, 255)

### Create Group
Group_6_objects = [model.selection("FACE", "Split_1_1_4/Modified_Face&Cylinder_1_1/Face_2"),
                   model.selection("FACE", "Split_1_1_2/Modified_Face&Cylinder_1_1/Face_2"),
                   model.selection("FACE", "Extrusion_1_1/To_Face"),
                   model.selection("FACE", "Split_1_1_5/Modified_Face&Cylinder_1_1/Face_2"),
                   model.selection("FACE", "Split_1_1_3/Modified_Face&Cylinder_1_1/Face_2")]
Group_6 = model.addGroup(Part_1_doc, "Faces", Group_6_objects)
Group_6.setName("outlet")
Group_6.result().setName("outlet")
Group_6.result().setColor(255, 0, 255)

model.end()

###
### SHAPERSTUDY component
###

model.publishToShaperStudy()
import SHAPERSTUDY
Split_1_1, n_len, n_axial, n_circular, inlet, walls, outlet, = SHAPERSTUDY.shape(model.featureStringId(Split_1))
###
### GEOM component
###

import GEOM
from salome.geom import geomBuilder
import math
import SALOMEDS


geompy = geomBuilder.New()

O = geompy.MakeVertex(0, 0, 0)
OX = geompy.MakeVectorDXDYDZ(1, 0, 0)
OY = geompy.MakeVectorDXDYDZ(0, 1, 0)
OZ = geompy.MakeVectorDXDYDZ(0, 0, 1)
geompy.addToStudy( O, 'O' )
geompy.addToStudy( OX, 'OX' )
geompy.addToStudy( OY, 'OY' )
geompy.addToStudy( OZ, 'OZ' )

###
### SMESH component
###

import  SMESH, SALOMEDS
from salome.smesh import smeshBuilder

smesh = smeshBuilder.New()
#smesh.SetEnablePublish( False ) # Set to False to avoid publish in study if not needed or in some particular situations:
                                 # multiples meshes built in parallel, complex and numerous mesh edition (performance)

Regular_1D = smesh.CreateHypothesis('Regular_1D')
Quadrangle_2D = smesh.CreateHypothesis('Quadrangle_2D')
Hexa_3D = smesh.CreateHypothesis('Hexa_3D')
Number_of_Segments_1 = smesh.CreateHypothesis('NumberOfSegments')
Number_of_Segments_1.SetNumberOfSegments( 15 )
Mesh_2 = smesh.Mesh(Split_1_1,'Mesh_2')
n_len_1 = Mesh_2.GroupOnGeom(n_len,'n_len',SMESH.EDGE)
n_axial_1 = Mesh_2.GroupOnGeom(n_axial,'n_axial',SMESH.EDGE)
n_circular_1 = Mesh_2.GroupOnGeom(n_circular,'n_circular',SMESH.EDGE)
[ n_len_1, n_axial_1, n_circular_1 ] = Mesh_2.GetGroups()
Number_of_Segments_2 = smesh.CreateHypothesis('NumberOfSegments')
status = Mesh_2.AddHypothesis(Regular_1D,n_len)
status = Mesh_2.AddHypothesis(Number_of_Segments_2,n_len)
[ n_len_1, n_axial_1, n_circular_1 ] = Mesh_2.GetGroups()
Number_of_Segments_3 = smesh.CreateHypothesis('NumberOfSegments')
status = Mesh_2.AddHypothesis(Regular_1D,n_axial)
status = Mesh_2.AddHypothesis(Number_of_Segments_3,n_axial)
[ n_len_1, n_axial_1, n_circular_1 ] = Mesh_2.GetGroups()
Number_of_Segments_3.SetNumberOfSegments( 25 )
[ n_len_1, n_axial_1, n_circular_1 ] = Mesh_2.GetGroups()
Number_of_Segments_4 = smesh.CreateHypothesis('NumberOfSegments')
status = Mesh_2.AddHypothesis(Regular_1D,n_circular)
status = Mesh_2.AddHypothesis(Number_of_Segments_4,n_circular)
[ n_len_1, n_axial_1, n_circular_1 ] = Mesh_2.GetGroups()
Number_of_Segments_4.SetNumberOfSegments( 25 )
Number_of_Segments_2.SetNumberOfSegments( 60 )
[ n_len_1, n_axial_1, n_circular_1 ] = Mesh_2.GetGroups()
try:
  Mesh_2.ExportUNV( r'C:/Users/Arman/Desktop/pipeUnv.unv', 0 )
  pass
except:
  print('ExportUNV() failed. Invalid file name?')
try:
  Mesh_2.ExportSTL( r'C:/Users/Arman/Desktop/pipeSTL.stl', 1 )
  pass
except:
  print('ExportSTL() failed. Invalid file name?')
NETGEN_1D_2D_3D = Mesh_2.Tetrahedron(algo=smeshBuilder.NETGEN_1D2D3D)
[ n_len_1, n_axial_1, n_circular_1 ] = Mesh_2.GetGroups()
status = Mesh_2.RemoveHypothesis(NETGEN_1D_2D_3D)
status = Mesh_2.AddHypothesis(Regular_1D)
status = Mesh_2.AddHypothesis(Quadrangle_2D)
status = Mesh_2.AddHypothesis(Hexa_3D)
isDone = Mesh_2.Compute()
Mesh_2.CheckCompute()
[ n_len_1, n_axial_1, n_circular_1 ] = Mesh_2.GetGroups()
try:
  Mesh_2.ExportUNV( r'C:/Users/Arman/Desktop/Mesh_2.unv', 0 )
  pass
except:
  print('ExportUNV() failed. Invalid file name?')
inlet_1 = Mesh_2.GroupOnGeom(inlet,'inlet',SMESH.FACE)
walls_1 = Mesh_2.GroupOnGeom(walls,'walls',SMESH.FACE)
outlet_1 = Mesh_2.GroupOnGeom(outlet,'outlet',SMESH.FACE)
inlet_2 = Mesh_2.GroupOnGeom(inlet,'inlet',SMESH.NODE)
walls_2 = Mesh_2.GroupOnGeom(walls,'walls',SMESH.NODE)
outlet_2 = Mesh_2.GroupOnGeom(outlet,'outlet',SMESH.NODE)
try:
  Mesh_2.ExportUNV( r'C:/Users/Arman/Desktop/pipeUnv.unv', 0 )
  pass
except:
  print('ExportUNV() failed. Invalid file name?')
Sub_mesh_1 = Mesh_2.GetSubMesh( n_len, 'Sub-mesh_1' )
Sub_mesh_2 = Mesh_2.GetSubMesh( n_axial, 'Sub-mesh_2' )
Sub_mesh_3 = Mesh_2.GetSubMesh( n_circular, 'Sub-mesh_3' )


## Set names of Mesh objects
smesh.SetName(Regular_1D, 'Regular_1D')
smesh.SetName(Sub_mesh_2, 'Sub-mesh_2')
smesh.SetName(Mesh_2.GetMesh(), 'Mesh_2')
smesh.SetName(inlet_1, 'inlet')
smesh.SetName(Quadrangle_2D, 'Quadrangle_2D')
smesh.SetName(Sub_mesh_1, 'Sub-mesh_1')
smesh.SetName(n_len_1, 'n_len')
smesh.SetName(Number_of_Segments_2, 'Number of Segments_2')
smesh.SetName(n_circular_1, 'n_circular')
smesh.SetName(n_axial_1, 'n_axial')
smesh.SetName(outlet_1, 'outlet')
smesh.SetName(walls_1, 'walls')
smesh.SetName(outlet_2, 'outlet')
smesh.SetName(Number_of_Segments_3, 'Number of Segments_3')
smesh.SetName(Sub_mesh_3, 'Sub-mesh_3')
smesh.SetName(walls_2, 'walls')
smesh.SetName(Number_of_Segments_1, 'Number of Segments_1')
smesh.SetName(Number_of_Segments_4, 'Number of Segments_4')
smesh.SetName(inlet_2, 'inlet')
smesh.SetName(Hexa_3D, 'Hexa_3D')
smesh.SetName(NETGEN_1D_2D_3D.GetAlgorithm(), 'NETGEN 1D-2D-3D')


if salome.sg.hasDesktop():
  salome.sg.updateObjBrowser()
