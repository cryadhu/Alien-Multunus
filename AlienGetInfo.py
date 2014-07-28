from AlienDetails import AlienDetails
from toTxt import Totxt
from toPdf import Topdf
from toFoobar import Tofoobar
import sys
class AlienInfo:
	def __init__(self):
		print "Welcome dear Alien Friend"
	def readAllDeatils(self,alienDetail):
		print "Enter Code Name : "
		alienDetail.setCodeName(raw_input())
		print "Enter Blood Color : "
		alienDetail.setBloodColor(raw_input())
		print "No. of Antinas : "
		alienDetail.setNoOfAntenas(raw_input())
		print "No. of Legs"
		alienDetail.setNoOfLegs(raw_input())
		print "Home"
		alienDetail.setHome(raw_input())
	def exportToFormat(self,dataObject,fileFormat):
		try :
			fileFormatObject = eval("To"+fileFormat+"()") #evaluate to get the class name from the string
		except :
			print "The requried File format cannot be processed, so the file is being processed in PDF format"
			fileFormatObject = eval("Topdf()")
		fileFormatObject(dataObject) # call __call__ function to initialize class object "alienDetails"
		fileFormatObject.writeToDisk()	# save the details in TXT/PDF/FOOBAR format
alienInfo= AlienInfo() #current class object
alienDetail = AlienDetails()	# object to store alien details
alienInfo.readAllDeatils(alienDetail) # read alien details
print "Enter export format"
fileFormat = raw_input() #get extension
alienInfo.exportToFormat(alienDetail,fileFormat) # export the details to corresponding format






