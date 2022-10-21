arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
query = 5

def binarySearch(arr, query):
  lo, hi = 0, len(arr)-1

  while lo<=hi:
    mid = (lo+hi) // 2
    mid_number = arr[mid]
    
    if (mid_number == query):
      return mid
    elif (mid_number > query):
      hi = mid-1
    elif (mid_number < query):
      lo = mid+1
    else:
      return -1
  
      
print(binarySearch(arr, query))
