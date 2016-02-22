import os, time, math
import plotly
import plotly.plotly as py
import plotly.graph_objs as go
from os.path import join, basename, exists, isdir

INPUT_FILE_DIR = "input/"
OUTPUT_FILE_DIR = "output/"


def readguardsfile():
	inputFileName = "guards"
	infilename = os.path.join(INPUT_FILE_DIR, inputFileName + '.pol')
	outfilename = os.path.join(INPUT_FILE_DIR, inputFileName + '.sol')
	with open(infilename, 'r') as f:
		polygons = []
		for i in range(0,30):
			line = f.readline()
			line = line.rstrip()
			while not line.startswith(':'):
				line = line.lstrip("0123456789");
			line = line.lstrip(': ')
			polygons.append(line)
		polygonVertices = []
		for polygon in polygons:
			s = polygon
			vertices = []
			tempStr = ''
			inTuple = False
			j = 0
			while j < len(s):
				if s[j] == '(':
					inTuple = True
					tempStr += s[j]
				elif s[j] == ')':
					tempStr += s[j]
					vertices.append(tempStr)
					inTuple = False
					tempStr = ''
				elif inTuple:
					tempStr += s[j]
				j += 1
			polygonVertices.append(vertices)

		return polygonVertices

def readcheckfile():
	inputFileName = "check"
	infilename = os.path.join(INPUT_FILE_DIR, inputFileName + '.pol')
	outfilename = os.path.join(INPUT_FILE_DIR, inputFileName + '.sol')
	with open(infilename, 'r') as f:
		polygons = []
		for i in range(0,20):
			line = f.readline()
			line = line.rstrip()
			while not line.startswith(':'):
				line = line.lstrip("0123456789");
			line = line.lstrip(': ')
			polygons.append(line)
		polygonVertices = []
		guardCoordinates = []
		for polygon in polygons:
			s = polygon
			vertices = []
			guards = []
			tempStr = ''
			inTuple = False
			j = 0
			while j < len(s): #polygon vertices
				if s[j] == '(':
					inTuple = True
					tempStr += s[j]
				elif s[j] == ')':
					tempStr += s[j]
					vertices.append(tempStr)
					inTuple = False
					tempStr = ''
				elif inTuple:
					tempStr += s[j]
				elif s[j] == ';':
					break
				j += 1
			inTuple = False
			while j < len(s): #guard coordinates
				if s[j] == '(':
					inTuple = True
					tempStr += s[j]
				elif s[j] == ')':
					tempStr += s[j]
					guards.append(tempStr)
					inTuple = False
					tempStr = ''
				elif inTuple:
					tempStr += s[j]
				j += 1
			polygonVertices.append(vertices)
			guardCoordinates.append(guards)

		return polygonVertices, guardCoordinates

def get_polygon_XYlists(singlePolygon): #takes in one list of vertices for a selected polygon
	listLength = len(singlePolygon)
	Xlist = []
	Ylist = []
	for vertice in singlePolygon:
		coordinates = vertice.strip('()')
		coordinates = coordinates.split(',')
		x = coordinates[0]
		x = float(x)
		y = coordinates[1]
		y = float(y)
		Xlist.append(x)
		Ylist.append(y)
	firstVertice = singlePolygon[0]
	coordinates = firstVertice.strip('()')
	coordinates = coordinates.split(',')
	x = coordinates[0]
	x = float(x)
	y = coordinates[1]
	y = float(y)
	Xlist.append(x)
	Ylist.append(y)
	return Xlist, Ylist

def get_guards_XYlists(singlePolygon): #takes in one list of vertices for a selected polygon
	listLength = len(singlePolygon)
	Xlist = []
	Ylist = []
	for vertice in singlePolygon:
		coordinates = vertice.strip('()')
		coordinates = coordinates.split(',')
		x = coordinates[0]
		x = float(x)
		y = coordinates[1]
		y = float(y)
		Xlist.append(x)
		Ylist.append(y)
	return Xlist, Ylist

def plot(singlePolygon,guard):
	from plotly.graph_objs import Scatter, Layout
	aXlist, aYlist = get_polygon_XYlists(singlePolygon)
	bXlist, bYlist = get_guards_XYlists(guard)
	plotly.offline.plot({
	"data": [
    Scatter(x=aXlist, y=aYlist, fill='tozeroy'),
    Scatter(x=bXlist, y=bYlist, mode = 'markers')
	]
	})


#guardsPolygonVertices =  readguardsfile()
#a =  guardsPolygonVertices[7]
#plot(a)

checkPolygonVertices, checkGuardCoordinates = readcheckfile()
a = checkPolygonVertices[2]
b = checkGuardCoordinates[2]
plot(a,b)


print get_polygon_XYlists(b)
print get_guards_XYlists(c)
