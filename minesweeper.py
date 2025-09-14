import turtle
import random
G = turtle.Turtle()
Z = turtle.Screen()

turtle.screensize(2000, 2000)

G.hideturtle()
G.speed(0)

bombs = []
bombs1 = []
zeros = []
numbers = []
bombplacementnumbers = []
wincondition = []
bombsdrawn = []

cordinates = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

Cordinates1 = [[30, 510], [90, 510], [150, 510], [210, 510], [270, 510], [330, 510], [390, 510], [450, 510], [510, 510],                                         [30, 450], [90, 450], [150, 450], [210, 450], [270, 450], [330, 450], [390, 450], [450, 450], [510, 450],                                         [30, 390], [90, 390], [150, 390], [210, 390], [270, 390], [330, 390], [390, 390], [450, 390], [510, 390],                                         [30, 330], [90, 330], [150, 330], [210, 330], [270, 330], [330, 330], [390, 330], [450, 330], [510, 330],                                         [30, 270], [90, 270], [150, 270], [210, 270], [270, 270], [330, 270], [390, 270], [450, 270], [510, 270],                                         [30, 210], [90, 210], [150, 210], [210, 210], [270, 210], [330, 210], [390, 210], [450, 210], [510, 210],                                         [30, 150], [90, 150], [150, 150], [210, 150], [270, 150], [330, 150], [390, 150], [450, 150], [510, 150],                                         [30, 90], [90, 90], [150, 90], [210, 90], [270, 90], [330, 90], [390, 90], [450, 90], [510, 90],                                                  [30, 30], [90, 30], [150, 30], [210, 30], [270, 30], [330, 30], [390, 30], [450, 30], [510, 30]]

firstclicklist = []
Z.bgcolor("navy")

def field():
  G.color("yellow")
  G.forward(540)
  G.goto(0, 0)
  for x in range(9):
   for x in range(9):
     G.begin_fill()
     G.color("yellow")
     G.left(90)
     G.forward(60)
     G.right(90)
     G.forward(60)
     G.right(90)
     G.forward(60)
     G.color("black")
     G.end_fill()
     G.left(90)
   G.penup()
   G.left(180)
   G.forward(540)
   G.right(180)
   G.left(90)
   G.forward(60)
   G.right(90)
   G.pendown()

def randomnumber():
  r = random.randint(0, 80)
  if ((r in bombplacementnumbers) or (Cordinates1[r] in firstclickfield)):
    randomnumber()
  else:
    bombplacementnumbers.append(r)  
    global r1
    r1 = r

def bombplacement(n):
  for x in range(n):
    randomnumber()
    bombs.append(Cordinates1[r1])
    bombs1.append(r1)

def customizedbombplacement():
  bombsamount = int(input("How many mines would you like to include in the field?:"))
  if (bombsamount < 0):
    print("incompatable range, please enter a higher value.")
    customizedbombplacement()
  if (bombsamount > 72):
    print("incompatable range, please enter a lower value.")
    customizedbombplacement()
  else:
    global ba
    ba = bombsamount


#customizedbombplacement()

#Predefines the ba variabal due to the input console not being accesible through the community page. If you would like to enable the ability to manually chose the amount of bombs, simply remove "ba = 10", and the hastag infront of customizedbombplacement().
ba = 10

def bombsadjecent(x, y):
  bombsadjecent = 0
  if [x, (y + 60)] in bombs:
    bombsadjecent = bombsadjecent + 1
  if [x, (y - 60)] in bombs:
     bombsadjecent = bombsadjecent + 1
  if [(x + 60), y] in bombs:
     bombsadjecent = bombsadjecent + 1
  if [(x - 60), y] in bombs:
     bombsadjecent = bombsadjecent + 1
  if [(x - 60), (y + 60)] in bombs:
     bombsadjecent = bombsadjecent + 1
  if [(x - 60), (y - 60)] in bombs:
     bombsadjecent = bombsadjecent + 1
  if [(x + 60), (y + 60)] in bombs:
     bombsadjecent = bombsadjecent + 1
  if [(x + 60), (y - 60)] in bombs:
     bombsadjecent = bombsadjecent + 1
  return bombsadjecent

