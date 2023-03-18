import math
import matplotlib.pyplot as plt
def poss_position():
    L1 = 100
    L2 = 100
    x1 = []
    y1 = []
    x2 = []
    y2 = []
    line = []
    for i in range(180):
        rad1 = math.radians(i)
        x1.append(L1*math.cos(rad1))
        y1.append(L1*math.sin(rad1))
        for j in range(360):
            rad2 = math.radians(j)
            xnext = (L1*math.cos(rad1) + L2*math.cos(rad1+rad2))
           
            ynext = (L2*math.sin(rad1) + L2*math.sin(rad1+rad2))
            if ynext< 0:
                continue
            else:
                y2.append(ynext)
                x2.append(xnext)
    ##pt.plot(x2, y2)
    ##plt.show()l
    return x2, y2
x_poss, y_poss = poss_position()


x_des = input("Desired x position")
y_des = input("Desired y position")

if x_des in x_poss:
    if y_des in y_poss:
        print(f"Moving now to {x_des}, {y_des}")
    else:
        print(f"Not a valid y position")
else:
    print(f"Not a valid x position")