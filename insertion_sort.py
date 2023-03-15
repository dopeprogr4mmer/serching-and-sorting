def insertion_sort(arr):
	for i in range(1, len(arr)):
		k = i
		while k and arr[k] < arr[k-1]:
			arr[k], arr[k-1] = arr[k-1], arr[k]
			k -= 1


if __name__ == '__main__':
	arr = [1, 9, 5, 4, 11, 19, 3, 15]
	print(arr)
	insertion_sort(arr)
	print(arr)