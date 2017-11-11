from argparse import ArgumentParser
import sys


class ScriptParser(ArgumentParser):
	def error(self, message):
		sys.stderr.write('error: %s\n' % message)
		self.print_help()
		sys.exit(2)

