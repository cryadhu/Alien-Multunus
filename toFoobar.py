from AlienDetails import AlienDetails

class Tofoobar:
	alienDetails = AlienDetails()
	def __call__(self,alienDetails):
		self.alienDetails = alienDetails	
		
	def writeToDisk(self):
		print "Do the code to export the detail to foobar extension."
		
	
	
