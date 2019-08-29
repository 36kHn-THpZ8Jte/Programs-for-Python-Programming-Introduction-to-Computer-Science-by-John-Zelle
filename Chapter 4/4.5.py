# Program 4.5
# See Excel file for computations
# by Scott Pellicane

from graphics import *

def main():
    win = GraphWin("Straight", 300*1.618, 300)
    win.setCoords(0, 0, 300*1.618, 300)
    win.setBackground("gold")

######### 45 about y ##############
######### 45 about x ##############

######### Die Vertices ############

    p1 = Point(-35.36+50,-17.68+200)
    p2 = Point(0+50,-42.68+200)
    p3 = Point(0+50,-7.32+200)
    p4 = Point(-35.36+50,17.68+200)
    p5 = Point(0+50,42.68+200)
    p6 = Point(35.36+50,17.68+200)
    p7 = Point(35.36+50,-17.68+200)
    p8 = Point(0+50,7.32+200)

######### Face 1 With One Pip #####

    f1 = Polygon(p1,p2,p3,p4)
    f1.setOutline("gray")
    f1.setFill("white")
    f1.draw(win)

    q1 = Point(-21.21+50,-13.54+200)
    q2 = Point(-21.21+50,-6.46+200)
    q3 = Point(-14.14+50,-11.46+200)
    q4 = Point(-14.14+50,-18.54+200)

    pip_1 = Polygon(q1,q2,q3,q4)
    pip_1.setFill("black")
    pip_1.draw(win)

######### Face 2 With Two Pips #####

    f2 = Polygon(p3,p4,p5,p6)
    f2.setOutline("gray")
    f2.setFill("white")
    f2.draw(win)

    r1 = Point(14.14+50,17.68+200)
    r2 = Point(21.21+50,12.68+200)
    r3 = Point(28.28+50,17.68+200)
    r4 = Point(21.21+50,22.68+200)

    pip_1 = Polygon(r1,r2,r3,r4)
    pip_1.setFill("black")
    pip_1.draw(win)

    s1 = Point(-14.14+50,17.68+200)
    s2 = Point(-21.21+50,22.68+200)
    s3 = Point(-28.28+50,17.68+200)
    s4 = Point(-21.21+50,12.68+200)

    pip_2 = Polygon(s1,s2,s3,s4)
    pip_2.setFill("black")
    pip_2.draw(win)

######### Face 3 With Three Pips #####

    f3 = Polygon(p2,p3,p6,p7)
    f3.setOutline("gray")
    f3.setFill("white")
    f3.draw(win)

    t1 = Point(10.61+50,-24.57+200)
    t2 = Point(3.54+50,-29.57+200)
    t3 = Point(3.54+50,-36.64+200)
    t4 = Point(10.61+50,-31.64+200)

    pip_1 = Polygon(t1,t2,t3,t4)
    pip_1.setFill("black")
    pip_1.draw(win)

    u1 = Point(21.21+50,-6.46+200)
    u2 = Point(14.14+50,-11.46+200)
    u3 = Point(14.14+50,-18.54+200)
    u4 = Point(21.21+50,-13.54+200)

    pip_2 = Polygon(u1,u2,u3,u4)
    pip_2.setFill("black")
    pip_2.draw(win)

    v1 = Point(24.75+50,-0.43+200)
    v2 = Point(31.82+50,4.57+200)
    v3 = Point(31.82+50,11.64+200)
    v4 = Point(24.75+50,6.64+200)

    pip_3 = Polygon(v1,v2,v3,v4)
    pip_3.setFill("black")
    pip_3.draw(win)

######### 90 about x ##############
######### 30 about y ##############
######### 45 about x ##############   

######### Die Vertices ############

    p1 = Point(-9.15+125,6.47+110)
    p2 = Point(34.15+125,-11.21+110)
    p3 = Point(9.15+125,-41.83+110)
    p4 = Point(-34.15+125,-24.15+110)
    p5 = Point(-34.15+125,11.21+110)
    p6 = Point(9.15+125,-6.47+110)
    p7 = Point(34.15+125,24.15+110)
    p8 = Point(-9.15+125,41.83+110)

