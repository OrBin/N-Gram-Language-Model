class ProbabilityHelper:

	def __init__(self, corpus):
		self.full_text = corpus.full_text
		self.occurences = {}
	
	def count_occurrences(self, n_gram):
		n_gram_str = n_gram if isinstance(n_gram, str) else ''.join(n_gram)
		if n_gram_str not in self.occurences:
			self.occurences[n_gram_str] = self.full_text.count(n_gram_str)
		return self.occurences[n_gram_str]
	
	def calculate_probability(self, n_gram):
		if self.count_occurrences(n_gram) == 0:
			return 0
		
		n = len(n_gram)
		probability = 1.0
		
		try:
			for k in range(1, n + 1):
				count_k_1 = self.count_occurrences(n_gram[:k - 1])
				count_k = self.count_occurrences(n_gram[:k])
				
				if count_k == 0:
					return 0
				
				probability *= count_k / count_k_1
		
		except ZeroDivisionError:
			return 0
		
		return probability
