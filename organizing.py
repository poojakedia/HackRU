'''
  open file for reading
  make new outer list that will store lists of strings
  
  while (file has next line)
    
    if (read line of file = "#####")
      make new inner list that will store strings 
      outer add inner
    else
      inner add line

  close file
'''
import random
from random import randrange


# stores answers into lists
def organize():
  file = open('key.txt', 'r')
  outer = []

  while file.next():
    line = file.readline()
    if line == "#####":
      inner = []
      outer.append(inner)
    else:
      inner.append(line)

  file.close()


# checks user's input against key
def check(user, key):
  user_list = [user.split(",")]
  if user == key:
    return True
  return False


# shuffles the list and stores it into a singular string to print more nicely
def randomize(key):
  copy_key =  [x for x in key]
  index = 0
  nkey = []
  while len(copy_key) != 00:
    index = random.randint(0, len(copy_key) - 1)
    nkey.append(copy_key[index])
    copy_key.remove(copy_key[index])
  str_output = "Word Bank: "
  for i in nkey:
    str_output = str_output + i + "  ,  "
  return str_output
