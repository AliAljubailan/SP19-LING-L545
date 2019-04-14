import sys
vo = 0
ov = 0
for c in sys.stdin.readlines():
    if c.startswith('#'):
        continue
    elif c.strip() == '':
        continue
    raw = c.split('\t')
    if 'obj' in raw:
	if raw[0] >  raw[6]:
		vo +=1
	if raw[6] > raw [0]:
		ov += 1
	if raw[0] > raw [6]:
		vo += 1

print(vo, ov)
if float(ov) <  float(vo):
	print  ("Relative object-verb order is: ","{:.2f}".format(float(ov) / float(vo)))
	print ("Relative verb-object order is: ", "{:.2f}".format(1-(float(ov) / float(vo))))
else:
	print  ("Relative verb-object order is: ","{:.2f}".format(float(vo) / float(ov)))
	print  ("Relative object-verb order is: ", "{:.2f}".format(1-(float(vo) / float(ov))))
