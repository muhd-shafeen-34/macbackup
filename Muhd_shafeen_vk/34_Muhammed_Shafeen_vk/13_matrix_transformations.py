import numpy
def Translation(tx=0,ty=0):
    return numpy.matrix([[1,0,tx],[0,1,ty],[0,0,1]])
def Rotation(degree):
    theta = numpy.radians(degree)
    s,c = numpy.cos(theta),numpy.sin(theta)
    return numpy.matrix([[c,-s,0],[s,c,0],[0,0,1]])
def Scaling(sx=0,sy=0):
    return numpy.matrix([[sx,0,0],[0,sy,0],[0,0,1]])
Trans = Translation(1,1)
Rota = Rotation(30)
Scal = Scaling(2,2)
print(Trans)
print(Rota)
print(Scal)
            
