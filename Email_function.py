import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

def Email_people_func(file):
    li = ["jdhbatman@gmail.com", "josha26@icstudents.org"]

    for dest in li:
        try:
            # Create a multipart message container
            msg = MIMEMultipart()
            msg['From'] = "thunderbots22064@gmail.com"
            msg['To'] = dest
            msg['Subject'] = "Automated part list"

            body = "Test email with attachment."
            msg.attach(MIMEText(body, 'plain'))

            # Attach the file
            attachment = open(file, "rb")
            part = MIMEBase('application', 'octet-stream')
            part.set_payload((attachment).read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition', "attachment; filename= %s" % file)
            msg.attach(part)

            # Connect to SMTP server and send email
            s = smtplib.SMTP('smtp.gmail.com', 587)
            s.starttls()
            s.login("thunderbots22064@gmail.com", "qvfdijeccnvwfuby")
            text = msg.as_string()
            s.sendmail("thunderbots22064@gmail.com", dest, text)
            s.quit()

            print(f"Sent email with attachment to {dest}")
        except Exception as e:
            print(f"Sending email to {dest} failed: {e}")


