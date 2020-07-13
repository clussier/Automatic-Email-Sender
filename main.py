import os
import smtplib
import getEmails

EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')


with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
    smtp.ehlo()

    # Encrypt traffic
    smtp.starttls()
    smtp.ehlo()

    # Log into email
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

    # Get emails from excel sheet
    emails = getEmails.get_emails()
    print(emails)
    for pair in emails:
        # Extract name and email out of pair
        name = pair[0]
        email = pair[1]
        # Email content
        subject = 'Lorem ipsum dolor'
        content = 'Vestibulum tincidunt, sapien in laoreet lacinia, felis odio fringilla sapien, in maximus lorem erat vitae eros. Mauris faucibus magna vitae lacus elementum ultricies.'
        signature = 'Sincerely,\n\n\nName'
        body = f'Dear {name},\n\n{content}\n\n{signature} '

        msg = f'Subject:{subject}\n\n{body}'

        # Send email
        smtp.sendmail(EMAIL_ADDRESS, email, msg)
