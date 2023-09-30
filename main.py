import ssl, smtplib


def init_smtp_context():
    smtp = smtplib.SMTP("mail.python.org", port=587)
    context = ssl.create_default_context()
    smtp.starttls(context=context)

def main():
    

if __name__ == '__main__':
  main()