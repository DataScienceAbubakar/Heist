import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(sender_email, sender_password, recipient_email, subject, body):
    try:
        # Set up the MIME
        message = MIMEMultipart()
        message['From'] = sender_email
        message['To'] = recipient_email
        message['Subject'] = subject

        # Attach the email body
        message.attach(MIMEText(body, 'plain'))

        # Connect to the SMTP server and send the email
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.send_message(message)
            print("Email sent successfully!")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Email details
    sender_email = "your_email@gmail.com"
    sender_password = "your_password"
    recipient_email = "company_email@example.com"
    subject = "Enquiry About Plot of Land"
    body = """Dear Sir/Madam,

I hope this email finds you well. I am writing to inquire about the availability and details of a plot of land that I am interested in purchasing. Could you please provide me with more information regarding the location, size, price, and any other relevant details?

Looking forward to your response.

Best regards,
[Your Name]
"""

    send_email(sender_email, sender_password, recipient_email, subject, body)