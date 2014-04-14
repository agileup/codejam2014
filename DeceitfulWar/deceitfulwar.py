# https://code.google.com/codejam/contest/2974486/dashboard#s=p3

FILENAME = "sample"

import sys
sys.stdin = open(FILENAME + ".in", 'r')
sys.stdout = open(FILENAME + ".out", 'w')

def get_line(): return raw_input()
def get_int(): return int(get_line())
def war(n, k):
  for i in range(len(n)):
    for j in range(len(k)):
      if (n[i] < k[j]):
        del k[j]
        break
  return str(len(k))
def deceit_war(n, k):
  length = len(n)
  for i in range(length):
    for j in range(len(n)):
      if (k[i] < n[j]):
        del n[j]
        break
  return str(length - len(n))

def solve():
  block = get_int()
  naomi = sorted([float(i) for i in get_line().split()])
  ken = sorted([float(k) for k in get_line().split()])
  reverse = sorted(list(ken), reverse=True)
  #return war(naomi, ken)
  #return deceit_war(naomi, reverse)
  return deceit_war(list(naomi), list(reverse))  + " " + war(list(naomi), list(ken))

for case in range(get_int()):
  print('Case #%d: %s' % (case+1, solve()))
