import utils


class Model:
	
	def __init__(self, file_path):
		with open(file_path, 'r', encoding="utf8") as model_file:
			self.model_tree = {}
			for line in model_file:
				chars, minus_log_p = utils.parse_model_file_line(line)
				n_1_gram = ''.join(chars[:-1])
				last_char = chars[-1]
				if n_1_gram not in self.model_tree:
					self.model_tree[n_1_gram] = {}
				self.model_tree[n_1_gram][last_char] = minus_log_p
				
		for n_1_gram in self.model_tree:
			
			min_n_char, min_value = next(iter(self.model_tree[n_1_gram].items()))
			
			for n_char, value in self.model_tree[n_1_gram].items():
				if value < min_value:
					min_n_char, min_value = n_char, value
			
			self.model_tree[n_1_gram] = min_n_char

	def __getitem__(self, n_1_gram):
		return self.model_tree[n_1_gram]