######### Face 2 With Two Pips ####

    f2 = Polygon(p3,p4,p5,p6)
    f2.setOutline("gray")
    f2.setFill("white")
    f2.draw(win)

    r1 = Point(-3.84+125,-11.77+110)
    r2 = Point(4.82+125,-15.31+110)
    r3 = Point(4.82+125,-8.24+110)
    r4 = Point(-3.84+125,-4.70+110)

    pip_1 = Polygon(r1,r2,r3,r4)
    pip_1.setFill("black")
    pip_1.draw(win)

    s1 = Point(-21.16+125,-18.84+110)
    s2 = Point(-29.82+125,-15.31+110)
    s3 = Point(-29.82+125,-22.38+110)
    s4 = Point(-21.16+125,-25.92+110)

    pip_2 = Polygon(s1,s2,s3,s4)
    pip_2.setFill("black")
    pip_2.draw(win)

######### Face 3 With Three Pips ##

    f3 = Polygon(p2,p3,p6,p7)
    f3.setOutline("gray")
    f3.setFill("white")
    f3.draw(win)

    t1 = Point(26.65+125,-9.79+110)
    t2 = Point(26.65+125,-16.86+110)
    t3 = Point(31.65+125,-10.73+110)
    t4 = Point(31.65+125,-3.66+110)

    pip_1 = Polygon(t1,t2,t3,t4)
    pip_1.setFill("black")
    pip_1.draw(win)

    u1 = Point(19.15+125,-8.37+110)
    u2 = Point(19.15+125,-15.44+110)
    u3 = Point(24.15+125,-9.31+110)
    u4 = Point(24.15+125,-2.24+110)

    pip_2 = Polygon(u1,u2,u3,u4)
    pip_2.setFill("black")
    pip_2.draw(win)

    v1 = Point(16.65+125,-7.89+110)
    v2 = Point(16.65+125,-0.82+110)
    v3 = Point(11.65+125,-6.94+110)
    v4 = Point(11.65+125,-14.02+110)

    pip_3 = Polygon(v1,v2,v3,v4)
    pip_3.setFill("black")
    pip_3.draw(win)

######### Face 6 With Six Pips ####

    f6 = Polygon(p5,p6,p7,p8)
    f6.setOutline("gray")
    f6.setFill("white")
    f6.draw(win)

    w1 = Point(3.66+125,8.02+110)
    w2 = Point(12.32+125,4.48+110)
    w3 = Point(7.32+125,-1.64+110)
    w4 = Point(-1.34+125,1.89+110)

    pip_1 = Polygon(w1,w2,w3,w4)
    pip_1.setFill("black")
    pip_1.draw(win)

    x1 = Point(-3.66+125,27.34+110)
    x2 = Point(-12.32+125,30.87+110)
    x3 = Point(-7.32+125,37+110)
    x4 = Point(1.34+125,33.46+110)

    pip_2 = Polygon(x1,x2,x3,x4)
    pip_2.setFill("black")
    pip_2.draw(win)

    y1 = Point(-13.66+125,15.09+110)
    y2 = Point(-22.32+125,18.63+110)
    y3 = Point(-27.32+125,12.50+110)
    y4 = Point(-18.66+125,8.97+110)

    pip_3 = Polygon(y1,y2,y3,y4)
    pip_3.setFill("black")
    pip_3.draw(win)

    z1 = Point(13.66+125,20.27+110)
    z2 = Point(22.32+125,16.73+110)
    z3 = Point(27.32+125,22.85+110)
    z4 = Point(18.66+125,26.39+110)

    pip_4 = Polygon(z1,z2,z3,z4)
    pip_4.setFill("black")
    pip_4.draw(win)

    a1 = Point(11.16+125,17.20+110)
    a2 = Point(6.16+125,11.08+110)
    a3 = Point(14.82+125,7.54+110)
    a4 = Point(19.82+125,13.67+110)

    pip_5 = Polygon(a1,a2,a3,a4)
    pip_5.setFill("black")
    pip_5.draw(win)

    b1 = Point(-6.16+125,24.28+110)
    b2 = Point(-11.16+125,18.15+110)
    b3 = Point(-19.82+125,21.69+110)
    b4 = Point(-14.82+125,27.81+110)

    pip_6 = Polygon(b1,b2,b3,b4)
    pip_6.setFill("black")
    pip_6.draw(win)

######### 90 about z ##############
######### 60 about y ##############
######### 45 about x ##############   

######### Die Vertices ############

    p1 = Point(-9.15+225,-41.83+180)
    p2 = Point(-9.15+225,-6.47+180)
    p3 = Point(-34.15+225,24.15+180)
    p4 = Point(-34.15+225,-11.21+180)
    p5 = Point(9.15+225,6.47+180)
    p6 = Point(9.15+225,41.83+180)
    p7 = Point(34.15+225,11.21+180)
    p8 = Point(34.15+225,-24.15+180)

