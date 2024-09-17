import urllib.parse  # Import the 'urllib.parse' module for URL encoding.
import streamlit as st  # Import the 'streamlit' module for creating interactive web apps.

class EmailClient:
    def __init__(self, service="outlook"):
        # Initialize the EmailClient class with a default email service (converted to lowercase).
        self.service = service.lower()

    def open_email_client(self, email_body):
        # Encode the email body to make it safe for use in URLs (handles special characters).
        encoded_email_body = urllib.parse.quote(email_body)

        # Decide which email client to open based on the selected service.
        if self.service == "outlook":
            self._open_outlook(encoded_email_body)  # Call the method to open Outlook.
        elif self.service == "gmail":
            self._open_gmail(encoded_email_body)  # Call the method to open Gmail.
        elif self.service == "yahoo":
            self._open_yahoo(encoded_email_body)  # Call the method to open Yahoo Mail.
        else:
            # Show an error if the email service is not supported.
            st.error("Email service not supported")

    def _open_outlook(self, encoded_email_body):
        # Create a URL to open the Outlook web email composer with the encoded email body.
        mailto_link = f"https://outlook.live.com/mail/0/?view=cm&fs=1&body={encoded_email_body}"
        # Display the link as a clickable markdown link in the Streamlit app.
        st.markdown(f"[Send via Outlook]({mailto_link})")

    def _open_gmail(self, encoded_email_body):
        # Create a URL to open the Gmail web email composer with the encoded email body.
        mailto_link = f"https://mail.google.com/mail/?view=cm&fs=1&body={encoded_email_body}"
        # Display the link as a clickable markdown link in the Streamlit app.
        st.markdown(f"[Send via Gmail]({mailto_link})")

    def _open_yahoo(self, encoded_email_body):
        # Create a URL to open the Yahoo Mail web email composer with the encoded email body.
        mailto_link = f"https://compose.mail.yahoo.com/?body={encoded_email_body}"
        # Display the link as a clickable markdown link in the Streamlit app.
        st.markdown(f"[Send via Yahoo Mail]({mailto_link})")
