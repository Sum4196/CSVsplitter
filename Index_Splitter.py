import csv
import pprint
lyst = []
new_lyst = []
csv_lyst = open(r"MasterDrawviewIndex_Edited.csv","r+")
lyst = csv.reader(csv_lyst)



for row in lyst:
	new_lyst.append(row)

def chunks(l, n):
	l = new_lyst
	#iterations = 0
	for i in xrange(0, len(l), n):
		yield l[i:i+n]
		#iterations = iterations + 1
	#print(iterations)

# def lyst1txt():
	# with open('lyst1.txt','w') as f1:
		# for row in new_lyst:
			# lyst1 = pprint.pprint(list(chunks(range(0, 9999), 1)))
			# output = pprint.pprint(lyst1)
			# print("END OF LIST 1")
			# f1.write(str(output))

# lyst1txt()
		
# lyst2 = pprint.pprint(list(chunks(range(10000, 19999), 1)))
# pprint.pprint(lyst2)
# print("END OF LIST 2")

# lyst3 = pprint.pprint(list(chunks(range(20000, 29999), 1)))
# pprint.pprint(lyst3)
# print("END OF LIST 3")

# lyst4 = pprint.pprint(list(chunks(range(30000, 39999), 1)))
# pprint.pprint(lyst4)
# print("END OF LIST 4")

# lyst5 = pprint.pprint(list(chunks(range(40000, 50000), 1)))
# pprint.pprint(lyst5)
# print("END OF LIST 5")



lyst1=[new_lyst[x:x+100] for x in xrange(0, len(new_lyst), 9500)]
print(lyst1)
print("END OF LYST1")

# lyst2=[new_lyst[x:x+100] for x in xrange(10001, len(new_lyst), 20000)]
# print(lyst2)
# print("END OF LYST2")

# lyst3=[new_lyst[x:x+100] for x in xrange(20001, len(new_lyst), 30000)]
# print(lyst3)
# print("END OF LYST3")

# lyst4=[new_lyst[x:x+100] for x in xrange(30001, len(new_lyst), 40000)]
# print(lyst4)
# print("END OF LYST4")

# lyst5=[new_lyst[x:x+100] for x in xrange(40001, len(new_lyst), 50000)]
# print(lyst5)
# print("END OF LYST5")		

#csv_lyst.close()