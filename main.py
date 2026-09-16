# Welcome to RXO this is just OX in Rotation.


Board = {'c1': " ", "a": "A", "b": "B", "c": "C",
               "r1": "1", 1: "_", 2: "_", 3: "_",
               "r2": "2", 4: "_", 5: "_", 6: "_",
               "r3": "3", 7: "_", 8: "_", 9: "_"}




def printBoard():
   ca = 0
   global Board
   for i, j in Board.items():
       ca = ca+1
       print(j, end="   ")
       if ca == 4:
           print()
       if ca == 8:
           print()
       if ca == 12:
           print()
       if ca == 16:
           print()




def keys():
   global Board
   keyl = []
   keyl1 = []
   for key, val in Board.items():
       if val != "_":
           keyl.append(key)
   for i in range(1, 10):
       if i not in keyl:
           keyl1.append(i)
   return keyl1




def get_key(value):
   for key, val in Board.items():
       if val == value:
           return key




X1 = 0
X2 = 0
X3 = 0


O1 = 0
O2 = 0
O3 = 0




def Mo(a):
   global Board
   global X1
   global X2
   global X3
   global O1
   global O2
   global O3
   l = []
   if a == "X1":
       a = X1
   elif a == "X2":
       a = X2
   elif a == "X3":
       a = X3
   elif a == "O1":
       a = O1
   elif a == "O2":
       a = O2
   elif a == "O3":
       a = O3


   if a:
       c = a - 1
       d = a + 1
       if d < 10:
           if (d != 4) and (d != 7) and (Board[d] == "_"):
               l.append(d)
       if c > 0:
           if (c != 3) and (c != 6) and (Board[c] == "_"):
               l.append(c)
       if a < 7 and (Board[a + 3] == "_"):
           l.append(a + 3)
       if a > 3 and (Board[a - 3] == "_"):
           l.append(a - 3)
   return l


def draw():
   global Board
   global X1
   global X2
   global X3
   global O1
   global O2
   global O3
   b = [X1, X2, X3]
   k11 = [O1, O2, O3]
   cc = 0
   cw = 0
   for var in b:
       Mol = Mo(var)
       if Mol == None:
           cc = cc + 1
           print(Mol)
   for var1 in k11:
      MOL = Mo(var1)
      if MOL == None:
          cw = cw + 1
   if cc == 3 or cw == 3:
       return "Draw"
   else:
       cc = 0
       cw = 0
       return "con"




def Pla(place):
   print("you can place at...")
   for no in place:
       if no == 1:
           print("A1", end=", ")
       elif no == 2:
           print("B1", end=", ")
       elif no == 3:
           print("C1", end=", ")
       elif no == 4:
           print("A2", end=", ")
       elif no == 5:
           print("B2", end=", ")
       elif no == 6:
           print("C2", end=", ")
       elif no == 7:
           print("A3", end=", ")
       elif no == 8:
           print("B3", end=", ")
       elif no == 9:
           print("C3", end=" ")
   print()




def ce(Pce):
   if Pce == "A1":
       return 1
   elif Pce == "B1":
       return 2
   elif Pce == "C1":
       return 3
   elif Pce == "A2":
       return 4
   elif Pce == "B2":
       return 5
   elif Pce == "C2":
       return 6
   elif Pce == "A3":
       return 7
   elif Pce == "B3":
       return 8
   elif Pce == "C3":
       return 9
def Po(p, Place):
   global Board
   global X1
   global X2
   global X3
   global O1
   global O2
   global O3
   if p == 1:
       if Board[Place] == "_":
           Board[Place] = "X1"
           X1 = Place
   elif p == 2:
       if Board[Place] == "_":
           Board[Place] = "X2"
           X2 = Place
   elif p == 3:
       if Board[Place] == "_":
           Board[Place] = "X3"
           X3 = Place
   elif p == 4:
       if Board[Place] == "_":
           Board[Place] = "O1"
           O1 = Place
   elif p == 5:
       if Board[Place] == "_":
           Board[Place] = "O2"
           O2 = Place
   elif p == 6:
       if Board[Place] == "_":
           Board[Place] = "O3"
           O3 = Place
   else:
       print("Not available")




