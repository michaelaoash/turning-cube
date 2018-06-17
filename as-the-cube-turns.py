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
## Oblique orthonormal
projector1 = np.array([(1,0,0.2),
                       (0,1,0.2)])

## homogeneous coordinates
# projector2 = np.array([(1, 0, 0, 0),
#                        (0, 1, 0, 0),
#                        (0, 0, 1, 0),
#                        (0, 0,-1, 0)])

projector2 = np.array([(1, 0, 0.2, 0),
                       (0, 1, 0.2, 0),
                       (0, 0, 1, 0),
                       (0, 0,-1, 0)])

def project2(a):
    return np.matmul(projector2,np.append(a,1))[0:2] / ((10 - np.matmul(projector2,np.append(a,1))[3])/10.)


## Create the axes
axisx1 = np.array([-2,0,0])
axisx2 = np.array([2,0,0])
axisy1 = np.array([0,-2,0])
axisy2 = np.array([0,2,0])
axisz1 = np.array([0,0,-2])
axisz2 = np.array([0,0,2])

projectedaxisx1 = np.matmul(projector1,axisx1)
projectedaxisx2 = np.matmul(projector1,axisx2)
projectedaxisy1 = np.matmul(projector1,axisy1)
projectedaxisy2 = np.matmul(projector1,axisy2)
projectedaxisz1 = np.matmul(projector1,axisz1)
projectedaxisz2 = np.matmul(projector1,axisz2)

projectedaxisx1 = project2(axisx1)
projectedaxisx2 = project2(axisx2) 
projectedaxisy1 = project2(axisy1)
projectedaxisy2 = project2(axisy2)
projectedaxisz1 = project2(axisz1)
projectedaxisz2 = project2(axisz2)


## Plot the axes
lineaxisx = Line(Point(projectedaxisx1[0],projectedaxisx1[1]),Point(projectedaxisx2[0],projectedaxisx2[1]))
lineaxisx.draw(win)
lineaxisx.setOutline('gray')
lineaxisx.setFill('gray')
loclabelaxisx = lineaxisx.getP2()
labelaxisx = Text(loclabelaxisx, "x")
labelaxisx.draw(win)

lineaxisy = Line(Point(projectedaxisy1[0],projectedaxisy1[1]),Point(projectedaxisy2[0],projectedaxisy2[1]))
lineaxisy.draw(win)
lineaxisy.setOutline('gray')
lineaxisy.setFill('gray')
loclabelaxisy = lineaxisy.getP2()
labelaxisy = Text(loclabelaxisy, "y")
labelaxisy.draw(win)

lineaxisz = Line(Point(projectedaxisz1[0],projectedaxisz1[1]),Point(projectedaxisz2[0],projectedaxisz2[1]))
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

## Create the initial cube with vertices A-H
cubeA = np.array([-1,-1,-1])
cubeB = np.array([1,-1,-1]) 
cubeC = np.array([1,1,-1])  
cubeD = np.array([-1,1,-1])
cubeE = np.array([-1,-1,1])
cubeF = np.array([1,-1,1])  
cubeG = np.array([1,1,1])   
cubeH = np.array([-1,1,1])   

