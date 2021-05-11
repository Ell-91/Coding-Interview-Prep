

def linearSearch(array, key):
  for i in range(len(array)):
    if array[i] == key:
      return i
  return -1

array = [3, 5, 6, 7, 8]
key = 7

print(linearSearch(array, key))

