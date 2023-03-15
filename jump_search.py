from merge_sort import merge_sort as sort 
import math

def jump_search(arr, k):
	block_size = int(math.sqrt(len(arr)))
	start = 0 
	end = block_size - 1
	while end < len(arr):
		if k >= arr[start] and k<= arr[end]:
			break
		start += block_size
		end += block_size
	if end < len(arr):
		for i in range(start, end+1):
			if arr[i] == k:
				return i
	return False


if __name__ == '__main__':
	arr = [1, 9, 5, 4, 11, 19, 3, 15, 2, 11]
	arr = sort(arr)		#array needs to be sorted for jump search
	f = jump_search(arr, 41)
	print(f)