
import smtplib
server=smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login('tejas.kawarkhe555@gmail.com','9309014869')
server.senfmail('2021bcs126@sggs.ac.in')
print('mail sent')
