# for sending mail through smtp you need to enable less sequre app in your email account.
from email.message import EmailMessage #this is use for send in the email format.
import smtplib # this is use for connect to gmail.
import imghdr # this is use for attach images to mail.

contacts = ['example1@gmail.com', 'example2@gmail.com'] # write the email ids to which you want to send mail. you can send mail to multiple people at a time.
msg = EmailMessage()
msg['From'] = 'yourmail@gmail.com'  #write your email id
msg['To'] = contacts
msg['Subject'] = 'write your email subject'
msg.set_content('write your email body')

# you can attach your file here. for files other than image you don't have to add imghdr. Change the maintype and subtype accordding to the file you are attaching.
with open('filename.png', 'rb') as f: # write your filename here.
    file_data = f.read()
    file_type = imghdr.what(f.name) # no need for this line for attaching files other than image.
    file_name = f.name
    msg.add_attachment(file_data, maintype='image', subtype=file_type, filename=file_name) # change according to your file type.

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp: # I am using smtp_ssl instead of smtp so that i need not have to use ehlo or starttls.
   smtp.login('yourmail@gmail.com', 'password') # write your email and password.
   smtp.send_message(msg)