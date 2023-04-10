from sys import argv
line2 = []
file = argv[1]
file_2 = argv[2]
ignore = ["duplex", "alias", "configuration"]
with open(file) as f:
        with open(file_2, 'a') as dest:
                 for line in f:
                        if '!' in line:
                                continue
                        elif ignore[0] in line:
                                continue
                        elif ignore[1] in line:
                                continue
                        elif ignore[2] in line:
                                continue
                        else:
                                line2.append(line.rstrip() + '\n')
                                dest.writelines(line2)
f.close()
