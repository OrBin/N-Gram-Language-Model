# This file samples a given model and generates text as requested


from model import Model
from script_parser import ScriptParser
import argparse

parser = ScriptParser(description='Sample a given model and generate text as requested.',
					  formatter_class=lambda prog: argparse.HelpFormatter(prog, max_help_position=60))
parser.add_argument('-n', '--n-gram', type=int, help='n gram (n value)', required=True)
parser.add_argument('-m', '--model-file', type=str, help='model file', required=True)
parser.add_argument('-s', '--start-text', type=str, help='start text', required=True)
parser.add_argument('-d', '--length', type=int, help='length', required=True)

args = parser.parse_args()

# If the start-text's length is not equal to n-1 => error.
if len(args.start_text) < (args.n_gram - 1):
	raise ValueError("The length of the given start text is lower than n-1")

model = Model(args.model_file)
text = args.start_text

for i in range(args.n_gram, args.length):
	text_last_n_1 = text[-(args.n_gram - 1):]
	text += model[text_last_n_1]
	
print(text)
