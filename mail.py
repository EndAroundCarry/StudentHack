import os
import smtplib
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

def mail():
    numeimagine="fatavecin.jpg"
    img_data = open(numeimagine, 'rb').read()
    msg = MIMEMultipart()
    msg['Subject'] = 'subject'
    msg['From'] = 'e@mail.cc'
    msg['To'] = 'e@mail.cc'
    image = MIMEImage(img_data, name=os.path.basename(numeimagine))
    msg.attach(image)
    mail =smtplib.SMTP('smtp.gmail.com',587)
    mail.ehlo()
    mail.starttls()
    mail.login('futurebellmanchester@gmail.com','123456789manchester')
    mail.sendmail('futurebellmanchester@gmail.com','gantubogdan@gmail.com',msg.as_string())
    mail.close()
