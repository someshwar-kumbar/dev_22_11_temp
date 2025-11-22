import sys

if len(sys.argv) != 2:
    print("Usage: python3 temp.py <temp>")
    sys.exit(1)
temp=int(sys.argv[1])
if (temp < 15):
  print("cold")
elif (temp<=30):
  print("normal")
else:
  print("hot")
