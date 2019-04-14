import sys
import matplotlib.pyplot as plt

""" THIS  IS the CODE that I wrote to get the results and based on which I adapted the below code :: 
vo = 0 # to start counting to verb object order by 0  
ov = 0 # # to start counting to verb object order by 0  

for c in sys.stdin.readlines(): # looping into the language conllu file
    if c.startswith('#'):
        continue          # skipping comment lines in the file
    elif c.strip() == '':
        continue          # skipping empty lines in the file
    raw = c.split('\t')    # splitting data in the file into lists 
    if 'obj' in raw:       # searching for object to count
        if raw[0] >  raw[6]:  # if the object index is greater than the head index then 
                vo +=1        # this means it follows its verb, so add 1 each time  
        if raw[6] > raw [0]:  # if the head index is greater, then:
                        
                ov += 1      # the head follows its object, so the program adds 1 each time it finds such a relation 
        if raw[0] > raw [6]:
                vo += 1

#print(vo, ov)    # debugging
if float(ov) <  float(vo):  #checking which word order is more freauent  
        print  ("Relative object-verb order is: ","{:.2f}".format(float(ov) / float(vo))) #output the division ov by vo if its smaller
        print ("Relative verb-object order is: ", "{:.2f}".format(1-(float(ov) / float(vo))))
else:
        print  ("Relative verb-object order is: ","{:.2f}".format(float(vo) / float(ov))) #output the division vo by ov if its smaller
        print  ("Relative object-verb order is: ", "{:.2f}".format(1-(float(vo) / float(ov))))
 ###### I chose to have a result of 2 decimal numbers do to that a number of the languages that ==
 ##       I inspected, like Arb and Hebr had a very low rate of relationship between obj and v ########

"""
### NOTE: 1 For more convience I uploaded the above code in a separated file with no comments.!!!

labels = {0:'fin', 1:'arb', 2:'hbr',3:'latn',4:'basq', 5: 'urd', 6: 'uyg', 7: 'latv', 8: 'jap', 9: 'copt', 10: 'dan'}
x = [0.2, 0.04, 0.08, 0.53, 0.54, 0.53, 0.54, 0.74, 0.77, 0.19, 0.08 ]  # proportion of OV
y = [0.8, 0.96, 0.92, 0.47, 0.46, 0.47, 0.46, 0.24, 0.23, 0.81, 0.92 ]  # proportion of VO
plt.plot(x, y, 'ro')
plt.title('Relative word order of verb and object')
plt.xlim([0,1]) # Set the x and y axis ranges
plt.ylim([0,1])
plt.xlabel('OV') # Set the x and y axis labels
plt.ylabel('VO')
for i in labels:  # Add labels to each of the points
    plt.text(x[i]-0.03, y[i]-0.03, labels[i], fontsize=9)
#plt.savefig(sys.argv[])
plt.show()

##NOTE2: Becuase some languages tested have very close rates, they may not be shown in the plot
### as well as I wanted. I tried to modify distances and lables but it was quiet complex.
