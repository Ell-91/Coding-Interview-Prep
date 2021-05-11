def binarySearch(array,key):
  first_element = 0 
  last_element = len(array)-1

  while first_element <= last_element: #base case
    mid_element = (first_element + last_element)//2

    #if element at index [i]
    if array[mid_element] == key:
      return mid_element
    
    else:
      #left side of array
      if key < array[mid_element]:
        last_element = mid_element - 1
      #right side of array
      else:
        first_element = mid_element + 1


	
array  = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
key = 8

print(binarySearch(array, key))


