import numpy as np
from graphics import *
from time import sleep

## Create a 1000 pixel x 1000 pixel graphics window
win = GraphWin("My Stage", 1000, 1000,autoflush=False)
## Give it a white background
win.setBackground("white")

## Give window coordinates from (-3,-3) to (3,3)
win.setCoords(-3, -3, 3, 3)

## Projection matrix takes a 3-d vector (x,y,z) and projects to 2-d (x',y')
projector1 = np.array([(1,0,0.2),
                       (0,1,0.2)])

## Create the axes
axisx = np.array([(-2,0,0),(2,0,0)])
axisy = np.array([(0,-2,0),(0,2,0)])
axisz = np.array([(0,0,-2),(0,0,2)])
## Project the axes
projectedaxisx = np.transpose(projector1.dot(np.transpose(axisx)))
projectedaxisy = np.transpose(projector1.dot(np.transpose(axisy)))
projectedaxisz = np.transpose(projector1.dot(np.transpose(axisz)))

## Plot the axes
lineaxisx = Line(Point(projectedaxisx[0,0],projectedaxisx[0,1]),Point(projectedaxisx[1,0],projectedaxisx[1,1]))
lineaxisx.draw(win)
lineaxisx.setOutline('gray')
lineaxisx.setFill('gray')
loclabelaxisx = lineaxisx.getP2()
labelaxisx = Text(loclabelaxisx, "x")
labelaxisx.draw(win)

lineaxisy = Line(Point(projectedaxisy[0,0],projectedaxisy[0,1]),Point(projectedaxisy[1,0],projectedaxisy[1,1]))
lineaxisy.draw(win)
lineaxisy.setOutline('gray')
lineaxisy.setFill('gray')
loclabelaxisy = lineaxisy.getP2()
labelaxisy = Text(loclabelaxisy, "y")
labelaxisy.draw(win)

lineaxisz = Line(Point(projectedaxisz[0,0],projectedaxisz[0,1]),Point(projectedaxisz[1,0],projectedaxisz[1,1]))
lineaxisz.draw(win)
lineaxisz.setOutline('gray')
lineaxisz.setFill('gray')
loclabelaxisz = lineaxisz.getP2()
labelaxisz = Text(loclabelaxisz, "z")
labelaxisz.draw(win)


## Set initial rotation
gamma = 0
beta  = 0
alpha = 0

## Creat the initial cube
cube = np.array([(-1,-1,-1), (1,-1,-1), (1,1,-1), (-1,1,-1),
                 (-1,-1,1), (1,-1,1), (1,1,1), (-1,1,1)])

