# Automated Emails
Program to help me get information from a lot of colleges at once. Takes the name of the college and its email, and uses a predefined message for the email itself. The program formats the college's name into the message, and sends it to the provided email address.

Modules needed: 
- SSL
- Smtplib
- Email.message
- Datetime

Caveats: 
- Emails from non-SSL-certified emails (eg., my myles@5050creative.com account) don't deliver or get sorted into the reciever's trash
- Emails sent from the program get grouped together in other email clients (eg., Apple Mail), it'll be one email chain of all the sent emails
- Can't read emails off of a CSV sheet- all emails and college names need to be entered in one at a time

Very little commit history for the files because there was sensitive information in the commit history, was deleted for the final verison.
