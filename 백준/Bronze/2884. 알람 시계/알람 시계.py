H, M = map(int, input().split())

if(M < 45) :    # same M-45 < 0, i did this because if m is smaller than 45, it will make our alarm clock time go into the negatives.
  if(H <= 0) :  # you can put the first "if"s print part into an else so that you can print it too.o ;-;
    print(H+23, M-45+60)
  else :
    print(H - 1, M - 45 + 60)
else :
  print(H, M - 45)
