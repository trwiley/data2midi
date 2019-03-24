# data2midi.py
# this file contains the main class that handles converting tabular data into MIDI files.
# filename - name of the datafile
# fileformat - the file format
# tempo - desired tempo
# TO-DO
#   1. write a function that scales numbers to notes
#   2. write a function that calls that function on each list
#   3. convert the resulting product into an actual MIDI
#   4. test the dang thing
#   5. make into a package

import lib.MidiFile as m
import pandas as p
from sklearn.preprocessing import MinMaxScaler

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
	
	@property
	def listarr(self):
		return self.__list_array

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
		"""Converts numerical data into MIDI notes ranging from 0 to 127. WIP."""
		scaler = MinMaxScaler(feature_range=(0, 127))
		print(scaler.transform(numbers))
		return scaler.transform(numbers)

	@staticmethod
	def scaleLevelsToNotes(numbers):
		"""Converts data represented as levels into MIDI notes ranging from 0 to 127. WIP"""
		pass
