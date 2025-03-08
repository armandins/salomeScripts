#!/usr/bin/env python

###
### Arman Dindar Safa 
### 3 / 9 / 2025
### This is the geom of Ahmed body test case.
### The angle phi is parameterized.
### https://www.cfd-online.com/Wiki/Ahmed_body
### This file is generated automatically by SALOME v9.13.0 with dump python functionality
###

import sys
import salome

salome.salome_init()
import salome_notebook
notebook = salome_notebook.NoteBook()
sys.path.insert(0, r'C:/Users/Arman/Desktop/SalomeTraining/ahmedBody')

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
model.addParameter(Part_1_doc, "angle", '35')

### Create Sketch
Sketch_1 = model.addSketch(Part_1_doc, model.defaultPlane("XOY"))

### Create SketchProjection
SketchProjection_1 = Sketch_1.addProjection(model.selection("EDGE", "PartSet/OY"), False)
SketchLine_1 = SketchProjection_1.createdFeature()
SketchLine_1.setName("SketchLine_2")
SketchLine_1.result().setName("SketchLine_2")

### Create SketchLine
SketchLine_2 = Sketch_1.addLine(1.044, 1.387778780781446e-16, 0, 0)
SketchLine_2.setName("SketchLine_3")
SketchLine_2.result().setName("SketchLine_3")
Sketch_1.setCoincident(SketchAPI_Line(SketchLine_1).startPoint(), SketchLine_2.endPoint())

### Create SketchLine
SketchLine_3 = Sketch_1.addLine(0, 0, -2.168404344971009e-19, 0.2880000000000001)
SketchLine_3.setName("SketchLine_4")
SketchLine_3.result().setName("SketchLine_4")

### Create SketchLine
SketchLine_4 = Sketch_1.addLine(-2.168404344971009e-19, 0.2880000000000001, 0.844058713643238, 0.288)
SketchLine_4.setName("SketchLine_5")
SketchLine_4.result().setName("SketchLine_5")

### Create SketchLine
SketchLine_5 = Sketch_1.addLine(1.044, 0.147999604093649, 1.044, 1.387778780781446e-16)
SketchLine_5.setName("SketchLine_6")
SketchLine_5.result().setName("SketchLine_6")
Sketch_1.setCoincident(SketchLine_5.endPoint(), SketchLine_2.startPoint())
Sketch_1.setCoincident(SketchLine_2.endPoint(), SketchLine_3.startPoint())
Sketch_1.setCoincident(SketchLine_3.endPoint(), SketchLine_4.startPoint())
Sketch_1.setPerpendicular(SketchLine_2.result(), SketchLine_3.result())
Sketch_1.setPerpendicular(SketchLine_3.result(), SketchLine_4.result())
Sketch_1.setPerpendicular(SketchLine_4.result(), SketchLine_5.result())
Sketch_1.setHorizontal(SketchLine_4.result())

### Create SketchLine
SketchLine_6 = Sketch_1.addLine(0.844058713643238, 0.288, 1.044, 0.147999604093649)
SketchLine_6.setName("SketchLine_7")
SketchLine_6.result().setName("SketchLine_7")

### Create SketchConstraintAngle
Sketch_1.setAngle(SketchLine_6.result(), SketchLine_4.result(), "angle", type = "Supplementary")
Sketch_1.setCoincident(SketchLine_6.startPoint(), SketchLine_4.endPoint())
Sketch_1.setCoincident(SketchLine_6.endPoint(), SketchLine_5.startPoint())
model.do()

### Create Extrusion
Extrusion_1 = model.addExtrusion(Part_1_doc, [model.selection("FACE", "Sketch_1/Face-SketchLine_6r-SketchLine_7r-SketchLine_5r-SketchLine_4r-SketchLine_3r")], model.selection(), 0, 0.389, "Faces|Wires")

