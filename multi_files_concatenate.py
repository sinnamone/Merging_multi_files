import optparse
from Bio import SeqIO
import os
import pandas as pd
import sys

parser = optparse.OptionParser(usage='python %prog -f [ "input file 1" ] -f [ "input file 2"] -o [  "Output Id" ] -o [ "Output Pathway" ] ',version='1.0',)
parser.add_option('-f', action="append", dest='input', default=[])
parser.add_option('-o', action="store", dest="output",help='Output Id')
parser.add_option('-p', action="store", dest="pathout",help='Output Pathway')
options, args = parser.parse_args()



class concatenatefasta(object):
	def __init__(self,input,output,pathout):
		self.input = input
		self.output = output
		self.pathout = pathout
		if pathout.endswith('/') == True:
			self.path_out = pathout
		else:
			self.path_out = pathout+'/'
			
	def confasta(self):
		with open(self.pathout+self.output+'.fasta', 'w') as outfile:
			for fname in self.input:
				with open(fname) as infile:
					for line in infile:
						outfile.write(line)
						
						

if __name__ == '__main__':
	print('Concatenate FastA file : %s' % (options.input))
	a  = concatenatefasta(options.input,options.output,options.pathout).confasta()
