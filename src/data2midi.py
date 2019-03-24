# data2midi.py
# this file contains the main class that handles converting tabular data into MIDI files.
# filename - name of the datafile
# fileformat - the file format
# tempo - desired tempo
# TO-DO
#   1. write a function that scales numbers to notes - DONE
#   2. write a function that calls that function on each list - DONE
#   3. convert the resulting product into an actual MIDI
#   4. test the dang thing
#   5. make into a package

from lib.MidiFile import MIDIFile
import pandas as p
from sklearn.preprocessing import minmax_scale
from numpy import ndarray 
from numpy import isnan

VALIDFORMATS = ['csv', 'CSV', 'tsv', 'TSV', 'json', 'JSON']


class data2midi:
	def __init__(self, filename, fileformat, tempo):
		# set the filename of the file, the format, and the tempo from the user.
		self.__filename = filename
		self.__tempo = tempo
		self.__fileformat = fileformat

		# Set up our raw data frame with data gathered directly from the file.
		self.__raw_df = self.convertToDataFrame(filename, fileformat)

		# Convert that data frame into an array of lists.
		self.__list_array = self.convertDFToMDList()

		# convert the list array into MIDI notes
		self.__notes = self.convertMDListToNotes()
	
	@property
	def listarr(self):
		return self.__list_array

	def createMIDI(self):
		"""create the MIDI object. WIP."""
		trackCount = len(self.__notes)

	def save(self, midi_filename):
		"""Save the midi file created by the user"""
		pass

	def convertDFToMDList(self):
		""" Converts the data frame that is generated from the data the user passes in into a multi-dimensional list."""
		outer_list = []
		# Take a column and convert it into a list.
		for column in self.__raw_df:
			inner_list = []
			for i in self.__raw_df[column]:
				inner_list.append(i)
			# Add the list to the outer multi-dimensional list.
			outer_list.append(inner_list)
		return(outer_list)

	def convertMDListToNotes(self):
		notesList = []

		for l in self.__list_array:
			notesList.append(self.scaleNumbersToNotes(l))
		return notesList

	@staticmethod
	def isValidFormat(fileformat):
		""" 
		Checks whether the file format of an input file is a valid format for conversion into a MIDI. 
		Valid formats include CSV, TSV, and JSON.
		"""
		if(fileformat in VALIDFORMATS):
			return True
		else:
			return False

	@staticmethod
	def convertToDataFrame(filename, fileformat):
		"""Converts the input file into a dataframe."""
		if (fileformat in ['csv', 'CSV']):
			return p.read_csv(filename, ',')
		elif (fileformat in ['tsv', 'TSV']):
			return p.read_csv(filename, '\t')
		else:
			return p.read_json(filename, 'records')

	@staticmethod
	def scaleNumbersToNotes(numbers):
		"""Converts numerical data into MIDI notes ranging from 0 to 127."""

		#scale the values, transform them back into a list.
		newnum = minmax_scale(numbers, (0, 127)).tolist()
		ints = []
		# if the value is a number, convert it into an integer. If it is NaN, convert it into zero.
		for n in newnum:
			if isnan(n):
				ints.append(0)
			else:
				ints.append(int(n))
		return ints

	@staticmethod
	def scaleLevelsToNotes(numbers):
		"""Converts data represented as levels into MIDI notes ranging from 0 to 127. WIP"""
		pass
