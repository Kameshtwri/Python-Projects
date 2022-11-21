""" NO of OCCURENCES OF ALL THE CHARACTER IN A STRING """
string = input("Enter any string - ")
print("Entered string -",string)
alpha = set()
for char in string:
    alpha.add(char)
#print("Alphabets in the string are -",alpha)

occurences = {}
keys = []
values = []
count = 0
for i in alpha:
    count = string.count(i)
    keys.append(i)
    values.append(count)
    
zip_iterator = zip(keys,values)
occurences = dict(zip_iterator)

for keys,values in occurences.items():
    print(keys,":",values)
