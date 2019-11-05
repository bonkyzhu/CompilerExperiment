'''
G[E]：
  E→eBaA
  A→a|bAcB
  B→dEd|aC
  C→e|dC
测试样例为：
  eadeaa#
  edeaebd#
  edeaeaadabacae#
'''
from prettytable import PrettyTable

test_set = [
  "eadeaa",
  "edeaebd",
  "edeaeaadabacae",
]

print_status = {"OK":"是", "ERROR":"不是"}

index = 0

def E(test):
  '''
  E->eBaA
  '''
  global index
  if test[index] == 'e':
    index += 1
    if B(test) == "ERROR":
      return "ERROR"
    else:
      if test[index] == 'a':
        index += 1
        if A(test) == "ERROR":
          return "ERROR"
        else:
          return "OK"
      else:
        return "ERROR"
  else:
    return "ERROR"

def A(test):
  '''
  A→a,A→bAcB
  '''
  global index
  if test[index] == 'a':
    index += 1
    return "OK"
  else:
    if test[index] == 'b':
      index += 1
      if A(test) == "ERROR":
        return "ERROR"
      else:
        if test[index] == 'c':
          index += 1
          if B(test) == "ERROR":
            return "ERROR"
          else:
            return "OK"
        else:
          return "ERROR"
    else:
      return "ERROR"

def B(test):
  '''
  B→dEd,B→aC
  '''
  global index
  if test[index] == 'd':
    index += 1
    if E(test) == "ERROR":
      return "ERROR"
    else:
      if test[index] == 'd':
        index += 1
        return "OK"
      else:
        return "ERROR"
  else:
    if test[index] == 'a':
      index += 1
      if C(test) == "ERROR":
        return "ERROR"
      else:
        return "OK"
    else:
      return "ERROR"

def C(test):
  '''
  C→e,C→dC
  '''
  global index
  if test[index] == 'e':
    index += 1
    return "OK"
  else:
    if test[index] == 'd':
      index += 1
      if C(test) == "ERROR":
        return "ERROR"
      else:
        return "OK"
    else:
      return "ERROR"

def run(test):
  global index
  index = 0
  table = PrettyTable(["源串", "是否为该文法的句子", "签名"])
  statu = print_status[E(test)]
  table.add_row([test, statu, "朱子权 20178859"])
  print(table)

if __name__ == "__main__":
  for test in test_set:
    run(test)