######### Face 1 With One Pip #####

    f1 = Polygon(p1,p2,p3,p4)
    f1.setOutline("gray")
    f1.setFill("white")
    f1.draw(win)

    r1 = Point(-19.15+225,-15.44+180)
    r2 = Point(-24.15+225,-9.31+180)
    r3 = Point(-24.15+225,-2.24+180)
    r4 = Point(-19.15+225,-8.37+180)

    pip_1 = Polygon(r1,r2,r3,r4)
    pip_1.setFill("black")
    pip_1.draw(win)

######### Face 3 With Three Pips ##

    f3 = Polygon(p2,p3,p6,p7)
    f3.setOutline("gray")
    f3.setFill("white")
    f3.draw(win)

    t1 = Point(-3.66+225,8.02+180)
    t2 = Point(-12.32+225,4.48+180)
    t3 = Point(-7.32+225,-1.64+180)
    t4 = Point(1.34+225,1.89+180)

    pip_1 = Polygon(t1,t2,t3,t4)
    pip_1.setFill("black")
    pip_1.draw(win)

    u1 = Point(1.83+225,22.51+180)
    u2 = Point(-6.83+225,18.97+180)
    u3 = Point(-1.83+225,12.85+180)
    u4 = Point(6.83+225,16.38+180)

    pip_2 = Polygon(u1,u2,u3,u4)
    pip_2.setFill("black")
    pip_2.draw(win)

    v1 = Point(3.66+225,27.34+180)
    v2 = Point(12.32+225,30.87+180)
    v3 = Point(7.32+225,37+180)
    v4 = Point(-1.34+225,33.46+180)

    pip_3 = Polygon(v1,v2,v3,v4)
    pip_3.setFill("black")
    pip_3.draw(win)

######### Face 4 With Four Pips ###

    f4 = Polygon(p1,p2,p7,p8)
    f4.setOutline("gray")
    f4.setFill("white")
    f4.draw(win)

    w1 = Point(21.16+225,-4.70+180)
    w2 = Point(21.16+225,2.37+180)
    w3 = Point(29.82+225,5.90+180)
    w4 = Point(29.82+225,-1.17+180)

    pip_1 = Polygon(w1,w2,w3,w4)
    pip_1.setFill("black")
    pip_1.draw(win)

    x1 = Point(3.84+225,-25.92+180)
    x2 = Point(3.84+225,-32.99+180)
    x3 = Point(-4.82+225,-36.52+180)
    x4 = Point(-4.82+225,-29.45+180)

    pip_2 = Polygon(x1,x2,x3,x4)
    pip_2.setFill("black")
    pip_2.draw(win)

    y1 = Point(21.16+225,-18.84+180)
    y2 = Point(21.16+225,-25.92+180)
    y3 = Point(29.82+225,-22.38+180)
    y4 = Point(29.82+225,-15.31+180)

    pip_3 = Polygon(y1,y2,y3,y4)
    pip_3.setFill("black")
    pip_3.draw(win)

    z1 = Point(3.84+225,-11.77+180)
    z2 = Point(3.84+225,-4.70+180)
    z3 = Point(-4.82+225,-8.24+180)
    z4 = Point(-4.82+225,-15.31+180)

    pip_4 = Polygon(z1,z2,z3,z4)
    pip_4.setFill("black")
    pip_4.draw(win)

######### -90 about z ##############
######### 36 about y ##############
######### 45 about x ##############   

######### Die Vertices ############

    p1 = Point(-34.92+400,13.77+225)
    p2 = Point(-34.92+400,-21.59+225)
    p3 = Point(5.53+400,-42.37+225)
    p4 = Point(5.53+400,-7.01+225)
    p5 = Point(34.92+400,21.59+225)
    p6 = Point(34.92+400,-13.77+225)
    p7 = Point(-5.53+400,7.01+225)
    p8 = Point(-5.53+400,42.37+225)

######### Face 1 With One Pip #####

    f1 = Polygon(p1,p2,p3,p4)
    f1.setOutline("gray")
    f1.setFill("white")
    f1.draw(win)

    r1 = Point(-18.74+400,-8.69+150)
    r2 = Point(-10.65+400,-12.84+150)
    r3 = Point(-10.65+400,-19.92+150)
    r4 = Point(-18.74+400,-15.76+150)

    pip_1 = Polygon(r1,r2,r3,r4)
    pip_1.setFill("black")
    pip_1.draw(win)

