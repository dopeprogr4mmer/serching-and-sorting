def get_pivot(arr, l, r):
	return (l+r)//2

def quick_sort(arr, left, right):
	if right-left < 1:
		return
	pivot = get_pivot(arr, left, right)
	arr[right], arr[pivot] = arr[pivot], arr[right]
	l = left 
	r = right - 1
	while l <= r:
		if arr[l] < arr[right]:
			l += 1
		if arr[r] > arr[right]:
			r -= 1
		if l > r:
			break
		if arr[l] > arr[right] and arr[r] < arr[right]:
			arr[l], arr[r] = arr[r], arr[l]
	arr[l], arr[right] = arr[right], arr[l]
	quick_sort(arr, left, l-1)
	quick_sort(arr, l+1, right)
	return arr

if __name__ == '__main__':
	arr = [1, 9, 5, 4, 11, 19, 3, 15, 2, 17, 7]
	print(arr)
	sorted_array = quick_sort(arr, 0, len(arr)-1)
	print(sorted_array)