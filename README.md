# Cold Email Generator with Streamlit and Groq AI (LLaMA 3.1 70B Versatile)

## Overview

The Cold Email Generator is a web application that helps you generate personalized cold emails based on job postings. The application extracts job details from URLs, cleans the extracted text, and uses the LLaMA 3.1 70B Versatile model via LangChain with Groq API to compose a customized email. It supports integration with popular email services, allowing you to send the generated email directly from the app.

## Features

- **URL Input**: Enter a URL to scrape job postings.
- **AI-Powered Email Composition**: Utilizes LLaMA 3.1 70B Versatile model for generating tailored emails.
- **Portfolio Integration**: Queries a portfolio database for relevant links based on job requirements.
- **Email Client Integration**: Opens email clients (Outlook, Gmail, Yahoo) with the generated email pre-filled.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Astro42/cold-email-generator.git
   cd cold-email-generator
   
2. Create a Virtual Environment (optional but recommended):
   ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`

3. Install Dependencies:
   ```bash
   pip install -r requirements.txt
   
4. Set Up Environment Variables:
   Create a .env file in the root directory.
   Add your API keys as follows:
   ```bash  
   GROQ_API_KEY=your_groq_api_key

4. Prepare Portfolio Data:
   Ensure you have a my_portfolio.csv file in the resources directory.

     