### Create Fillet
Fillet_1 = model.addFillet(Part_1_doc, [model.selection("FACE", "Extrusion_1_1/Generated_Face&Sketch_1/SketchLine_4")], 0.1, 0.1, keepSubResults = True)

### Create Rotation
Rotation_1 = model.addRotation(Part_1_doc, [model.selection("SOLID", "Fillet_1_1")], axis = model.selection("EDGE", "PartSet/OX"), angle = 90, keepSubResults = True)

### Create Sketch
Sketch_2 = model.addSketch(Part_1_doc, model.selection("FACE", "Rotation_1_1/MF:Rotated&Sketch_1/SketchLine_3"))

### Create SketchLine
SketchLine_7 = Sketch_2.addLine(4.575005998161249e-34, -0.031, 0.202, -0.031)
SketchLine_7.setName("SketchLine_8")
SketchLine_7.result().setName("SketchLine_8")
SketchLine_7.setAuxiliary(True)

### Create SketchProjection
SketchProjection_2 = Sketch_2.addProjection(model.selection("EDGE", "PartSet/OY"), False)
SketchLine_8 = SketchProjection_2.createdFeature()
SketchLine_8.setName("SketchLine_9")
SketchLine_8.result().setName("SketchLine_9")
Sketch_2.setCoincident(SketchLine_7.startPoint(), SketchLine_8.result())
Sketch_2.setHorizontal(SketchLine_7.result())
Sketch_2.setHorizontalDistance(SketchLine_7.startPoint(), SketchLine_7.endPoint(), 0.202)

### Create SketchProjection
SketchProjection_3 = Sketch_2.addProjection(model.selection("EDGE", "[Rotation_1_1/MF:Rotated&Extrusion_1_1/To_Face][Rotation_1_1/MF:Rotated&Sketch_1/SketchLine_3]"), False)
SketchLine_9 = SketchProjection_3.createdFeature()
SketchLine_9.setName("SketchLine_11")
SketchLine_9.result().setName("SketchLine_11")

### Create SketchProjection
SketchProjection_4 = Sketch_2.addProjection(model.selection("EDGE", "[Rotation_1_1/MF:Rotated&Extrusion_1_1/From_Face][Rotation_1_1/MF:Rotated&Sketch_1/SketchLine_3]"), False)
SketchLine_10 = SketchProjection_4.createdFeature()
SketchLine_10.setName("SketchLine_12")
SketchLine_10.result().setName("SketchLine_12")

### Create SketchPoint
SketchPoint_1 = Sketch_2.addPoint(0.202, -0.031)
Sketch_2.setCoincident(SketchLine_7.endPoint(), SketchPoint_1.coordinates())

### Create SketchPoint
SketchPoint_2 = Sketch_2.addPoint(0.202591375249664, 0)
Sketch_2.setCoincident(SketchPoint_2.coordinates(), SketchLine_9.result())
Sketch_2.setVerticalDistance(SketchPoint_2.coordinates(), SketchPoint_1.coordinates(), 0.031)

### Create SketchLine
SketchLine_11 = Sketch_2.addLine(0.202591375249664, 0, 0.202591375249664, -0.1444352572872336)
SketchLine_11.setName("SketchLine_13")
SketchLine_11.result().setName("SketchLine_13")
SketchLine_11.setAuxiliary(True)
Sketch_2.setCoincident(SketchPoint_2.coordinates(), SketchLine_11.startPoint())
Sketch_2.setVertical(SketchLine_11.result())

### Create SketchPoint
SketchPoint_3 = Sketch_2.addPoint(0.202591375249664, -0.062)
Sketch_2.setCoincident(SketchPoint_3.coordinates(), SketchLine_11.result())
Sketch_2.setVerticalDistance(SketchPoint_3.coordinates(), SketchPoint_1.coordinates(), 0.031)

