from email import policy
from email.parser import BytesParser
import sys

def read_eml(eml_file):
    # Parse the EML file
    with open(eml_file, 'rb') as eml_data:
        msg = BytesParser(policy=policy.default).parse(eml_data)

    # Extract information from the parsed message
    subject = msg.get('Subject', 'No Subject')
    sender = msg.get('From', 'No Sender')
    recipients = msg.get_all('To', [])
    date = msg.get('Date', 'No Date')

    # Print email information
    print(f"Subject: {subject}")
    print(f"From: {sender}")
    print(f"To: {', '.join(recipients)}")
    print(f"Date: {date}")

    # Get the plain text body of the email
    plain_text_body = None
    for part in msg.iter_parts():
        if part.get_content_type() == 'text/plain':
            plain_text_body = part.get_payload(decode=True).decode(part.get_content_charset(), 'ignore')
            break

    if plain_text_body:
        print("\nBody:")
        print(plain_text_body)
    else:
        print("\nNo plain text body found.")

if __name__ == "__main__":

    # read input eml file path from CLI arguments 
    if len(sys.argv) != 2:
        print("Usage: python3 read_eml.py <eml_file_path>")
        sys.exit(1)

    eml_file = sys.argv[1]
    read_eml(eml_file)
    