def bombsadjecentcheck():
  for x in range(81):
    z = Cordinates1[x]
    g = bombsadjecent(z[0], z[1])
    cordinates[x] = g

def bombplacement1():
  for x in range(len(bombs1)):
    cordinates[(bombs1[x])] = "M"

def zerosandnumberscheck():
 for x in range(81):
   if (cordinates[x] == 0):
     zeros.append(Cordinates1[x])
   if (cordinates[x] != 0) and (cordinates[x] != ("M")):
     numbers.append(Cordinates1[x])

def wingame():
  Z.bgcolor("lawngreen")
  for x in range(len(Cordinates1)):
    u = Cordinates1[x]
    cordinatesdraw(u[0], u[1])
  print("You have won.")

def losegame():
  Z.bgcolor("red")
  for x in range(len(Cordinates1)):
    u = Cordinates1[x]
    cordinatesdraw(u[0], u[1])
  print("You have lost.")

def numberdraw(x, y, z):
  if (([x, y]) in wincondition):
    return
  else:
   wincondition.append([x, y])
  G.penup()
  G.goto((x - 30), (y - 30))
  G.color("yellow")
  G.pendown()
  G.begin_fill()
  G.forward(60)
  G.left(90)
  G.forward(60)
  G.left(90)
  G.forward(60)
  G.left(90)
  G.forward(60)
  G.left(90)
  if (z == 0):
    G.color("grey")
  else:
   G.color("white")
  G.end_fill()
  G.color("black")
  G.penup()
  G.goto(x, y)
  if (z != 0):
   if (z == 1):
     G.color("lime")
   if (z == 2):
     G.color("green")
   if (z == 3):
     G.color("orange")
   if (z == 4):
     G.color("red")
   if (z > 4):
     G.color("pink")
   G.write(z, font=("Verdana", 20), align=("center"))
  if (len(wincondition) >= (81 - ba) and (len(bombsdrawn) == 0)):
    wingame()

def bombdraw(x, y):
  G.penup()
  G.goto((x - 30), (y - 30))
  G.color("yellow")
  G.pendown()
  G.begin_fill()
  G.forward(60)
  G.left(90)
  G.forward(60)
  G.left(90)
  G.forward(60)
  G.left(90)
  G.forward(60)
  G.left(90)
  G.color("white")
  G.end_fill()

  G.color("black")
  G.penup()
  G.goto((x - 20), (y - 20))
  G.pendown
  G.forward(40)
  G.hideturtle()
  G.left(90)
  G.begin_fill()
  G.circle(20, 180)
  G.end_fill()
  G.penup()
  G.goto(x, y)
  G.right(180)
  G.right(90)
  G.pendown()
  G.color("red")
  G.begin_fill()
  G.circle(2)
  G.end_fill()
  G.color("black")
  bombsdrawn.append(1)
  if ((len(bombsdrawn) < 2) and (len(wincondition) < (81 - ba))):
    losegame()

