array_x = [88, 12, 78, 87, 89, 95, 16, 82]

def insertionSort(array, i = 1):
  if i >= len(array):
    return array
  if array[i-1] > array[i]:
    temp = array[i]
    for a in range(0, i):
      if temp < array[a]:
        array.insert(a,temp)
        del array[i+1]
        break
  return insertionSort(array, i+1)

if __name__ == '__main__':
  result = insertionSort(array_x)
  print array_x
