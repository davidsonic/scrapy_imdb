import os


c = 1
id1 = 1
id2 = 1000
id0 = str(id1) + "_" + str(id2)
with open("cut/12Wimdb.txt") as o:
    cut_l = o.readlines()
out = open('cut/imdb' + id0 + '.txt', 'w')
for line in cut_l:
	#print line
	out.write(line)
	if c%1000 == 0:
		id1 += 1000
		id2 += 1000
		id0 = str(id1) + "_" + str(id2)
		out = open('cut/imdb' + id0 + '.txt', 'w')
	# if c == 4000:
		# break
	c += 1