def Win(w):
   global Board
   global X1
   global X2
   global X3
   global O1
   global O2
   global O3
   Xl1 = [X1, X2, X3]
   Xl2 = [X2, X3, X1]
   Xl3 = [X3, X1, X2]
   Ol1 = [O1, O2, O3]
   Ol2 = [O2, O3, O1]
   Ol3 = [O3, O1, O2]
   winc =0
   if w == "X":
       for i in range(3):
           if Xl1[i] == Xl2[i] + 1 and Xl1[i] == Xl3[i] - 1:
               winc = winc + 1
           elif Xl1[i] == Xl2[i] + 4 and Xl1[i] == Xl3[i] - 4:
               winc = winc + 1
           elif Xl1[i] == Xl2[i] + 3 and Xl1[i] == Xl3[i] - 3:
               winc = winc + 1
       if winc >= 1:
           return "WinX"
       else:
           return "hi"
   elif w == "O":
       for i in range(3):
           if Ol1[i] == Ol2[i] + 1 and Ol1[i] == Ol3[i] - 1:
               winc = winc + 1
           elif Ol1[i] == Ol2[i] + 4 and Ol1[i] == Ol3[i] - 4:
               winc = winc + 1
           elif Ol1[i] == Ol2[i] + 3 and Ol1[i] == Ol3[i] - 3:
               winc = winc + 1
       if winc >= 1:
           return "WinO"
       else:
           return "HI"






def MoveX(Mee):
   global Board
   global X1
   global X2
   global X3
   global O1
   global O2
   global O3
   if Mee == 1:
        x = Mo(X1)
        Pla(x)
        y = input("Where do you want to move it:  ")
        k = int(ce(y))
        i = get_key("X1")
        Board[i] = "_"
        Board[k] = "X1"
        printBoard()
        X1 = k
   elif Mee == 2:
        x = Mo(X2)
        Pla(x)
        y = input("Where do you want to move it:  ")
        k = ce(y)
        i = get_key("X2")
        Board[i] = "_"
        Board[k] = "X2"
        printBoard()
        X2 = k
   elif Mee == 3:
        x = Mo(X3)
        Pla(x)
        y = input("Where do you want to move it:  ")
        k = ce(y)
        i = get_key("X3")
        Board[i] = "_"
        Board[k] = "X3"
        printBoard()
        X3 = k




def MoveO(Mee):
   global Board
   global X1
   global X2
   global X3
   global O1
   global O2
   global O3
   if Mee == 1:
       x = Mo(O1)
       Pla(x)
       y = input("Where do you want to move it:  ")
       k = int(ce(y))
       i = get_key("O1")
       Board[i] = "_"
       Board[k] = "O1"
       printBoard()
       O1 = k
   elif Mee == 2:
       x = Mo(O2)
       Pla(x)
       y = input("Where do you want to move it:  ")
       k = ce(y)
       i = get_key("O2")
       Board[i] = "_"
       Board[k] = "O2"
       printBoard()
       O2 = k
   elif Mee == 3:
       x = Mo(O3)
       Pla(x)
       y = input("Where do you want to move it:  ")
       k = ce(y)
       i = get_key("O3")
       Board[i] = "_"
       Board[k] = "O3"
       printBoard()
       O3 = k


running = True
c = 0
t1 = 1
t2 = 1
while running:
   if c%2 == 0:
       if t1 <= 3:
           p = int(input("what do you want to place: 1-X1, 2-X2, 3-X3:  "))
           place = keys()
           Pla(place)
           printBoard()
           Pce = input("where do you want to place")
           Place = int(ce(Pce))
           print(Place)
           Po(p, Place)
           printBoard()
           t1 = t1 + 1
           c = c + 1
       elif (t1 > 3) and (t1 <= 5):
           dra = draw()
           if dra == "Draw":
               break
           Mee = int(input("What do you want to move, 1-X1, 2-X2, 3-X3:  "))
           MoveX(Mee)
           t1 = t1 + 1
           c = c + 1
       elif t1 > 5:
           dra = draw()
           if dra == "Draw":
               break
           Mee = int(input("What do you want to move, 1-X1, 2-X2, 3-X3:  "))
           MoveX(Mee)
           wi = Win("X")
           if wi == "WinX":
               break
           t1 = t1 + 1
           c = c + 1
   else:
       if t2 <= 3:
           PO = int(input("what do you want to place: 1-O1, 2-O2, 3-O3"))
           PO = PO + 3
           plac = keys()
           Pla(plac)
           printBoard()
           Poo = input("where do you want to place")
           Plce = int(ce(Poo))
           print(Plce)
           Po(PO, Plce)
           printBoard()
           t2 = t2 + 1
           c = c + 1
       elif (t2 > 3) and (t2 <= 5):
           dra = draw()
           if dra == "Draw":
               break
           Mee = int(input("What do you want to move, 1-O1, 2-O2, 3-O3:  "))
           MoveO(Mee)
           t2 = t2 + 1
           c = c + 1
       elif t2 > 5:
           dra = draw()
           if dra == "Draw":
               break
           Mee = int(input("What do you want to move, 1-O1, 2-O2, 3-O3:  "))
           MoveO(Mee)
           wi = Win("O")
           if wi == "WinO":
               break
           t2 = t2 + 1
           c = c + 1




if dra == "Draw":
   print(" ********* DRAW *********** ")
elif wi == "WinX":
   print("********** X Wins the match **********")
elif wi == "WinO":
   print("********** O Wins the match **********")

