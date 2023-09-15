import io
import sys
from importlib import import_module


def test_program():	
	test_inputs = ["3", "5"]
	out_data = []
	
	def write(data):
		out_data.append(data)
	
	def flush():
		pass
	
	def readline(*args):
		out = test_inputs.pop()
		return out
		
	old_inn = sys.stdin
	old_out = sys.stdout
	sys.stdout = io.StringIO()
	sys.stdout.write = write
	sys.stdout.flush = flush
	
	sys.stdin = io.StringIO()
	sys.stdin.readline = readline
	import_module("newfile")
	
	sys.stdin = old_inn
	sys.stdout = old_out
	# print(type(out_data[0].strip()))
	assert (out_data[0].strip()) == "7"

if __name__ == "__main__":
    test_program()