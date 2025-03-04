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

from salome.shaper import model

model.begin()
partSet = model.moduleDocument()

### Create Part
Part_1 = model.addPart(partSet)
Part_1_doc = Part_1.document()

### Create Sketch
Sketch_1 = model.addSketch(Part_1_doc, model.defaultPlane("XOY"))

### Create SketchLine
SketchLine_1 = Sketch_1.addLine(0, 0, 20.635961271104, 35.74253338457832)

### Create SketchProjection
SketchProjection_1 = Sketch_1.addProjection(model.selection("VERTEX", "PartSet/Origin"), False)
SketchPoint_1 = SketchProjection_1.createdFeature()
Sketch_1.setCoincident(SketchLine_1.startPoint(), SketchPoint_1.result())

### Create SketchLine
SketchLine_2 = Sketch_1.addLine(20.635961271104, 35.74253338457832, 0, 35.74253338457832)
Sketch_1.setCoincident(SketchLine_1.endPoint(), SketchLine_2.startPoint())

### Create SketchProjection
SketchProjection_2 = Sketch_1.addProjection(model.selection("EDGE", "PartSet/OY"), False)
SketchLine_3 = SketchProjection_2.createdFeature()
Sketch_1.setCoincident(SketchLine_2.endPoint(), SketchLine_3.result())
Sketch_1.setHorizontal(SketchLine_2.result())

### Create SketchConstraintAngle
Sketch_1.setAngle(SketchLine_2.result(), SketchLine_1.result(), 60, type = "Direct")

### Create SketchConstraintMirror
SketchConstraintMirror_1 = Sketch_1.addMirror(SketchLine_3.result(), [SketchLine_2.result(), SketchLine_1.result()])
[SketchLine_4, SketchLine_5] = SketchConstraintMirror_1.mirrored()

### Create SketchLine
SketchLine_6 = Sketch_1.addLine(-177.2659993128781, 130.8145552758825, 176.1530847745012, 130.8145552758825)

### Create SketchLine
SketchLine_7 = Sketch_1.addLine(176.1530847745012, 130.8145552758825, 176.1530847745012, -93.75382107130639)

### Create SketchLine
SketchLine_8 = Sketch_1.addLine(176.1530847745012, -93.75382107130639, -177.2659993128781, -93.75382107130639)

### Create SketchLine
SketchLine_9 = Sketch_1.addLine(-177.2659993128781, -93.75382107130639, -177.2659993128781, 130.8145552758825)
Sketch_1.setCoincident(SketchLine_9.endPoint(), SketchLine_6.startPoint())
Sketch_1.setCoincident(SketchLine_6.endPoint(), SketchLine_7.startPoint())
Sketch_1.setCoincident(SketchLine_7.endPoint(), SketchLine_8.startPoint())
Sketch_1.setCoincident(SketchLine_8.endPoint(), SketchLine_9.startPoint())
Sketch_1.setPerpendicular(SketchLine_6.result(), SketchLine_7.result())
Sketch_1.setPerpendicular(SketchLine_7.result(), SketchLine_8.result())
Sketch_1.setPerpendicular(SketchLine_8.result(), SketchLine_9.result())
model.do()

### Create Face
Face_1 = model.addFace(Part_1_doc, [model.selection("FACE", "Sketch_1/Face-SketchLine_1r-SketchLine_2f-SketchLine_4r-SketchLine_5r")])

### Create Face
Face_2 = model.addFace(Part_1_doc, [model.selection("FACE", "Sketch_1/Face-SketchLine_9r-SketchLine_8r-SketchLine_7r-SketchLine_6r-SketchLine_5f-SketchLine_4f-SketchLine_2r-SketchLine_1r")])

### Create Cut
Cut_1 = model.addCut(Part_1_doc, [model.selection("FACE", "Face_2_1")], [model.selection("FACE", "Face_1_1")], keepSubResults = True)

