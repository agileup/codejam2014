# https://code.google.com/codejam/contest/2974486/dashboard#s=p1

FILENAME = "B-large"

import sys
sys.stdin = open(FILENAME + ".in", 'r')
sys.stdout = open(FILENAME + ".out", 'w')

def get_int(): return int(get_line())
def get_line(): return raw_input()

def solve():
  C, F, X = map(float, [float(i) for i in get_line().split()])

  farmNum = 0
  currentRate = 2.0
  farmSeconds = [0, ]

  currentTime = X / currentRate
  nextTime = (C / currentRate) + X / (currentRate + F)

  farmSeconds.append( farmSeconds[farmNum] + C / currentRate )

  while True:
    if (currentTime <= nextTime): break
    currentTime = nextTime
    farmNum += 1
    currentRate += F
    farmSeconds.append( farmSeconds[farmNum] + C / currentRate )
    nextTime = farmSeconds[farmNum+1] + X / (currentRate + F)

  return currentTime

for case in range(get_int()):
  print('Case #%d: %.7f' % (case+1, solve()))
