import smtplib
from email.message import EmailMessage


def send_email(sender_email, app_password, receiver_email, subject, message):

    email = EmailMessage()

    email["From"] = sender_email
    email["To"] = receiver_email
    email["Subject"] = subject

    email.set_content(message)


    # Connect to Gmail
    server = smtplib.SMTP("smtp.gmail.com", 587)

    server.starttls()

    # Login
    server.login(
        sender_email,
        app_password
    )

    # Send email
    server.send_message(email)

    # Close connection
    server.quit()