
def find_duplicates(numbers_list) :
    i=0
    j=0
    dulicates =[]
    for i in range (len(numbers_list)):
        for j in range (len(numbers_list)):
            if (i!=j and numbers_list[i]==numbers_list[j] and numbers_list[i] not in dulicates) :
                dulicates.append(numbers_list[i])
                break
        
    print (dulicates)
    
numbers_list = [1, -1, 0,2, 2,4,3,3, 4, 5,0,-1,2,0,5]
find_duplicates(numbers_list)
