NAME = {}
print(NAME)
NAME = {'FIRST_NAME': 'YASH', 'LAST_NAME': 'KUMAR', 'ROLL': 2, 'PLACE': 'GHAZIABAD'}
print(NAME)

#deleting 2 nd key

del NAME['LAST_NAME']
print(NAME)

#ADDING key back to the dictionary

NAME['LAST_NAME'] = "KUMAR"
print(NAME)

NAME['AGE'] = 26
print(NAME)

#apply if condition on key

if "FIRST_NAME" in NAME.keys():
    print("name exist")
else:
    print("none")

#apply if condition on key AND VALUE
Count = 0
for key, value in NAME.items():
    numbers = {}
    if "ROLL" in key:
        print("key inside ROLL : : ", key)
        #if isinstance(value, int):
            #print("Inside roll value is :: ", value)
            #print("inside roll key is ::", key)
        print("****" * 30)
        #print(isinstance(NAME['ROLL'], int))
        #print(NAME['ROLL'] == isinstance(NAME['ROLL'], int))
        #print("instance ~IJFNHFNSNF", isinstance(value ,int))
    #print("instance ~~",isinstance(value, int))
    if isinstance(value, int):
        Count+=1
        value **= 2
        #NAME[value] = value ** 2
        print("value squared is ::", value)
        print("key is :: ", key)
print("Count # of keys having integer values", Count)










