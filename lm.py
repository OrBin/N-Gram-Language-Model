# This file generates a character-based n-gram language model from a textual corpus


from script_parser import ScriptParser
from corpus import Corpus
from probability_helper import ProbabilityHelper
import argparse
import math

parser = ScriptParser(description='Generate a character-based language model from a textual corpus.',
					  formatter_class=lambda prog: argparse.HelpFormatter(prog, max_help_position=60))
parser.add_argument('-n', '--n-gram', type=int, help='n gram (n value)', required=True)
parser.add_argument('-i', '--input', type=str, help='input corpus file', required=True)
parser.add_argument('-o', '--output', type=str, help='output model file', required=True)

args = parser.parse_args()

print("Reading corpus")
corpus = Corpus(args.input)

# Generating all possible n-grams
print("Extracting possible n-grams")
n_grams = corpus.extract_n_grams(args.n_gram)

probability_helper = ProbabilityHelper(corpus)

# Check probability of every n-gram and write to model file
with open(args.output, 'w', encoding="utf8") as model_file:
	
	n_grams_count = len(n_grams)
	
	for index, n_gram in enumerate(n_grams):
		
		probability = probability_helper.calculate_probability(n_gram)
		if probability > 0:
			n_gram_repr = ' '.join([repr(token)[1:-1] for token in n_gram])
			model_file.write('%s\t%.5f\n' % (n_gram_repr, -math.log(probability, 2)))
			
		print("\rGenerating model... %d%% (%d/%d)" % ((index + 1) / n_grams_count * 100, index + 1, n_grams_count), end='')