### Create Extrusion
Extrusion_1 = model.addExtrusion(Part_1_doc, [model.selection("FACE", "Sketch_1/Face-SketchLine_9r-SketchLine_8r-SketchLine_7r-SketchLine_6r-SketchLine_5f-SketchLine_4f-SketchLine_2r-SketchLine_1r")], model.selection(), 0.1, 0, "Faces|Wires")

### Create Group
Group_1 = model.addGroup(Part_1_doc, "Faces", [model.selection("FACE", "Extrusion_1_1/Generated_Face&Sketch_1/SketchLine_9")])
Group_1.setName("inlet")
Group_1.result().setName("inlet")

### Create Group
Group_2 = model.addGroup(Part_1_doc, "Faces", [model.selection("FACE", "Extrusion_1_1/Generated_Face&Sketch_1/SketchLine_7")])
Group_2.setName("outlet")
Group_2.result().setName("outlet")

### Create Group
Group_3 = model.addGroup(Part_1_doc, "Faces", [model.selection("FACE", "Extrusion_1_1/Generated_Face&Sketch_1/SketchLine_6")])
Group_3.setName("top")
Group_3.result().setName("top")

### Create Group
Group_4 = model.addGroup(Part_1_doc, "Faces", [model.selection("FACE", "Extrusion_1_1/Generated_Face&Sketch_1/SketchLine_8")])
Group_4.setName("bottom")
Group_4.result().setName("bottom")

### Create Group
Group_5_objects = [model.selection("FACE", "Extrusion_1_1/Generated_Face&Sketch_1/SketchLine_2"),
                   model.selection("FACE", "Extrusion_1_1/Generated_Face&Sketch_1/SketchLine_1"),
                   model.selection("FACE", "Extrusion_1_1/Generated_Face&Sketch_1/SketchLine_5"),
                   model.selection("FACE", "Extrusion_1_1/Generated_Face&Sketch_1/SketchLine_4")]
Group_5 = model.addGroup(Part_1_doc, "Faces", Group_5_objects)
Group_5.setName("nabla")
Group_5.result().setName("nabla")

model.end()

###
### SHAPERSTUDY component
###

model.publishToShaperStudy()
import SHAPERSTUDY
Cut_1_1, = SHAPERSTUDY.shape(model.featureStringId(Cut_1))
Extrusion_1_1, inlet, outlet, top, bottom, nabla, = SHAPERSTUDY.shape(model.featureStringId(Extrusion_1))
###
### SMESH component
###

import  SMESH, SALOMEDS
from salome.smesh import smeshBuilder

smesh = smeshBuilder.New()
#smesh.SetEnablePublish( False ) # Set to False to avoid publish in study if not needed or in some particular situations:
                                 # multiples meshes built in parallel, complex and numerous mesh edition (performance)

