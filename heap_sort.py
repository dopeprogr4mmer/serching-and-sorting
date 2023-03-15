def heapify(arr, i, N):	#max_haep
	left = i*2 + 1 
	right = i*2 + 2
	largest = i
	if left < N and arr[left] > arr[largest]:
		largest = left 
	if right < N and arr[right] > arr[largest]:
		largest = right
	if largest != i:
		arr[i], arr[largest] = arr[largest], arr[i]
		heapify(arr, largest, N)

def heap_sort(arr):
	N = len(arr)
	for i in range(N//2, -1, -1):
		heapify(arr, i, N)
	for i in range(N-1, -1, -1):
		arr[i], arr[0] = arr[0], arr[i]
		heapify(arr, 0, i)
		

if __name__ == '__main__':
	arr = [1, 9, 5, 4, 11, 19, 3, 15, 2]
	print(arr)
	heap_sort(arr)
	print(arr)