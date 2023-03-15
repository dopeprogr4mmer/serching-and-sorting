def merge(arr1, arr2):
	arr = []
	i = j = 0
	while(i<len(arr1) or j<len(arr2)):
		if i == len(arr1):
			arr.append(arr2[j])
			j += 1
		elif j == len(arr2):
			arr.append(arr1[i])
			i += 1
		elif arr1[i] < arr2[j]:
			arr.append(arr1[i])
			i += 1
		else:
			arr.append(arr2[j])
			j += 1
	return arr

def merge_sort(arr):
	if len(arr) == 1:
		return arr
	mid = len(arr)//2
	l = merge_sort(arr[:mid])
	r = merge_sort(arr[mid:])
	return merge(l, r)
	

if __name__ == '__main__':
	arr = [1, 9, 5, 4, 11, 19, 3, 15, 2]
	print(arr)
	sorted_arr = merge_sort(arr)
	print(sorted_arr)
	# z = merge([1, 4, 6, 9], [2, 6, 8, 11, 13])
	# print(z)