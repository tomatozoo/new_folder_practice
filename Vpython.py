from vpython import *
from time import *

#length = x, width = y, height = z
#vector 첫번째 칼럼 : 행은 정해져 있고, 열은 어디서 시작할 것인가? 물체의 좌우
#vector 두번째 칼럼 : 열은 정해져 있고, 행을 어디서 시작할 것인가? 물체의 높이
#vector 세번째 칼럼 : 물체를 정면(화면)에서 얼마나 멀리 둘 것인가? 

canvas(width=700, height=500, background=color.white)

floor = box(pos=vector(0,-4.15,0), color=color.green, length=10, height=.1, width=10)
#ceiling = box(pos = vector(0,5,0), color = color.white, length=10, height=.1, width=10)

ball = sphere(pos = vector(0,-2.5,0), color=color.red, length = 2, height = 2.5, width = 2)

hair1 = sphere(pos = vector(-.3,-1.15,0), color=color.green, radius =.2)
hair2 = sphere(pos = vector(0,-1.1,0), color=color.green, radius =.2)
hair3 = sphere(pos = vector(+.3,-1.15,0), color=color.green, radius =.2)

leg1 = cylinder(pos = vector(-0.3,-3.7,0), color=color.black, length=.17, width=.2, height=0.44)
leg2 = cylinder(pos = vector(+0.3,-3.7,0), color=color.black, length=.17, width=.2, height=0.44)
foot1 = sphere(pos = vector(-.24,-4,0), color=color.green, radius =.1)
foot2 = sphere(pos = vector(+.36,-4,0), color=color.green, radius =.1)

x = -0.8
y = +1
x2 = +0.7
y2 = +1

arm1 = cylinder(pos = vector(-0.3+x,-3.7+y,0), color=color.black, length=.17, width=.2, height=0.44)
arm2 = cylinder(pos = vector(+0.3+x2,-3.7+y2,0), color=color.black, length=.17, width=.2, height=0.44)
hand1 = sphere(pos = vector(-.24+x,-4+y,0), color=color.green, radius =.1)
hand2 = sphere(pos = vector(+.36+x2,-4+y2,0), color=color.green, radius =.1)


while True:
    pass


# 화면 레코드 : Ctrl+Alt+Shift+R
# box, ball, cylinder