######### Face 2 With Two Pips ####

    f2 = Polygon(p3,p4,p5,p6)
    f2.setOutline("gray")
    f2.setFill("white")
    f2.draw(win)

    t1 = Point(26.1+400,-11.74+150)
    t2 = Point(26.1+400,-18.81+150)
    t3 = Point(31.98+400,-13.09+150)
    t4 = Point(31.98+400,-6.02+150)

    pip_1 = Polygon(t1,t2,t3,t4)
    pip_1.setFill("black")
    pip_1.draw(win)

    u1 = Point(14.35+400,-9.04+150)
    u2 = Point(14.35+400,-1.97+150)
    u3 = Point(8.47+400,-7.69+150)
    u4 = Point(8.47+400,-14.76+150)

    pip_2 = Polygon(u1,u2,u3,u4)
    pip_2.setFill("black")
    pip_2.draw(win)

######### Face 5 With Five Pips ###

    f5 = Polygon(p1,p4,p5,p8)
    f5.setOutline("gray")
    f5.setFill("white")
    f5.draw(win)

    w1 = Point(13.97+400,19.24+150)
    w2 = Point(22.06+400,15.09+150)
    w3 = Point(27.94+400,20.81+150)
    w4 = Point(19.85+400,24.96+150)

    pip_1 = Polygon(w1,w2,w3,w4)
    pip_1.setFill("black")
    pip_1.draw(win)

    x1 = Point(-13.97+400,16.11+150)
    x2 = Point(-22.06+400,20.27+150)
    x3 = Point(-27.94+400,14.55+150)
    x4 = Point(-19.85+400,10.39+150)

    pip_2 = Polygon(x1,x2,x3,x4)
    pip_2.setFill("black")
    pip_2.draw(win)

    y1 = Point(-2.21+400,27.56+150)
    y2 = Point(-10.3+400,31.71+150)
    y3 = Point(-4.42+400,37.43+150)
    y4 = Point(3.67+400,33.28+150)

    pip_3 = Polygon(y1,y2,y3,y4)
    pip_3.setFill("black")
    pip_3.draw(win)

    z1 = Point(2.21+400,7.8+150)
    z2 = Point(10.3+400,3.64+150)
    z3 = Point(4.42+400,-2.08+150)
    z4 = Point(-3.67+400,2.08+150)

    pip_4 = Polygon(z1,z2,z3,z4)
    pip_4.setFill("black")
    pip_4.draw(win)

    a1 = Point(-6.98+400,16.9+150)
    a2 = Point(1.11+400,12.74+150)
    a3 = Point(6.98+400,18.46+150)
    a4 = Point(-1.11+400,22.62+150)

    pip_5 = Polygon(a1,a2,a3,a4)
    pip_5.setFill("black")
    pip_5.draw(win)

######### 180 about x #############
######### 30 about y ##############
######### 45 about x ##############

######### Die Vertices ############

    p1 = Point(-9.15+450,41.83+150)
    p2 = Point(34.15+450,24.15+150)
    p3 = Point(34.15+450,-11.21+150)
    p4 = Point(-9.15+450,6.47+150)
    p5 = Point(-34.15+450,-24.15+150)
    p6 = Point(9.15+450,-41.83+150)
    p7 = Point(9.15+450,-6.47+150)
    p8 = Point(-34.15+450,11.21+150)

######### Face 3 With Three Pips ##

    f3 = Polygon(p2,p3,p6,p7)
    f3.setOutline("gray")
    f3.setFill("white")
    f3.draw(win)

##    t1 = Point(-3.66+300,8.02+150)
##    t2 = Point(-12.32+300,4.48+150)
##    t3 = Point(-7.32+300,-1.64+150)
##    t4 = Point(1.34+300,1.89+150)
##
##    pip_1 = Polygon(t1,t2,t3,t4)
##    pip_1.setFill("black")
##    pip_1.draw(win)
##
##    u1 = Point(1.83+300,22.51+150)
##    u2 = Point(-6.83+300,18.97+150)
##    u3 = Point(-1.83+300,12.85+150)
##    u4 = Point(6.83+300,16.38+150)
##
##    pip_2 = Polygon(u1,u2,u3,u4)
##    pip_2.setFill("black")
##    pip_2.draw(win)
##
##    v1 = Point(3.66+300,27.34+150)
##    v2 = Point(12.32+300,30.87+150)
##    v3 = Point(7.32+300,37+150)
##    v4 = Point(-1.34+300,33.46+150)
##
##    pip_3 = Polygon(v1,v2,v3,v4)
##    pip_3.setFill("black")
##    pip_3.draw(win)

