array = [10,2,3,4,-5,6,0,12,-9]

# Whole array
print(array)

# 4th no 
print(array[3])

# 1st to 4 no
print(array[1:4])

# 2nd to 7 no
print(array[2:7])

# return all excep last 2
print(array[:-2])

# starting from index 2 to all
print (array[2 :])

#linear search
hst = array[0]

for num in array:
    if num > hst:
        hst = num

print(hst)