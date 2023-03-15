def bubble_sort(arr):
	n = len(arr)
	k = n
	for i in range(n):
		for j in range(1, k):
			if arr[j] < arr[j-1]:
				arr[j], arr[j-1] = arr[j-1], arr[j]
		k -= 1
		

if __name__ == '__main__':
	arr = [1, 9, 5, 4, 11, 19, 3, 15]
	print(arr)
	bubble_sort(arr)
	print(arr)