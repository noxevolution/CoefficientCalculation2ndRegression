#!/usr/bin/python

import csv, MySQLdb, traceback, sys, glob, os
from collections import defaultdict

dirPath = "C:\\Python27\\CoefficientCalculation2ndRegression\\"
inputCsvFileName = "generate_data_2ndregressionrun.csv"
#List of all csv files
#allCsvFilesList = glob.glob(dirPath+"*.csv")
allCsvFilesList = list(os.listdir(dirPath))

listCorsInputOutputFiles = {}

for csvfile in allCsvFilesList:
	csvfile = str(csvfile)
	if 'final_output_WOI_Forester_Total_regression' in csvfile:
	
		outputFileSbstr = csvfile.split('_')
		
		inputFile = 'ts_forester_'+outputFileSbstr[len(outputFileSbstr)-1][:-4]+'_import.csv'
		
		if os.path.isfile(inputFile):
			listCorsInputOutputFiles[csvfile] = inputFile
		
#print listCorsInputOutputFiles
headerTop = ['uniqueid', 'forecasting','tool tip','node name','Category','delta','08-2010','Monthly']

ofile = open(inputCsvFileName, 'wb')
writer = csv.writer(ofile)

writer.writerow(headerTop)     



for key,value in listCorsInputOutputFiles.iteritems():
	print 	key ," : ", value
	
	variables = list()	
	
	i_f_out = open(key)
	
	reader = csv.reader(i_f_out)
	header = reader.next()
	for index, line in enumerate(reader):
		if index == 5:
			break
		variables.append(line[0]) 
	
	for var in variables:
		i_f_input = open(value)
		reader = csv.reader(i_f_input)
		header1 = reader.next()
		for index, line in enumerate(reader):
			if var == line[0]:
				writer.writerow(line)     
		
		

ofile.close() 
	
	

