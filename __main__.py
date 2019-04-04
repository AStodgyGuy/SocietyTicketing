from Email import Email
from GenerateTickets import PDFGenerator
from QRGenerator import QRGenerator
from Person import Person
from datetime import datetime

import os
import csv

user_list = []

def parse_list():

    # for each person in list
    with open('users.csv', 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            # add person to user_list
            user = Person(hash(datetime.now()), row[0], row[1])
            user_list.append(user)
            with open('PurchasedTickets.csv','a') as fd:
                fd.write(user.toString()+"\n")


def main():

    # parse the list
    parse_list()

    for x in user_list:
        # Generate QR code for the user
        code = QRGenerator(x.ID, x.name)
        code.generateQR()

        # Attach the QR code to the ticket
        ticketPDF = PDFGenerator(x.ID+".png", x.ID)
        ticketPDF.generatePDF()

        # Send the ticket to the user
        emailContent = Email(x.email_address, x.name, x.ID+".pdf")
        emailContent.sendEmail()

        os.remove(x.ID+".pdf")
        os.remove(x.ID+".png")
        
    print("Complete")

main()
