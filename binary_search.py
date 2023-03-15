from merge_sort import merge_sort as sort 

def binary_search(arr, k, l, r):
	if l > r:
		return False
	mid = (l+r)//2
	if arr[mid] == k:
		return mid
	if k > arr[mid]:
		return binary_search(arr, k, mid+1, r)
	else:
		return binary_search(arr, k, l, mid-1)


if __name__ == '__main__':
	arr = [1, 9, 5, 4, 11, 19, 3, 15, 2]
	arr = sort(arr)		#array needs to be sorted for binary search
	f = binary_search(arr, 1, 0, len(arr)-1)
	print(f)