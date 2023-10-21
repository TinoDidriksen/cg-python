#!/usr/bin/env python3
#from functools import singledispatchmethod
import sys
import io
import re

class Window:
	def __init__(self) -> None:
		self.text_pre = ''
		self.test_post = ''
		self.flush_after = False
		self.cohorts = []

class Cohort:
	def __init__(self) -> None:
		self.text_post = ''
		self.dep_self = None
		self.dep_parent = None
		self.readings = []

class Reading:
	def __init__(self) -> None:
		self.string = ''
		self.tags = []

class Stream:
	def __init__(self, input=sys.stdin, output=sys.stdout) -> None:
		self.input = input
		self.output = output

	#@singledispatchmethod # Doesn't work with =None?
	def parse(self, stream=None):
		if not stream:
			stream = self.input
		if isinstance(stream, str):
			stream = io.StringIO(str)
		for line in stream:
			line = line.rstrip()
			print(line)
			break

	'''
	@parse.register
	def _parse(self, arg: str):
		return self.parse(io.StringIO(arg))
	'''

if __name__ == "__main__":
	stream = Stream()
	stream.parse()