### Create SketchCircle
SketchCircle_1 = Sketch_2.addCircle(0.202591375249664, -0.062, 0.03)
Sketch_2.setCoincident(SketchPoint_3.coordinates(), SketchCircle_1.center())
Sketch_2.setRadius(SketchCircle_1.results()[1], 0.03)

### Create SketchLine
SketchLine_12 = Sketch_2.addLine(1.044, -0.1945, 2.870447311749558e-33, -0.1945)
SketchLine_12.setName("SketchLine_14")
SketchLine_12.result().setName("SketchLine_14")
SketchLine_12.setAuxiliary(True)

### Create SketchProjection
SketchProjection_5 = Sketch_2.addProjection(model.selection("EDGE", "[Rotation_1_1/MF:Rotated&Sketch_1/SketchLine_3][Rotation_1_1/MF:Rotated&Sketch_1/SketchLine_6]"), False)
SketchLine_13 = SketchProjection_5.createdFeature()
SketchLine_13.setName("SketchLine_15")
SketchLine_13.result().setName("SketchLine_15")
Sketch_2.setCoincident(SketchLine_12.startPoint(), SketchLine_13.result())
Sketch_2.setCoincident(SketchLine_12.endPoint(), SketchLine_8.result())
Sketch_2.setHorizontal(SketchLine_12.result())
Sketch_2.setVerticalDistance(SketchLine_12.startPoint(), SketchAPI_Line(SketchLine_9).startPoint(), 0.1945)

### Create SketchLine
SketchLine_14 = Sketch_2.addLine(0.202591375249664, -0.062, 0.6725913752496639, -0.062)
SketchLine_14.setName("SketchLine_16")
SketchLine_14.result().setName("SketchLine_16")
SketchLine_14.setAuxiliary(True)
Sketch_2.setCoincident(SketchPoint_3.coordinates(), SketchLine_14.startPoint())
Sketch_2.setHorizontal(SketchLine_14.result())
Sketch_2.setHorizontalDistance(SketchLine_14.endPoint(), SketchPoint_2.coordinates(), 0.47)

### Create SketchMultiTranslation
SketchMultiTranslation_1 = Sketch_2.addTranslation([SketchCircle_1.results()[1]], SketchPoint_3.coordinates(), SketchLine_14.endPoint(), 2)
[SketchCircle_2] = SketchMultiTranslation_1.translatedList()

### Create SketchConstraintMirror
SketchConstraintMirror_1 = Sketch_2.addMirror(SketchLine_12.result(), [SketchCircle_2.results()[1], SketchCircle_1.results()[1]])
[SketchCircle_3, SketchCircle_4] = SketchConstraintMirror_1.mirrored()
model.do()

### Create Extrusion
Extrusion_2_objects = [model.selection("FACE", "Sketch_2/Face-SketchCircle_2_2f"),
                       model.selection("FACE", "Sketch_2/Face-SketchCircle_1_2f"),
                       model.selection("FACE", "Sketch_2/Face-SketchCircle_4_2f"),
                       model.selection("FACE", "Sketch_2/Face-SketchCircle_3_2f")]
Extrusion_2 = model.addExtrusion(Part_1_doc, Extrusion_2_objects, model.selection(), 0.05, 0, "Faces|Wires")

model.end()

###
### SHAPERSTUDY component
###

model.publishToShaperStudy()
import SHAPERSTUDY
Rotation_1_1, = SHAPERSTUDY.shape(model.featureStringId(Rotation_1))
Extrusion_2_1, = SHAPERSTUDY.shape(model.featureStringId(Extrusion_2))
Extrusion_2_2, = SHAPERSTUDY.shape(model.featureStringId(Extrusion_2, 1))
Extrusion_2_3, = SHAPERSTUDY.shape(model.featureStringId(Extrusion_2, 2))
Extrusion_2_4, = SHAPERSTUDY.shape(model.featureStringId(Extrusion_2, 3))

if salome.sg.hasDesktop():
  salome.sg.updateObjBrowser()
