
# #Email send through Smtp server
import smtplib
s = smtplib.SMTP('smtp.gmail.com', "587")
s.starttls()
s.login("enter_send_mail", "gmail_app_password") #enter generated by app password not gmail password
message = "hi"
s.sendmail("enter_send_mail", "enter_receiver_mail", message)
s.quit()
