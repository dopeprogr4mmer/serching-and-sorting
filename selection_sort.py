def selection_sort(arr):
	for i in range(len(arr)-1):
		min_ = i
		for j in range(i+1, len(arr)):
			if arr[j] < arr[min_]:
				min_ = j
		arr[i], arr[min_] = arr[min_], arr[i] 



if __name__ == '__main__':
	arr = [1, 9, 5, 4, 11, 19, 3, 15]
	print(arr)
	selection_sort(arr)
	print(arr)