#hyp_1.SetLength( 1 ) ### not created Object
NETGEN_3D_Parameters_1 = smesh.CreateHypothesisByAverageLength( 'NETGEN_Parameters', 'NETGENEngine', 1, 0 )
smeshObj_1 = smesh.Mesh(Cut_1_1)
#hyp_3.SetLength( 41.8731 ) ### not created Object
NETGEN_2D_Parameters_1 = smesh.CreateHypothesisByAverageLength( 'NETGEN_Parameters_2D', 'NETGENEngine', 41.8731, 0 )
NETGEN_1D_2D = smesh.CreateHypothesis('NETGEN_2D', 'NETGENEngine')
status = smeshObj_1.AddHypothesis(NETGEN_1D_2D)
status = smeshObj_1.AddHypothesis( Cut_1_1, NETGEN_2D_Parameters_1 )
isDone = smeshObj_1.Compute()
smeshObj_1.CheckCompute()
Viscous_Layers_2D_1 = smesh.CreateHypothesis('ViscousLayers2D')
Viscous_Layers_2D_1.SetTotalThickness( 0.5 )
Viscous_Layers_2D_1.SetNumberLayers( 5 )
Viscous_Layers_2D_1.SetStretchFactor( 1 )
Viscous_Layers_2D_1.SetEdges( [], 1 )
status = smeshObj_1.AddHypothesis(Viscous_Layers_2D_1)
smeshObj_1.Clear()
isDone = smeshObj_1.Compute()
smeshObj_1.CheckCompute()
NETGEN_2D_Parameters_1.SetMaxSize( 5 )
NETGEN_2D_Parameters_1.SetMinSize( 1.2 )
NETGEN_2D_Parameters_1.SetSecondOrder( 0 )
NETGEN_2D_Parameters_1.SetOptimize( 1 )
NETGEN_2D_Parameters_1.SetFineness( 2 )
NETGEN_2D_Parameters_1.SetChordalError( 20.9366 )
NETGEN_2D_Parameters_1.SetChordalErrorEnabled( 1 )
NETGEN_2D_Parameters_1.SetUseSurfaceCurvature( 1 )
NETGEN_2D_Parameters_1.SetFuseEdges( 1 )
NETGEN_2D_Parameters_1.SetWorstElemMeasure( 640 )
NETGEN_2D_Parameters_1.SetUseDelauney( 0 )
NETGEN_2D_Parameters_1.SetQuadAllowed( 0 )
NETGEN_2D_Parameters_1.SetWorstElemMeasure( 221 )
NETGEN_2D_Parameters_1.SetCheckChartBoundary( 48 )
smeshObj_1.Clear()
isDone = smeshObj_1.Compute()
smeshObj_1.CheckCompute()
Viscous_Layers_2D_1.SetTotalThickness( 5 )
Viscous_Layers_2D_1.SetNumberLayers( 5 )
Viscous_Layers_2D_1.SetStretchFactor( 1 )
Viscous_Layers_2D_1.SetEdges( [], 1 )
smeshObj_1.Clear()
isDone = smeshObj_1.Compute()
smeshObj_1.CheckCompute()
NETGEN_2D_Parameters_1.SetMaxSize( 5 )
NETGEN_2D_Parameters_1.SetMinSize( 1.2 )
NETGEN_2D_Parameters_1.SetSecondOrder( 0 )
NETGEN_2D_Parameters_1.SetOptimize( 1 )
NETGEN_2D_Parameters_1.SetFineness( 4 )
NETGEN_2D_Parameters_1.SetChordalError( 20.9366 )
NETGEN_2D_Parameters_1.SetChordalErrorEnabled( 1 )
NETGEN_2D_Parameters_1.SetUseSurfaceCurvature( 1 )
NETGEN_2D_Parameters_1.SetFuseEdges( 1 )
NETGEN_2D_Parameters_1.SetWorstElemMeasure( 464 )
NETGEN_2D_Parameters_1.SetQuadAllowed( 0 )
NETGEN_2D_Parameters_1.SetWorstElemMeasure( 62 )
NETGEN_2D_Parameters_1.SetCheckChartBoundary( 64 )
status = smeshObj_1.RemoveHypothesis(Viscous_Layers_2D_1)
smeshObj_1.Clear()
isDone = smeshObj_1.Compute()
smeshObj_1.CheckCompute()
NETGEN_2D_Parameters_1.SetMinSize( 0.5 )
NETGEN_2D_Parameters_1.SetWorstElemMeasure( 464 )
NETGEN_2D_Parameters_1.SetCheckChartBoundary( 1 )
NETGEN_2D_Parameters_1.SetWorstElemMeasure( 62 )
NETGEN_2D_Parameters_1.SetCheckChartBoundary( 64 )
smeshObj_1.Clear()
isDone = smeshObj_1.Compute()
smeshObj_1.CheckCompute()
NETGEN_2D_Parameters_1.SetMaxSize( 2 )
NETGEN_2D_Parameters_1.SetMinSize( 0.05 )
NETGEN_2D_Parameters_1.SetWorstElemMeasure( 464 )
NETGEN_2D_Parameters_1.SetCheckChartBoundary( 1 )
NETGEN_2D_Parameters_1.SetWorstElemMeasure( 62 )
NETGEN_2D_Parameters_1.SetCheckChartBoundary( 64 )
smeshObj_1.Clear()
isDone = smeshObj_1.Compute()
smeshObj_1.CheckCompute()
NETGEN_2D_Parameters_1.SetWorstElemMeasure( 464 )
NETGEN_2D_Parameters_1.SetCheckChartBoundary( 1 )
NETGEN_2D_Parameters_1.SetLocalSizeOnShape(__NOT__Published__Object__, 0.02)
NETGEN_2D_Parameters_1.SetWorstElemMeasure( 62 )
NETGEN_2D_Parameters_1.SetCheckChartBoundary( 64 )
smeshObj_1.Clear()
isDone = smeshObj_1.Compute()
smeshObj_1.CheckCompute()
smeshObj_2 = smeshObj_1.GroupOnGeom(__NOT__Published__Object__,'inlet',SMESH.EDGE)
smeshObj_3 = smeshObj_1.GroupOnGeom(__NOT__Published__Object__,'outlet',SMESH.EDGE)
smeshObj_4 = smeshObj_1.GroupOnGeom(__NOT__Published__Object__,'bottom',SMESH.EDGE)
smeshObj_5 = smeshObj_1.GroupOnGeom(__NOT__Published__Object__,'top',SMESH.EDGE)
smeshObj_6 = smeshObj_1.GroupOnGeom(__NOT__Published__Object__,'nabla',SMESH.EDGE)
smeshObj_1.Clear()
isDone = smeshObj_1.Compute()
smeshObj_1.CheckCompute()
[ smeshObj_2, smeshObj_3, smeshObj_4, smeshObj_5, smeshObj_6 ] = smeshObj_1.GetGroups()
#hyp_6.SetLength( 1 ) ### not created Object
NETGEN_3D_Parameters_2 = smesh.CreateHypothesisByAverageLength( 'NETGEN_Parameters', 'NETGENEngine', 1, 0 )
NETGEN_3D_Parameters_2.SetMaxSize( 0.5 )
NETGEN_3D_Parameters_2.SetMinSize( 0.05 )
NETGEN_3D_Parameters_2.SetSecondOrder( 0 )
NETGEN_3D_Parameters_2.SetOptimize( 1 )
NETGEN_3D_Parameters_2.SetFineness( 2 )
NETGEN_3D_Parameters_2.SetChordalError( 0.5 )
NETGEN_3D_Parameters_2.SetChordalErrorEnabled( 1 )
NETGEN_3D_Parameters_2.SetUseSurfaceCurvature( 1 )
NETGEN_3D_Parameters_2.SetFuseEdges( 1 )
NETGEN_3D_Parameters_2.SetQuadAllowed( 0 )
NETGEN_3D_Parameters_2.SetLocalSizeOnShape(nabla, 0.02)
NETGEN_3D_Parameters_2.SetCheckChartBoundary( 48 )
Mesh_1 = smesh.Mesh(Extrusion_1_1,'Mesh_1')
status = Mesh_1.AddHypothesis( Extrusion_1_1, NETGEN_3D_Parameters_2 )
NETGEN_1D_2D_3D = Mesh_1.Tetrahedron(algo=smeshBuilder.NETGEN_1D2D3D)
inlet_1 = Mesh_1.GroupOnGeom(inlet,'inlet',SMESH.FACE)
outlet_1 = Mesh_1.GroupOnGeom(outlet,'outlet',SMESH.FACE)
top_1 = Mesh_1.GroupOnGeom(top,'top',SMESH.FACE)
bottom_1 = Mesh_1.GroupOnGeom(bottom,'bottom',SMESH.FACE)
nabla_1 = Mesh_1.GroupOnGeom(nabla,'nabla',SMESH.FACE)
isDone = Mesh_1.Compute()
Mesh_1.CheckCompute()
[ inlet_1, outlet_1, top_1, bottom_1, nabla_1 ] = Mesh_1.GetGroups()
NETGEN_3D_Parameters_2.SetMaxSize( 2 )
NETGEN_3D_Parameters_2.SetMinSize( 0.1 )
NETGEN_3D_Parameters_2.SetCheckChartBoundary( 1 )
NETGEN_3D_Parameters_2.SetLocalSizeOnShape(nabla, 0.05)
NETGEN_3D_Parameters_2.SetCheckChartBoundary( 48 )
Mesh_1.Clear()
isDone = Mesh_1.Compute()
Mesh_1.CheckCompute()
[ inlet_1, outlet_1, top_1, bottom_1, nabla_1 ] = Mesh_1.GetGroups()
NETGEN_3D_Parameters_2.SetMaxSize( 4 )
NETGEN_3D_Parameters_2.SetCheckChartBoundary( 1 )
NETGEN_3D_Parameters_2.SetCheckChartBoundary( 48 )
Mesh_1.Clear()
isDone = Mesh_1.Compute()
Mesh_1.CheckCompute()
[ inlet_1, outlet_1, top_1, bottom_1, nabla_1 ] = Mesh_1.GetGroups()
try:
  Mesh_1.ExportUNV( r'C:/Users/Arman/Desktop/SalomeTraining/nablaLogoUNV.unv', 0 )
  pass
