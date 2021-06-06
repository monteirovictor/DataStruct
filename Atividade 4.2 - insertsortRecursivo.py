def insertionSortRecursive(arr,n):
   if n>1:
      insertionSortRecursive(arr,n-1)
      x = arr[n]
      i = n-1
      while (i>0 and arr[i]>x):
         arr[i+1] = arr[i]
         i = i-1
      arr[i+1]=x

arr = [1,5,3,4,8,6,3,4,5]
n = len(arr)
insertionSortRecursive(arr, n)

print("Sorted array is:")
for i in range(n):
   print(arr[i],end=" ")
   
   
   
   