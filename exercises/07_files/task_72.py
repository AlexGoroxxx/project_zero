from sys import argv
file = argv[1]
with open(file) as f:
     for line in f:
          if '!' in line:
            continue

          else:
               print(line.rstrip())
