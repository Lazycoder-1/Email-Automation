
# Email Automation using Python

# import smtplib
# user_email = input('Enter your email: ')
# message = input('Enter your message here: ')

# def email_automation(user_email,message):
#     server = smtplib.SMTP('smtp.gmail.com',587)
#     server.starttls()
#     server.login('amoakoheneafirim@gmail.com','Bohr2015')
#     server.sendmail('amoakoheneafirim@gmail.com',user_email, message) 
#     server.close()

# email_automation(user_email,message)










import smtplib
# from email.mime.text import MIMEText
user_email = input('Enter your email: ')
message = input('Enter your message here: ')
def email_automation():
    try:
        # Establish a connection to the Gmail SMTP server
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        
        # Login to the email account
        server.login('amoakoheneafirim@gmail.com', 'Bohr2015')  # Replace with your App Password if using two-factor authentication
        
        # Create the email content
        from_addr = 'amoakoheneafirim@gmail.com'
        # to_addr = 'sma84762@doolk.com'
        # subject = 'A simple testing email'
        # body = 'This is a test email from a Python script.'
        
        # Construct the email message
        msg = MIMEText(body)
        msg['Subject'] = subject
        msg['From'] = from_addr
        msg['To'] = to_addr
        
        # Send the email
        server.sendmail(from_addr, to_addr, msg.as_string())
        
        # Close the connection to the server
        server.quit()
        
        print("Email sent successfully!")
    except smtplib.SMTPAuthenticationError:
        print("Failed to authenticate with the SMTP server. Check your email address and password.")
    except smtplib.SMTPConnectError:
        print("Failed to connect to the SMTP server. Check your internet connection.")
    except smtplib.SMTPRecipientsRefused:
        print("The recipient's email address was refused by the server. Check the recipient's email address.")
    except smtplib.SMTPSenderRefused:
        print("The sender's email address was refused by the server. Check the sender's email address.")
    except smtplib.SMTPDataError:
        print("The SMTP server refused to accept the message data.")
    except Exception as e:
        print(f"Failed to send email: {e}")

email_automation()

