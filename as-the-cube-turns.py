import numpy as np
from Tkinter import *
from graphics import *
from time import sleep


## Set up sliders to control rotation
master = Tk()
w1 = Scale(master, from_=-60, to=60, orient=HORIZONTAL,label='pitch')
w1.set(0)
w1.pack()
w2 = Scale(master, from_=-60, to=60, orient=HORIZONTAL,label='yaw')
w2.set(0)
w2.pack()
w3 = Scale(master, from_=-60, to=60, orient=HORIZONTAL,label='roll')
w3.set(0)
w3.pack()



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
vertexA = np.array([-1,-1,-1])
vertexB = np.array([1,-1,-1]) 
vertexC = np.array([1,1,-1])  
vertexD = np.array([-1,1,-1])
vertexE = np.array([-1,-1,1])
vertexF = np.array([1,-1,1])  
vertexG = np.array([1,1,1])   
vertexH = np.array([-1,1,1])   

## Loop
while True:
## for C in range (0,1000):

    ## Project the current cube from 3-space to 2-space with oblique projection
    projectedvertexA = np.matmul(projector1,vertexA)
    projectedvertexB = np.matmul(projector1,vertexB)
    projectedvertexC = np.matmul(projector1,vertexC)
    projectedvertexD = np.matmul(projector1,vertexD)
    projectedvertexE = np.matmul(projector1,vertexE)
    projectedvertexF = np.matmul(projector1,vertexF)
    projectedvertexG = np.matmul(projector1,vertexG)
    projectedvertexH = np.matmul(projector1,vertexH)

    ## Project the current cube from 3-space to 2-space with homogeneous coordinates
    projectedvertexA = project2(vertexA)
    projectedvertexB = project2(vertexB)
    projectedvertexC = project2(vertexC)
    projectedvertexD = project2(vertexD)
    projectedvertexE = project2(vertexE)
    projectedvertexF = project2(vertexF)
    projectedvertexG = project2(vertexG)
    projectedvertexH = project2(vertexH)


    # Label the vertices (doesn't work when the cube is spinning)
    # for T in range(0,8):
    #     point = Point(projectedvertex[T,0],projectedvertex[T,1])
    #     cir = Circle(point,0.1)
    #     cir.draw(win)
    #     lab = Text(point,T)
    #     lab.draw(win)

    def gray(point1,point2):
        return int(((point1[2] + point2[2])/2 + np.sqrt(2))/(2*np.sqrt(2)) * 255)
    
    ## Set the line color by the average z-depth of the two end points
    gray1  = gray(vertexA,vertexB) ;
    gray2  = gray(vertexA,vertexD) ;
    gray3  = gray(vertexA,vertexE) ;
    gray4  = gray(vertexC,vertexB) ;
    gray5  = gray(vertexC,vertexD) ;
    gray6  = gray(vertexC,vertexG) ;
    gray7  = gray(vertexF,vertexB) ;
    gray8  = gray(vertexF,vertexB) ;
    gray9  = gray(vertexF,vertexB) ;
    gray10 = gray(vertexH,vertexB) ;
    gray11 = gray(vertexH,vertexB) ;
    gray12 = gray(vertexH,vertexB) ;
    

    # Define and draw the twelve edges for the projected cube
    line1 = Line(Point(projectedvertexA[0],projectedvertexA[1]),Point(projectedvertexB[0],projectedvertexB[1]) )
    line1.setOutline(color_rgb(gray1,gray1,gray1))
    line1.draw(win)
    line2 = Line(Point(projectedvertexA[0],projectedvertexA[1]),Point(projectedvertexD[0],projectedvertexD[1]) )
    line2.setOutline(color_rgb(gray2,gray2,gray2))
    line2.draw(win)
    line3 = Line(Point(projectedvertexA[0],projectedvertexA[1]),Point(projectedvertexE[0],projectedvertexE[1]) )
    line3.setOutline(color_rgb(gray3,gray3,gray3))
    line3.draw(win)
        
    line4 = Line(Point(projectedvertexC[0],projectedvertexC[1]),Point(projectedvertexB[0],projectedvertexB[1]) )
    line4.setOutline(color_rgb(gray4,gray4,gray4))   
    line4.draw(win)
    line5 = Line(Point(projectedvertexC[0],projectedvertexC[1]),Point(projectedvertexD[0],projectedvertexD[1]) )
    line5.setOutline(color_rgb(gray5,gray5,gray5))
    line5.draw(win)
    line6 = Line(Point(projectedvertexC[0],projectedvertexC[1]),Point(projectedvertexG[0],projectedvertexG[1]) )
    line6.setOutline(color_rgb(gray6,gray6,gray6))
    line6.draw(win)
    
    line7 = Line(Point(projectedvertexF[0],projectedvertexF[1]),Point(projectedvertexB[0],projectedvertexB[1]) )
    line7.setOutline(color_rgb(gray7,gray7,gray7))
    line7.draw(win)
    line8 = Line(Point(projectedvertexF[0],projectedvertexF[1]),Point(projectedvertexE[0],projectedvertexE[1]) )
    line8.setOutline(color_rgb(gray8,gray8,gray8))
    line8.draw(win)
    line9 = Line(Point(projectedvertexF[0],projectedvertexF[1]),Point(projectedvertexG[0],projectedvertexG[1]) )
    line9.setOutline(color_rgb(gray9,gray9,gray9))
    line9.draw(win)

    line10 = Line(Point(projectedvertexH[0],projectedvertexH[1]),Point(projectedvertexD[0],projectedvertexD[1]) )
    line10.setOutline(color_rgb(gray10,gray10,gray10))
    line10.draw(win)
    line11 = Line(Point(projectedvertexH[0],projectedvertexH[1]),Point(projectedvertexE[0],projectedvertexE[1]) )
    line11.setOutline(color_rgb(gray11,gray11,gray11))
    line11.draw(win)
    line12 = Line(Point(projectedvertexH[0],projectedvertexH[1]),Point(projectedvertexG[0],projectedvertexG[1]) )
    line12.setOutline(color_rgb(gray12,gray12,gray12))
    line12.draw(win)

    ##  Set pitch, yaw, and roll rates using the sliders
    gamma = w1.get()*np.pi/6000
    beta = w2.get()*np.pi/6000
    alpha = w3.get()*np.pi/6000

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
    vertexA = np.matmul(Rz,np.matmul(Ry,np.matmul(Rx,(vertexA))))
    vertexB = np.matmul(Rz,np.matmul(Ry,np.matmul(Rx,(vertexB))))
    vertexC = np.matmul(Rz,np.matmul(Ry,np.matmul(Rx,(vertexC))))
    vertexD = np.matmul(Rz,np.matmul(Ry,np.matmul(Rx,(vertexD))))
    vertexE = np.matmul(Rz,np.matmul(Ry,np.matmul(Rx,(vertexE))))
    vertexF = np.matmul(Rz,np.matmul(Ry,np.matmul(Rx,(vertexF))))
    vertexG = np.matmul(Rz,np.matmul(Ry,np.matmul(Rx,(vertexG))))
    vertexH = np.matmul(Rz,np.matmul(Ry,np.matmul(Rx,(vertexH))))
    
    update()
    for item in [line1,line2,line3,line4,line5,line6,line7,line8,line9,line10,line11,line12]:
        item.undraw()
    sleep(0.1)
