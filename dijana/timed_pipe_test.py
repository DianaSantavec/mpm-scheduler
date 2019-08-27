#!/usr/bin/python

import sys, time

with open(sys.argv[1]) as fin:
    cmds = fin.readlines()

for cmds_word in cmds:
    word = cmds_word.split(" ")

print (word)

first = True
second = True
third = False
number_of_words = -1
for cmd in word:
    cmd = cmd.strip()
#    if not cmd:
#        continue
#    cmd = cmd + '\r'
    if third:
        number_of_words = int(cmd)
        third = False
        continue
    if first or second:
        cmd = cmd + '\r'
        if first:
            first = False
        else:
            second = False
            third = True
    if not first or not second or not third:
        number_of_words = number_of_words - 1
    if number_of_words == 0:
        cmd = cmd + '\r'
#    else:
#        first = False
    #print(cmd)
    time.sleep(float(sys.argv[2]))
    sys.stdout.write(cmd)
    sys.stdout.flush()
