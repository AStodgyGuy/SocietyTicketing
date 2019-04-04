from fpdf import FPDF

'''
    Class that generates the ticket pdf
'''

class PDFGenerator():

    def __init__(self, qr_code, ID):
        '''
            Init method for this class
            @param: qr_code: The file path to the qr code to add to the ticket
            @param: ID: The ID of the user that this qr code will be sent too
        '''
        self.qr_code = qr_code
        self.ID = ID

    def generatePDF(self):
        '''
            Method that generates the ticket. The ticket will be output as {self.ID}.pdf
        '''

        # Create pdf with ticket dimensions
        w = 1050
        h = 387
        pdf = FPDF('P','mm',[w,h])
        pdf.add_page()

        # Add ticket and qr code to the pdf
        pdf.image("ticket.png",x=0,y=0,w=w,h=h,type="png")
        pdf.image(self.qr_code,x=838, y=124, w=139,h=142,type="png")

        # Output the file
        pdf.output(self.ID + ".pdf", "F")