## Loop
while True:
## for C in range (0,1000):

    ## Project the current cube from 3-space to 2-space
    projectedcube = np.transpose(projector1.dot(np.transpose(cube)))

    # Label the vertices (doesn't work when the cube is spinning)
    # for T in range(0,8):
    #     point = Point(projectedcube[T,0],projectedcube[T,1])
    #     cir = Circle(point,0.1)
    #     cir.draw(win)
    #     lab = Text(point,T)
    #     lab.draw(win)

    print(cube)
    print(projectedcube)

    ## Set the line color by the average z-depth of the two end points
    gray1  = ((cube[0,2] + cube[1,2])/2 + np.sqrt(2))/(2*np.sqrt(2)) * 255
    gray2  = ((cube[0,2] + cube[3,2])/2 + np.sqrt(2))/(2*np.sqrt(2)) * 255
    gray3  = ((cube[0,2] + cube[4,2])/2 + np.sqrt(2))/(2*np.sqrt(2)) * 255
    gray4  = ((cube[2,2] + cube[1,2])/2 + np.sqrt(2))/(2*np.sqrt(2)) * 255
    gray5  = ((cube[2,2] + cube[3,2])/2 + np.sqrt(2))/(2*np.sqrt(2)) * 255
    gray6  = ((cube[2,2] + cube[6,2])/2 + np.sqrt(2))/(2*np.sqrt(2)) * 255
    gray7  = ((cube[5,2] + cube[1,2])/2 + np.sqrt(2))/(2*np.sqrt(2)) * 255
    gray8  = ((cube[5,2] + cube[4,2])/2 + np.sqrt(2))/(2*np.sqrt(2)) * 255
    gray9  = ((cube[5,2] + cube[6,2])/2 + np.sqrt(2))/(2*np.sqrt(2)) * 255    
    gray10 = ((cube[7,2] + cube[3,2])/2 + np.sqrt(2))/(2*np.sqrt(2)) * 255
    gray11 = ((cube[7,2] + cube[4,2])/2 + np.sqrt(2))/(2*np.sqrt(2)) * 255
    gray12 = ((cube[7,2] + cube[6,2])/2 + np.sqrt(2))/(2*np.sqrt(2)) * 255

    # Define and draw the twelve edges for the projected cube
    line1 = Line(Point(projectedcube[0,0],projectedcube[0,1]),Point(projectedcube[1,0],projectedcube[1,1]) )
    line1.setOutline(color_rgb(gray1,gray1,gray1))
    line1.draw(win)
    line2 = Line(Point(projectedcube[0,0],projectedcube[0,1]),Point(projectedcube[3,0],projectedcube[3,1]) )
    line2.setOutline(color_rgb(gray2,gray2,gray2))
    line2.draw(win)
    line3 = Line(Point(projectedcube[0,0],projectedcube[0,1]),Point(projectedcube[4,0],projectedcube[4,1]) )
    line3.setOutline(color_rgb(gray3,gray3,gray3))
    line3.draw(win)
        
    line4 = Line(Point(projectedcube[2,0],projectedcube[2,1]),Point(projectedcube[1,0],projectedcube[1,1]) )
    line4.setOutline(color_rgb(gray4,gray4,gray4))   
    line4.draw(win)
    line5 = Line(Point(projectedcube[2,0],projectedcube[2,1]),Point(projectedcube[3,0],projectedcube[3,1]) )
    line5.setOutline(color_rgb(gray5,gray5,gray5))
    line5.draw(win)
    line6 = Line(Point(projectedcube[2,0],projectedcube[2,1]),Point(projectedcube[6,0],projectedcube[6,1]) )
    line6.setOutline(color_rgb(gray6,gray6,gray6))
    line6.draw(win)
    
    line7 = Line(Point(projectedcube[5,0],projectedcube[5,1]),Point(projectedcube[1,0],projectedcube[1,1]) )
    line7.setOutline(color_rgb(gray7,gray7,gray7))
    line7.draw(win)
    line8 = Line(Point(projectedcube[5,0],projectedcube[5,1]),Point(projectedcube[4,0],projectedcube[4,1]) )
    line8.setOutline(color_rgb(gray8,gray8,gray8))
    line8.draw(win)
    line9 = Line(Point(projectedcube[5,0],projectedcube[5,1]),Point(projectedcube[6,0],projectedcube[6,1]) )
    line9.setOutline(color_rgb(gray9,gray9,gray9))
    line9.draw(win)

    line10 = Line(Point(projectedcube[7,0],projectedcube[7,1]),Point(projectedcube[3,0],projectedcube[3,1]) )
    line10.setOutline(color_rgb(gray10,gray10,gray10))
    line10.draw(win)
    line11 = Line(Point(projectedcube[7,0],projectedcube[7,1]),Point(projectedcube[4,0],projectedcube[4,1]) )
    line11.setOutline(color_rgb(gray11,gray11,gray11))
    line11.draw(win)
    line12 = Line(Point(projectedcube[7,0],projectedcube[7,1]),Point(projectedcube[6,0],projectedcube[6,1]) )
    line12.setOutline(color_rgb(gray12,gray12,gray12))
    line12.draw(win)

    ##  Set pitch, yaw, and roll rates
    gamma = gamma + np.pi/6000
    beta = beta + np.pi/36000
    alpha = alpha + np.pi/36000

    ## Compute the rotation matrices
    Rx = np.array([(1 ,0,                        0),            
                   (0 ,np.cos(gamma),-np.sin(gamma)),
                   (0 ,np.sin(gamma),np.cos(gamma))])
    
    Ry = np.array([(np.cos(beta) ,0, np.sin(beta)),
                   (0            ,1,            0),          
                   (-np.sin(beta),0, np.cos(beta))])
        
    Rz = np.array([(np.cos(alpha) ,-np.sin(alpha), 0),
                   (np.sin(alpha),np.cos(alpha),0),
                   (0,0, 1)])

    ## Rotate the cube
    cube = np.transpose(np.matmul(Rz,np.matmul(Ry,np.matmul(Rx,np.transpose(cube)))))

    update()
    for item in [line1,line2,line3,line4,line5,line6,line7,line8,line9,line10,line11,line12]:
        item.undraw()
    sleep(0.1)
