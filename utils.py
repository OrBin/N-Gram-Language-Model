

def read_corpus(file_path, token_separator=(lambda text: [char for char in text])):

	tokens = []
	types = set()

	with open(file_path, 'r', encoding="utf8") as corpus_file:
		for line in corpus_file:
			line_tokens = token_separator(line)
			tokens.extend(line_tokens)
			types = types.union(line_tokens)

	corpus = {
		"tokens": tokens,
		"types": types
	}

	return corpus


def generate_n_grams(types, n):

	if n <= 0:
		return []

	if n > 1:
		n_grams = []
		for curr_type in types:
			n_grams.extend([[curr_type] + n_1_gram for n_1_gram in generate_n_grams(types, n - 1)])
		
		return n_grams
	
	else:
		return [[curr_type] for curr_type in types]


def count_occurrences(sublst, lst):
	return sum(1 for i in range(len(lst)) if lst[i:i+len(sublst)] == sublst)


def calculate_probability(tokens, n_gram):

	if count_occurrences(n_gram, tokens) == 0:
		return 0

	n = len(n_gram)
	probability = 1.0
	
	try:
		for k in range(1, n+1):
			count_k_1 = count_occurrences(n_gram[:k-1], tokens)
			count_k = count_occurrences(n_gram[:k], tokens)
			probability *= count_k / count_k_1
	
	except ZeroDivisionError:
		return 0
	
	return probability
