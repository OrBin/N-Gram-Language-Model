import utils


class Corpus:
	
	def __init__(self, file_path, token_separator=(lambda text: [char for char in text])):
		self.tokens = []
		self.types = set()
		
		with open(file_path, 'r', encoding="utf8") as corpus_file:
			for line in corpus_file:
				line_tokens = token_separator(line)
				self.tokens.extend(line_tokens)
				self.types = self.types.union(line_tokens)
		
	@property
	def tokens(self):
		return self._tokens
	
	@tokens.setter
	def tokens(self, value):
		self._tokens = value
		
	@property
	def types(self):
		return self._types
	
	@types.setter
	def types(self, value):
		self._types = value

	def generate_n_grams(self, n):
		if n <= 0:
			return []
		
		if n > 1:
			n_grams = []
			for curr_type in self.types:
				n_grams.extend([[curr_type] + n_1_gram for n_1_gram in self.generate_n_grams(n - 1)])
			
			return n_grams
		
		else:
			return [[curr_type] for curr_type in self.types]

	def calculate_probability(self, n_gram):
		if utils.count_occurrences(n_gram, self.tokens) == 0:
			return 0
		
		n = len(n_gram)
		probability = 1.0
		
		try:
			for k in range(1, n + 1):
				count_k_1 = utils.count_occurrences(n_gram[:k - 1], self.tokens)
				count_k = utils.count_occurrences(n_gram[:k], self.tokens)
				probability *= count_k / count_k_1
		
		except ZeroDivisionError:
			return 0
		
		return probability
