year = int(input())
if year%4==0 :      # write equals remainder
  if year%400==0:   # can use if another time if you put it inside the barrier of the first "if"
    print(1)
  elif year%100!=0:
    print(1)
  else:                   # write another else so that the code knows that if the two are false but only one is true, to print 0 instead of one.
    print(0)
else:                     # don't use tab if you don't want to use the else on the codes on the inside.
  print(0)