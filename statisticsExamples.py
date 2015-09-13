def max(array):
    if(len(array)==1):
        return array
    else:
        max=array[0]
        #print(max)
        for index,item in enumerate(array):
            #print(item)
            if(item>max):
                max=item
        return max
def min(array):
    if(len(array)==1):
        return array
    else:
        min=array[0]
        for index,item in enumerate(array):
            #print(item)
            if(item<min):
                min=item
        return min
def avg(array):
    sum=0
    for n in array:
        sum += n
    return sum/len(array)

testArray = [3,6,2,23,3,89,5,489,2,4,5,-1,-40,34]
maximum = max(testArray)
minimum = min(testArray)
average = avg(testArray)
print('Max:'+str(maximum)+' Min:'+str(minimum)+'\n')
print('Average array elements: '+str(average))