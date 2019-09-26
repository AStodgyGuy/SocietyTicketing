import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.encoders import encode_base64

'''
    Class that composes and sends an email
'''

class Email():

    def __init__(self, to_address, to_name, ticket):
        """ 
            Init method for sending an email
            @param: to_address: The address to send the email to
            @param: to_name: The name of the addressee
            @param: image: The file location of the ticket to attach
        """
        self.to_address = to_address
        self.ticket = ticket
        self.to_name = to_name

    def sendEmail(self):
        # The society email details
        gmail_user = "smigmail@st-andrews.ac.uk"
        gmail_password = "#####"

        # Composing the email
        msg = MIMEMultipart()
        msg["Subject"] = "Flavours of Malaysia Ticket"
        msg["From"] = gmail_user
        msg["To"] = self.to_address
        body = "Dear " + self.to_name + ",\n\nThank you for purchasing a ticket for our flagship \'Flavours of Malaysia\' event. Your ticket is attached at the end of this email. Please show this ticket at the door in order to get in. \n\nSee you at the event,\nSMIG"
        body = MIMEText(body)
        msg.attach(body)

        # Adding ticket
        with open(self.ticket, "rb") as opened:
            openedfile = opened.read()
        attachedfile = MIMEApplication(openedfile, _subtype = "pdf", _encoder = encode_base64)
        attachedfile.add_header('content-disposition', 'attachment', filename = self.to_name + "_ticket.pdf")
        msg.attach(attachedfile)

        # SMTP server details
        server = smtplib.SMTP("mailhost.st-andrews.ac.uk:587")
        server.ehlo()
        server.starttls()

        # Sending the email
        server.login(gmail_user, gmail_password)
        server.sendmail(gmail_user, self.to_address, msg.as_string())
        server.quit()
