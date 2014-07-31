textfile = open('ubu-orienteering - 5.txt', 'r')
lines=textfile.readlines()
textfile.close()

textlist = []

for l in lines:
	textlist.append(l)

emaillist = open('emaillist5.txt', 'w')

for i in textlist:
	if '<input type="checkbox" name="email"' in i:
		emaillist.write(i[52:-5] + '\n')



