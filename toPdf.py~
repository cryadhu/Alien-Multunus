from AlienDetails import AlienDetails
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
class Topdf:
	alienDetails = AlienDetails()
	def __call__(self,alienDetails):
		self.alienDetails = alienDetails	
		
	def writeToDisk(self):
		canvasDraw = canvas.Canvas("Alien Details.pdf",pagesize=letter)
		width, height = letter
		canvasDraw.drawString(width/2, height - 100, 'Alien Detail')
		
		canvasDraw.drawString(100, height - 150,"Code Name: "+ self.alienDetails.codename)
		canvasDraw.drawString(100, height - 200,"Blood Color : "+ self.alienDetails.bloodColor)
		canvasDraw.drawString(100, height - 250,"No. of Antenas: "+ self.alienDetails.noAntenas)
		canvasDraw.drawString(100, height - 300,"No. of Legs: "+ self.alienDetails.noLegs)
		canvasDraw.drawString(100, height - 350,"Home: "+ self.alienDetails.home)
		
		canvasDraw.showPage()
		canvasDraw.save()
		
	
	
