import copy
def bubbleSort(arr):
    n = len(arr)
 
    for i in range(n-1):
 
        for j in range(0, n-i-1):

            if arr[j] > arr[j + 1] :
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
 

def insertionSort(arr):
  
    for i in range(1, len(arr)):
  
        key = arr[i]
  
        j = i-1
        while j >=0 and key < arr[j] :
                arr[j+1] = arr[j]
                j -= 1
        arr[j+1] = key

def selectionSort(A):

  for i in range(len(A)):
      
    min_idx = i
    for j in range(i+1, len(A)):
        if A[min_idx] > A[j]:
            min_idx = j
    A[i], A[min_idx] = A[min_idx], A[i]
  
arrInsertion = [12, 11, 13, 5, 6]
arrBubble = copy.deepcopy(arrInsertion)
arrselection = copy.deepcopy(arrInsertion)

bubbleSort(arrBubble)
print ("Bubble sorted array is:")
for i in range(len(arrBubble)):
    print (arrBubble[i]),

insertionSort(arrInsertion)
print ("Insertion sorted array is:")
for i in range(len(arrInsertion)):
    print (arrInsertion[i])

selectionSort(arrBubble)
print ("Selection sorted array is:")
for i in range(len(arrBubble)):
    print (arrBubble[i]),