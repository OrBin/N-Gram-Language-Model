def count_occurrences(sublist, lst):
	return sum(1 for i in range(len(lst)) if lst[i:i+len(sublist)] == sublist)