def zeroadejecentcheck(x, y):
  if [x, (y + 60)] in zeros:
    zeros.remove([x, (y + 60)])
    numberdraw(x, (y + 60), 0)
    zeroadejecentcheck(x, (y + 60))
  if [x, (y + 60)] in numbers:
    numbers.remove([x, (y + 60)])
    i = Cordinates1.index([x, (y + 60)])
    numberdraw(x, (y + 60), cordinates[i])

  if [x, (y - 60)] in zeros:
    zeros.remove([x, (y - 60)])
    numberdraw(x, (y - 60), 0)
    zeroadejecentcheck(x, (y - 60))
  if [x, (y - 60)] in numbers:
    numbers.remove([x, (y - 60)])
    i = Cordinates1.index([x, (y - 60)])
    numberdraw(x, (y - 60), cordinates[i])

  if [(x + 60), y] in zeros:
    zeros.remove([(x + 60), y])
    numberdraw((x + 60), y, 0)
    zeroadejecentcheck((x + 60), y)
  if [(x + 60), y] in numbers:
    numbers.remove([(x + 60), y])
    i = Cordinates1.index([(x + 60), y])
    numberdraw((x + 60), y, cordinates[i])

  if [(x - 60), y] in zeros:
    zeros.remove([(x - 60), y])
    numberdraw((x - 60), y, 0)
    zeroadejecentcheck((x - 60), y)
  if [(x - 60), y] in numbers:
    numbers.remove([(x - 60), y])
    i = Cordinates1.index([(x - 60), y])
    numberdraw((x - 60), y, cordinates[i])

  if [(x - 60), (y + 60)] in zeros:
    zeros.remove([(x - 60), (y + 60)])
    numberdraw((x - 60), (y + 60), 0)
    zeroadejecentcheck((x - 60), (y + 60))
  if [(x - 60), (y + 60)] in numbers:
    numbers.remove([(x - 60), (y + 60)])
    i = Cordinates1.index([(x - 60), (y + 60)])
    numberdraw((x - 60), (y + 60), cordinates[i])

  if [(x - 60), (y - 60)] in zeros:
    zeros.remove([(x - 60), (y - 60)])
    numberdraw((x - 60), (y - 60), 0)
    zeroadejecentcheck((x - 60), (y - 60))
  if [(x - 60), (y - 60)] in numbers:
    numbers.remove([(x - 60), (y - 60)])
    i = Cordinates1.index([(x - 60), (y - 60)])
    numberdraw((x - 60), (y - 60), cordinates[i])

  if [(x + 60), (y + 60)] in zeros:
    zeros.remove([(x + 60), (y + 60)])
    numberdraw((x + 60), (y + 60), 0)
    zeroadejecentcheck((x + 60), (y + 60))
  if [(x + 60), (y + 60)] in numbers:
    numbers.remove([(x + 60), (y + 60)])
    i = Cordinates1.index([(x + 60), (y + 60)])
    numberdraw((x + 60), (y + 60), cordinates[i])

  if [(x + 60), (y - 60)] in zeros:
    zeros.remove([(x + 60), (y - 60)])
    numberdraw((x + 60), (y - 60), 0)
    zeroadejecentcheck((x + 60), (y - 60))
  if [(x + 60), (y - 60)] in numbers:
    numbers.remove([(x + 60), (y - 60)])
    i = Cordinates1.index([(x + 60), (y - 60)])
    numberdraw((x + 60), (y - 60), cordinates[i])

def cordinatesdraw(clickx1, clicky1):
  firstclicklist.append(clickx1)
  if (len(firstclicklist) == 1):
    for z in range(81):
     u = Cordinates1[z]
     if ((u[0] + 30) > clickx1 > (u[0] - 30)) and ((u[1] + 30) > clicky1 > (u[1] - 30)):
       global firstclickfield
       firstclickfield = [Cordinates1[z], [(u[0] + 60), u[1]], [(u[0] - 60), u[1]], [u[0], (u[1] + 60)], [u[0], (u[1] - 60)], [(u[0] + 60), (u[1] + 60)], [(u[0] + 60), (u[1] - 60)], [(u[0] - 60), (u[1] + 60)], [(u[0] - 60), (u[1] - 60)]]
       bombplacement(ba)
       bombsadjecentcheck()
       bombplacement1()
       zerosandnumberscheck()
       numberdraw(u[0], u[1], cordinates[z])
       zeroadejecentcheck(u[0], u[1])
  else:
   for z in range(81):
     u = Cordinates1[z]
     if ((u[0] + 30) > clickx1 > (u[0] - 30)) and ((u[1] + 30) > clicky1 > (u[1] - 30)):
       if Cordinates1[z] in bombs:
         bombdraw(u[0], u[1])
       elif (cordinates[z] == 0):
         numberdraw(u[0], u[1], cordinates[z])
         zeroadejecentcheck(u[0], u[1])
       else:
         numberdraw(u[0], u[1], cordinates[z])

def cordinatesclick(x1, y1):
  clickx = x1
  clicky = y1
  cordinatesdraw(clickx, clicky)




field()
Z.onscreenclick(cordinatesclick)