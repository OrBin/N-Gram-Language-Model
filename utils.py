import codecs

unicode_decoder = codecs.getdecoder("unicode_escape")


def count_occurrences(sublist, lst):
	return sum(1 for i in range(len(lst)) if lst[i:i+len(sublist)] == sublist)


def parse_model_file_line(line):
	model_file_element = line.rstrip().split("\t")
	model_file_element[0] = [char for char in unicode_decoder(model_file_element[0])[0][::2]]
	return tuple(model_file_element)
