import codecs

unicode_decoder = codecs.getdecoder("unicode_escape")


def parse_model_file_line(line):
	model_file_element = line.rstrip().split("\t")
	model_file_element[0] = [char for char in unicode_decoder(model_file_element[0])[0][::2]]
	return tuple(model_file_element)
