import streamlit as st  # Import Streamlit for creating the interactive web app.
from langchain_community.document_loaders import WebBaseLoader  # Import WebBaseLoader to load content from URLs.
from chains import Chain  # Import the Chain class for handling job extraction and email composition.
from portfolio import Portfolio  # Import Portfolio class to manage and query portfolio data.
from utils import clean_text  # Import clean_text function to preprocess and clean the text from URLs.
from email_client import EmailClient  # Import EmailClient to handle opening email clients with the pre-filled email body.

# Function to create the Streamlit app
def create_streamlit_app(llm, portfolio, clean_text):
    st.title("Cold E-Mail Generator")  # Title of the app

    # Input box for the user to enter a URL
    url_input = st.text_input("Enter a URL:", value=" ")  
    submit_button = st.button("Submit")  # Submit button to trigger the process

    if submit_button:
        try:
            # Use the WebBaseLoader to load data from the URL
            loader = WebBaseLoader([url_input])
            # Clean the loaded text (remove unwanted characters, etc.)
            data = clean_text(loader.load().pop().page_content)
            
            # Load the portfolio information (skills and links)
            portfolio.load_portfolio()
            # Extract jobs from the cleaned data using the LLM
            jobs = llm.extract_jobs(data)
            
            # Loop through each job posting extracted
            for job in jobs:
                # Get the required skills for the job
                skills = job.get('skills', [])
                # Query the portfolio for relevant links based on the skills
                links = portfolio.query_links(skills)
                # Generate the email using the LLM and the job details
                email = llm.write_mail(job, links)
                
                # Store the generated email in session state to prevent it from disappearing
                st.session_state.generated_email = email

        except Exception as e:
            # If any error occurs, show the error message on the screen
            st.error(f"An Error Occurred: {e}")

    # Always display the generated email if it exists in session state
    if "generated_email" in st.session_state and st.session_state.generated_email:
        st.code(st.session_state.generated_email, language='markdown')

    # Show the email service dropdown with a blank default option
    st.session_state.email_service = st.selectbox(
        "Select Email Service", ["", "Outlook", "Gmail", "Yahoo"], index=0
    )

    # Ensure the "Send Email" button is only shown after an email service is selected
    if st.session_state.email_service and st.session_state.email_service != "":
        # Add a "Send Email" button
        send_email_button = st.button("Send Email")

        # If the user clicks the "Send Email" button
        if send_email_button:
            # Ensure the email was generated before proceeding
            if "generated_email" in st.session_state and st.session_state.generated_email:
                # Create an EmailClient instance based on the selected service
                email_client = EmailClient(service=st.session_state.email_service)
                # Use the email client to open the email service with the generated email content
                email_client.open_email_client(st.session_state.generated_email)
            else:
                st.error("No email content available to send.")

# Main entry point for the app
if __name__ == "__main__":
    # Initialize the Chain and Portfolio objects
    chain = Chain()
    portfolio = Portfolio()
    
    # Configure the Streamlit app (wide layout, page title, and page icon)
    st.set_page_config(layout="wide", page_title="Cold Email Generator", page_icon="📧")
    
    # Run the Streamlit app with the chain, portfolio, and clean_text function
    create_streamlit_app(chain, portfolio, clean_text)
