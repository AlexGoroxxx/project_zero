with open('ospf.txt') as f:
	 for line in f:
                prefix = line.split()[1]
                ad_metric = line.strip('[]').split()[2]
                next_hop = line.split()[4].strip(',')
                last_update = line.split()[5].strip(',')
                interface = line.rstrip().split()[6]
                print('\n', '{:<20}{:<30}'.format('Prefix', prefix), '\n',
                '{:<20}{:<30}'.format('AD', ad_metric), '\n', '{:<20}{:<30}'.format('Next-Hop',next_hop.lstrip()), '\n',
                '{:<20}{:<30}'.format('Last update',last_update ), '\n', '{:<20}{:<30}'.format('Out Interface', interface))
