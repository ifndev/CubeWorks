from math import *
from kandinsky import *
from time import *
from random import *

#Settings
movesNumber = 25 #Number of moves per scramble
inspectionTime = 15 #Inspection time, 0 to disable

#Seed random generator based on uptime
seed(int(monotonic()*10000))

movesList = ["U","D","L","R","B","F"]

def centerSay(string):
  draw_string(string, 20, 100)
  
def centerClear():
  draw_string("                                ", 20, 100)

def startTimer():
  startPoint=monotonic()
  return startPoint

def getTime(startPoint):
  return monotonic()-startPoint
  
def newScramble(movNum):
  scramblesArr = []
  scrambleStr = []
  for i in range(movNum*2):
    scrambleStr.append("")
  
  for i in range(movNum):
    mov = randint(0,5)
    scramblesArr.append(mov)
  
  for i in range(movNum):
    if randint(1,2)==2:
      scramblesArr[i] += 6
  
  act = movNum-1
  while act>=0:
    if scramblesArr[act] == scramblesArr[act-1] and act > 1 and scramblesArr[act] < 6:
      scrambleStr[act-1] = str(2) + (movesList[scramblesArr[act]])
      act -= 1
    elif scramblesArr[act] == scramblesArr[act-1] and act > 1 and scramblesArr[act] >= 6:
      scrambleStr[act-1] = str(2) + (movesList[scramblesArr[act]-6])
      act -= 1
    elif (scramblesArr[act] == scramblesArr[act-1]-6) or ((scramblesArr[act] == scramblesArr[act-1]+6)) and (act > 1):
      new = 0
      while (new == scramblesArr[act] or new == scramblesArr[act-1]):
        new = randint(1, 6)
      scrambleStr[act] = (movesList[new])


    else:
      if scramblesArr[act]>5:
        scrambleStr[act] = movesList[scramblesArr[act]-6] + "'"
      else:
        scrambleStr[act] = movesList[scramblesArr[act]]
    act -= 1
  scrambleFinal = list(filter(None, scrambleStr))
  
  return scrambleFinal
  
def printScramble(scramble):
  pos = 0
  hau = -1
  for i in scramble:
    if pos%9 == 0:
      hau += 1
      pos == 1
    draw_string(i, (1+(pos%9))*30, 10+hau*25)
    pos +=1

printScramble(newScramble(movesNumber))
centerSay("Press back to start")
input()
if inspectionTime > 0:
  centerSay("   s remaining (inspection)")
  sp = startTimer()
  while getTime(sp) < 15:
    if getTime(sp) > 5 and getTime(sp) < 7:
      centerSay("   ")
    centerSay(str(inspectionTime-int(getTime(sp))))
centerClear()
sp = startTimer()
centerSay("SOLVE... (press back)")
input()
time = getTime(sp)
centerClear()
centerSay("             " + str(int(time)))