except:
  print('ExportUNV() failed. Invalid file name?')

## some objects were removed
aStudyBuilder = salome.myStudy.NewBuilder()
SO = salome.myStudy.FindObjectIOR(salome.myStudy.ConvertObjectToIOR(smeshObj_5))
if SO: aStudyBuilder.RemoveObjectWithChildren(SO)
SO = salome.myStudy.FindObjectIOR(salome.myStudy.ConvertObjectToIOR(smeshObj_1.GetMesh()))
if SO: aStudyBuilder.RemoveObjectWithChildren(SO)
SO = salome.myStudy.FindObjectIOR(salome.myStudy.ConvertObjectToIOR(smeshObj_6))
if SO: aStudyBuilder.RemoveObjectWithChildren(SO)
SO = salome.myStudy.FindObjectIOR(salome.myStudy.ConvertObjectToIOR(smeshObj_3))
if SO: aStudyBuilder.RemoveObjectWithChildren(SO)
SO = salome.myStudy.FindObjectIOR(salome.myStudy.ConvertObjectToIOR(smeshObj_4))
if SO: aStudyBuilder.RemoveObjectWithChildren(SO)
SO = salome.myStudy.FindObjectIOR(salome.myStudy.ConvertObjectToIOR(smeshObj_2))
if SO: aStudyBuilder.RemoveObjectWithChildren(SO)

## Set names of Mesh objects
smesh.SetName(NETGEN_3D_Parameters_2, 'NETGEN 3D Parameters_2')
smesh.SetName(top_1, 'top')
smesh.SetName(nabla_1, 'nabla')
smesh.SetName(Viscous_Layers_2D_1, 'Viscous Layers 2D_1')
smesh.SetName(bottom_1, 'bottom')
smesh.SetName(NETGEN_3D_Parameters_1, 'NETGEN 3D Parameters_1')
smesh.SetName(outlet_1, 'outlet')
smesh.SetName(Mesh_1.GetMesh(), 'Mesh_1')
smesh.SetName(inlet_1, 'inlet')
smesh.SetName(NETGEN_1D_2D, 'NETGEN 1D-2D')
smesh.SetName(NETGEN_2D_Parameters_1, 'NETGEN 2D Parameters_1')
smesh.SetName(NETGEN_1D_2D_3D.GetAlgorithm(), 'NETGEN 1D-2D-3D')


if salome.sg.hasDesktop():
  salome.sg.updateObjBrowser()
