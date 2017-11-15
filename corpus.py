import utils


class Corpus:
	
	def __init__(self, file_path, token_separator=(lambda text: [char for char in text])):
		
		with open(file_path, 'r') as corpus_file:
			self._full_text = corpus_file.read()
			
		self.types = set(token_separator(self._full_text))
	
	@property
	def types(self):
		return self._types
	
	@types.setter
	def types(self, value):
		self._types = value
	
	@property
	def full_text(self):
		return self._full_text
		
	def extract_n_grams(self, n):
		return set([self.full_text[i:i + n] for i in range(len(self.full_text))[:-n + 1]])