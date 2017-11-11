from lm_parser import LmParser
import argparse
from utils import *
import math

parser = LmParser(description='Generate a character-based language model from a textual corpus.',
				  formatter_class=lambda prog: argparse.HelpFormatter(prog, max_help_position=60))
parser.add_argument('-n', '--n-gram', type=int, help='n gram (n value)', required=True)
parser.add_argument('-i', '--input', type=str, help='input corpus file', required=True)
parser.add_argument('-o', '--output', type=str, help='output model file', required=True)

args = parser.parse_args()

corpus = read_corpus(args.input)

# Generating all possible n-grams
n_grams = generate_n_grams(corpus["types"], args.n_gram)

# Check probability of every n-gram and write to model file
with open(args.output, 'w', encoding="utf8") as model_file:
	
	for n_gram in n_grams:
		probability = calculate_probability(corpus["tokens"], n_gram)
		if probability > 0:
			n_gram_repr = ' '.join([repr(token) for token in n_gram])
			model_file.write('%s\t%.5f\n' % (' '.join(n_gram), -math.log(probability, 2)))
			print('%s\t%.5f' % (n_gram_repr, -math.log(probability, 2)))