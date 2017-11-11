# This file samples a given model and generates text as requested


from script_parser import ScriptParser
import argparse

parser = ScriptParser(description='Sample a given model and generate text as requested.',
					  formatter_class=lambda prog: argparse.HelpFormatter(prog, max_help_position=60))
parser.add_argument('-n', '--n-gram', type=int, help='n gram (n value)', required=True)
parser.add_argument('-m', '--model-file', type=str, help='model file', required=True)
parser.add_argument('-s', '--start-text', type=str, help='start text', required=True)
parser.add_argument('-d', '--length', type=int, help='length', required=True)

args = parser.parse_args()

