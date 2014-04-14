# https://code.google.com/codejam/contest/2974486/dashboard#s=p0

FILENAME = "A-small-attempt0"

import sys
sys.stdin = open(FILENAME + ".in", 'r')
sys.stdout = open(FILENAME + ".out", 'w')

def get_int(): return int(get_line())
def get_line(): return raw_input()
def trick(first, second):
  number = list(set(first) & set(second))
  if ( len(number) == 0 ): return "Volunteer cheated!"
  elif ( len(number) == 1 ): return int(number[0])
  else: return "Bad magician!"

def solve():
  f_line = get_int()
  for i in range(4):
    if (i == f_line-1):
      f_list = [float(i) for i in get_line().split()]
    else:
      get_line()

  s_line = get_int()
  for i in range(4):
    if (i == s_line-1):
      s_list = [float(i) for i in get_line().split()]
    else:
      get_line()

  return trick(list(f_list), list(s_list))

for case in range(get_int()):
  print('Case #%d: %s' % (case+1, solve()))