######### Face 4 With Four Pips ###

    f4 = Polygon(p1,p2,p7,p8)
    f4.setOutline("gray")
    f4.setFill("white")
    f4.draw(win)

##    w1 = Point(21.16+300,-4.70+150)
##    w2 = Point(21.16+300,2.37+150)
##    w3 = Point(29.82+300,5.90+150)
##    w4 = Point(29.82+300,-1.17+150)
##
##    pip_1 = Polygon(w1,w2,w3,w4)
##    pip_1.setFill("black")
##    pip_1.draw(win)
##
##    x1 = Point(3.84+300,-25.92+150)
##    x2 = Point(3.84+300,-32.99+150)
##    x3 = Point(-4.82+300,-36.52+150)
##    x4 = Point(-4.82+300,-29.45+150)
##
##    pip_2 = Polygon(x1,x2,x3,x4)
##    pip_2.setFill("black")
##    pip_2.draw(win)
##
##    y1 = Point(21.16+300,-18.84+150)
##    y2 = Point(21.16+300,-25.92+150)
##    y3 = Point(29.82+300,-22.38+150)
##    y4 = Point(29.82+300,-15.31+150)
##
##    pip_3 = Polygon(y1,y2,y3,y4)
##    pip_3.setFill("black")
##    pip_3.draw(win)
##
##    z1 = Point(3.84+300,-11.77+150)
##    z2 = Point(3.84+300,-4.70+150)
##    z3 = Point(-4.82+300,-8.24+150)
##    z4 = Point(-4.82+300,-15.31+150)
##
##    pip_4 = Polygon(z1,z2,z3,z4)
##    pip_4.setFill("black")
##    pip_4.draw(win)

######### Face 6 With Six Pips ####

    f6 = Polygon(p5,p6,p7,p8)
    f6.setOutline("gray")
    f6.setFill("white")
    f6.draw(win)

##    w1 = Point(3.66+200,8.02+150)
##    w2 = Point(12.32+200,4.48+150)
##    w3 = Point(7.32+200,-1.64+150)
##    w4 = Point(-1.34+200,1.89+150)
##
##    pip_1 = Polygon(w1,w2,w3,w4)
##    pip_1.setFill("black")
##    pip_1.draw(win)
##
##    x1 = Point(-3.66+200,27.34+150)
##    x2 = Point(-12.32+200,30.87+150)
##    x3 = Point(-7.32+200,37+150)
##    x4 = Point(1.34+200,33.46+150)
##
##    pip_2 = Polygon(x1,x2,x3,x4)
##    pip_2.setFill("black")
##    pip_2.draw(win)
##
##    y1 = Point(-13.66+200,15.09+150)
##    y2 = Point(-22.32+200,18.63+150)
##    y3 = Point(-27.32+200,12.50+150)
##    y4 = Point(-18.66+200,8.97+150)
##
##    pip_3 = Polygon(y1,y2,y3,y4)
##    pip_3.setFill("black")
##    pip_3.draw(win)
##
##    z1 = Point(13.66+200,20.27+150)
##    z2 = Point(22.32+200,16.73+150)
##    z3 = Point(27.32+200,22.85+150)
##    z4 = Point(18.66+200,26.39+150)
##
##    pip_4 = Polygon(z1,z2,z3,z4)
##    pip_4.setFill("black")
##    pip_4.draw(win)
##
##    a1 = Point(11.16+200,17.20+150)
##    a2 = Point(6.16+200,11.08+150)
##    a3 = Point(14.82+200,7.54+150)
##    a4 = Point(19.82+200,13.67+150)
##
##    pip_5 = Polygon(a1,a2,a3,a4)
##    pip_5.setFill("black")
##    pip_5.draw(win)
##
##    b1 = Point(-6.16+200,24.28+150)
##    b2 = Point(-11.16+200,18.15+150)
##    b3 = Point(-19.82+200,21.69+150)
##    b4 = Point(-14.82+200,27.81+150)
##
##    pip_6 = Polygon(b1,b2,b3,b4)
##    pip_6.setFill("black")
##    pip_6.draw(win)




    
main()
