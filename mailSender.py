
# libraries to be imported
from io import StringIO
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import environmentControl
import camera

fromaddr = 'KomatoBot@gmail.com'
toaddr = 'eMichalGut@gmail.com'

tempSensor = environmentControl.GetTemp()
lightSensor = environmentControl.GetLight()
#camera.getPicture()

# instance of MIMEMultipart
msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = 'Komato Fotka'
body = 'Komato kontrolní fotografie.'+'\n'+'temp: ' + tempSensor[0] + '\n'+'humidity: ' + tempSensor[1] + '\n' + 'ligthSensor: ' + str(lightSensor)
  
# attach the body with the msg instance
#msg.attach(MIMEText(body, 'image.jpg'))
msg.attach(MIMEText(body, 'x.txt')) 

# open the file to be sent 
filename = 'x.txt'
#attachment = open('/home/pi/Desktop/image.jpg', 'rb')
attachment = open('C:\\temp\\x.txt', 'rb')
p = MIMEBase('application', 'octet-stream')
p.set_payload((attachment).read())
encoders.encode_base64(p)
p.add_header('Content-Disposition', "attachment; filename= %s" % filename)
msg.attach(p)
  
# creates SMTP session
s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
s.login(fromaddr, "komato420")
  
text = msg.as_string()
s.sendmail(fromaddr, toaddr, text)

s.quit()