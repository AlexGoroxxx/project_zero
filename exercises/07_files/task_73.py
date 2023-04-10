file = 'CAM_table.txt'
ignore = ['DYNAMIC']
CAM = {}
with open(file) as f:
        for line in f:
            if ignore[0] in line:
                interface = line.split()[-1]
                CAM[interface] = {}
                vlan = line.split()[0]
                mac = line.split()[1]
                CAM[interface]['vlan'] = int(vlan)
                CAM[interface]['mac'] = mac
                CAM_SOR = dict(sorted(CAM.items(), key=lambda item: item[1].get('vlan')))

print(CAM_SOR)
