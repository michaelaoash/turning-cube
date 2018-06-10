import numpy as np
from graphics import *

win.close()

win = GraphWin("My Stage", 1000, 1000)

win.setCoords(-3, -3, 3, 3)

projector1 = np.array([(1,0,0.2),(0,1,0.2)])

axisx = np.array([(-2,0,0),(2,0,0)])
axisy = np.array([(0,-2,0),(0,2,0)])
axisz = np.array([(0,0,-2),(0,0,2)])
projectedaxisx = np.transpose(projector1.dot(np.transpose(axisx)))
projectedaxisy = np.transpose(projector1.dot(np.transpose(axisy)))
projectedaxisz = np.transpose(projector1.dot(np.transpose(axisz)))

## rotator = np.array([])

cube = np.array([(-1,-1,-1), (1,-1,-1), (1,1,-1), (-1,1,-1),
                 (-1,-1,1), (1,-1,1), (1,1,1), (-1,1,1)])
projectedcube = np.transpose(projector1.dot(np.transpose(cube)))


for T in range(0,8):
    point = Point(projectedcube[T,0],projectedcube[T,1])
    point.draw(win)
    cir = Circle(point,0.1)
    cir.draw(win)
    lab = Text(point,T)
    lab.draw(win)
    
line = Line(Point(projectedcube[0,0],projectedcube[0,1]),Point(projectedcube[1,0],projectedcube[1,1]) )
line.draw(win)
line = Line(Point(projectedcube[0,0],projectedcube[0,1]),Point(projectedcube[3,0],projectedcube[3,1]) )
line.draw(win)
line = Line(Point(projectedcube[0,0],projectedcube[0,1]),Point(projectedcube[4,0],projectedcube[4,1]) )
line.draw(win)

line = Line(Point(projectedcube[2,0],projectedcube[2,1]),Point(projectedcube[1,0],projectedcube[1,1]) )
line.draw(win)
line = Line(Point(projectedcube[2,0],projectedcube[2,1]),Point(projectedcube[3,0],projectedcube[3,1]) )
line.draw(win)
line = Line(Point(projectedcube[2,0],projectedcube[2,1]),Point(projectedcube[6,0],projectedcube[6,1]) )
line.draw(win)

line = Line(Point(projectedcube[5,0],projectedcube[5,1]),Point(projectedcube[1,0],projectedcube[1,1]) )
line.draw(win)
line = Line(Point(projectedcube[5,0],projectedcube[5,1]),Point(projectedcube[4,0],projectedcube[4,1]) )
line.draw(win)
line = Line(Point(projectedcube[5,0],projectedcube[5,1]),Point(projectedcube[6,0],projectedcube[6,1]) )
line.draw(win)

line = Line(Point(projectedcube[7,0],projectedcube[7,1]),Point(projectedcube[3,0],projectedcube[3,1]) )
line.draw(win)
line = Line(Point(projectedcube[7,0],projectedcube[7,1]),Point(projectedcube[4,0],projectedcube[4,1]) )
line.draw(win)
line = Line(Point(projectedcube[7,0],projectedcube[7,1]),Point(projectedcube[6,0],projectedcube[6,1]) )
line.draw(win)


line = Line(Point(projectedaxisx[0,0],projectedaxisx[0,1]),Point(projectedaxisx[1,0],projectedaxisx[1,1]))
line.draw(win)
line.setOutline('gray')
line.setFill('gray')
line = Line(Point(projectedaxisy[0,0],projectedaxisy[0,1]),Point(projectedaxisy[1,0],projectedaxisy[1,1]))
line.draw(win)
line.setOutline('gray')
line.setFill('gray')
line = Line(Point(projectedaxisz[0,0],projectedaxisz[0,1]),Point(projectedaxisz[1,0],projectedaxisz[1,1]))
line.draw(win)
line.setOutline('gray')
line.setFill('gray')


## Code for earlier looping problems
# for T in range(1, 5, 1):
#     line = Line(Point(1,T+2),Point(9,T) )
#     line.draw(win)
# for T in range(5,1,-1):
#     line = Line(Point(2,T+1),Point(9,T+1) )
#     line.draw(win)
# b = 10*np.random.random((10,2)) + 1