## Loop
while True:
## for C in range (0,1000):

    ## Project the current cube from 3-space to 2-space with oblique projection
    projectedcubeA = np.matmul(projector1,cubeA)
    projectedcubeB = np.matmul(projector1,cubeB)
    projectedcubeC = np.matmul(projector1,cubeC)
    projectedcubeD = np.matmul(projector1,cubeD)
    projectedcubeE = np.matmul(projector1,cubeE)
    projectedcubeF = np.matmul(projector1,cubeF)
    projectedcubeG = np.matmul(projector1,cubeG)
    projectedcubeH = np.matmul(projector1,cubeH)

    ## Project the current cube from 3-space to 2-space with homogeneous coordinates
    projectedcubeA = project2(cubeA)
    projectedcubeB = project2(cubeB)
    projectedcubeC = project2(cubeC)
    projectedcubeD = project2(cubeD)
    projectedcubeE = project2(cubeE)
    projectedcubeF = project2(cubeF)
    projectedcubeG = project2(cubeG)
    projectedcubeH = project2(cubeH)


    # Label the vertices (doesn't work when the cube is spinning)
    # for T in range(0,8):
    #     point = Point(projectedcube[T,0],projectedcube[T,1])
    #     cir = Circle(point,0.1)
    #     cir.draw(win)
    #     lab = Text(point,T)
    #     lab.draw(win)

    def gray(point1,point2):
        return int(((point1[2] + point2[2])/2 + np.sqrt(2))/(2*np.sqrt(2)) * 255)
    
    ## Set the line color by the average z-depth of the two end points
    gray1  = gray(cubeA,cubeB) ;
    gray2  = gray(cubeA,cubeD) ;
    gray3  = gray(cubeA,cubeE) ;
    gray4  = gray(cubeC,cubeB) ;
    gray5  = gray(cubeC,cubeD) ;
    gray6  = gray(cubeC,cubeG) ;
    gray7  = gray(cubeF,cubeB) ;
    gray8  = gray(cubeF,cubeB) ;
    gray9  = gray(cubeF,cubeB) ;
    gray10 = gray(cubeH,cubeB) ;
    gray11 = gray(cubeH,cubeB) ;
    gray12 = gray(cubeH,cubeB) ;
    

    # Define and draw the twelve edges for the projected cube
    line1 = Line(Point(projectedcubeA[0],projectedcubeA[1]),Point(projectedcubeB[0],projectedcubeB[1]) )
    line1.setOutline(color_rgb(gray1,gray1,gray1))
    line1.draw(win)
    line2 = Line(Point(projectedcubeA[0],projectedcubeA[1]),Point(projectedcubeD[0],projectedcubeD[1]) )
    line2.setOutline(color_rgb(gray2,gray2,gray2))
    line2.draw(win)
    line3 = Line(Point(projectedcubeA[0],projectedcubeA[1]),Point(projectedcubeE[0],projectedcubeE[1]) )
    line3.setOutline(color_rgb(gray3,gray3,gray3))
    line3.draw(win)
        
    line4 = Line(Point(projectedcubeC[0],projectedcubeC[1]),Point(projectedcubeB[0],projectedcubeB[1]) )
    line4.setOutline(color_rgb(gray4,gray4,gray4))   
    line4.draw(win)
    line5 = Line(Point(projectedcubeC[0],projectedcubeC[1]),Point(projectedcubeD[0],projectedcubeD[1]) )
    line5.setOutline(color_rgb(gray5,gray5,gray5))
    line5.draw(win)
    line6 = Line(Point(projectedcubeC[0],projectedcubeC[1]),Point(projectedcubeG[0],projectedcubeG[1]) )
    line6.setOutline(color_rgb(gray6,gray6,gray6))
    line6.draw(win)
    
    line7 = Line(Point(projectedcubeF[0],projectedcubeF[1]),Point(projectedcubeB[0],projectedcubeB[1]) )
    line7.setOutline(color_rgb(gray7,gray7,gray7))
    line7.draw(win)
    line8 = Line(Point(projectedcubeF[0],projectedcubeF[1]),Point(projectedcubeE[0],projectedcubeE[1]) )
    line8.setOutline(color_rgb(gray8,gray8,gray8))
    line8.draw(win)
    line9 = Line(Point(projectedcubeF[0],projectedcubeF[1]),Point(projectedcubeG[0],projectedcubeG[1]) )
    line9.setOutline(color_rgb(gray9,gray9,gray9))
    line9.draw(win)

    line10 = Line(Point(projectedcubeH[0],projectedcubeH[1]),Point(projectedcubeD[0],projectedcubeD[1]) )
    line10.setOutline(color_rgb(gray10,gray10,gray10))
    line10.draw(win)
    line11 = Line(Point(projectedcubeH[0],projectedcubeH[1]),Point(projectedcubeE[0],projectedcubeE[1]) )
    line11.setOutline(color_rgb(gray11,gray11,gray11))
    line11.draw(win)
    line12 = Line(Point(projectedcubeH[0],projectedcubeH[1]),Point(projectedcubeG[0],projectedcubeG[1]) )
    line12.setOutline(color_rgb(gray12,gray12,gray12))
    line12.draw(win)

    ##  Set pitch, yaw, and roll rates
    gamma = gamma + np.pi/6000
    # beta = beta + np.pi/36000
    # alpha = alpha + np.pi/36000

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
    cubeA = np.matmul(Rz,np.matmul(Ry,np.matmul(Rx,(cubeA))))
    cubeB = np.matmul(Rz,np.matmul(Ry,np.matmul(Rx,(cubeB))))
    cubeC = np.matmul(Rz,np.matmul(Ry,np.matmul(Rx,(cubeC))))
    cubeD = np.matmul(Rz,np.matmul(Ry,np.matmul(Rx,(cubeD))))
    cubeE = np.matmul(Rz,np.matmul(Ry,np.matmul(Rx,(cubeE))))
    cubeF = np.matmul(Rz,np.matmul(Ry,np.matmul(Rx,(cubeF))))
    cubeG = np.matmul(Rz,np.matmul(Ry,np.matmul(Rx,(cubeG))))
    cubeH = np.matmul(Rz,np.matmul(Ry,np.matmul(Rx,(cubeH))))
    
    update()
    for item in [line1,line2,line3,line4,line5,line6,line7,line8,line9,line10,line11,line12]:
        item.undraw()
    sleep(0.1)
