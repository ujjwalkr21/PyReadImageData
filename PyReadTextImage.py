

''' Declaration of Used Package '''
import os
import string
import datetime
import pytesseract
from PIL import Image

'''Defination of Function '''
def pyReadFiles(Base_Folder):
	print ('<<<<< In pyReadFiles function >>>>>>')
	''' Source Folder Location '''
	Source_Folder=Base_Folder+'\\Input\\'
	
	try:
		for root, dirs, InputFiles in os.walk(Source_Folder):
			print('########  Execution Started #######')
			print ('Start Date Time :: '+str(datetime.datetime.now())+'\n')

			''' Reading all files in Input Folder '''
			for Inputfilename in InputFiles:
				print('Processing Input FileName :: '+Inputfilename)
				pyReadImage(Base_Folder,Inputfilename)
				
	except IOError as err:
		print('Error:', err)
		print('Code:', err.errno)

''' Function to Read text from Image'''
def pyReadImage(Base_Folder,imageFileLocation):
	
	Source_Folder=Base_Folder+'\\Input\\'
	Target_Folder=Base_Folder+'\\Output\\'
	#print(Target_Folder+imageFileLocation)
	img = Image.open(Source_Folder+imageFileLocation)
	text = pytesseract.image_to_string(img)
	#print(text)
	Target_File = Target_Folder+'OutputReadImage.txt'
	fOutput = open(Target_File, "a")
	fOutput.write(text)

''' Execution Starts from Here ''' 
if __name__== "__main__":
	try:
		print(' <<<<< In Main() >>>>>')	
		''' Set the value of base folder '''
		Base_Folder=r'E:\WorkInProgress\Codepython\PyReadTextImage'
		Target_Folder=Base_Folder+'\\Output\\'
		''' Delete file to not overwrite data '''
		os.remove(Target_Folder+'OutputReadImage.txt')
		''' Calling a Function '''
		pyReadFiles(Base_Folder)

	except Exception as expt:
		print('Execption Occured')
		print(expt)
