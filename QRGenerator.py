import qrcode
from PIL import Image
import os

'''
    A class to generate QR codes
'''

class QRGenerator():
    
    def __init__(self, ID, name):
        '''
            Init method for the class
            @param: ID: The ID of the person
            @param: name: The name of the person
        '''
        self.ID = ID
        self.name = name
        
    def generateQR(self):
        '''
            Method that generates the QR code
            Returns the QR code as a png file with the ID as the name i.e. {self.ID}.png
        '''
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data("ID:"+ self.ID +",NAME:" + self.name)
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="transparent")
        width, height = img.size

        pixels = img.load()
        R_OLD, G_OLD, B_OLD = (0,0,0)
        R_NEW, G_NEW, B_NEW = (246, 214, 136)

        for x in range(width):
            for y in range(height):
                r, g, b, a = pixels[x, y]
                if (r, g, b) == (R_OLD, G_OLD, B_OLD):
                    pixels[x, y] = (R_NEW, G_NEW, B_NEW, a)

        img.save(str(self.ID) + ".png")