# Cold Email Generator with Streamlit and Groq AI (LLaMA 3.1 70B Versatile)

## Overview

The Cold Email Generator is a web application that helps you generate personalized cold emails based on job postings. The application extracts job details from URLs, cleans the extracted text, and uses the LLaMA 3.1 70B Versatile model via LangChain with Groq API to compose a customized email. It supports integration with popular email services, allowing you to send the generated email directly from the app.
**Note:** Due to security restrictions, web-based email clients do not support prepopulating the email body. As a result, the app currently redirects users to the web page of their email client, and users need to manually copy and paste the generated email content. Desktop clients may support prepopulating the email body in future updates.

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

5. Prepare Portfolio Data:
   Ensure you have a my_portfolio.csv file in the resources directory.


## File Descriptions

**main.py:**  This is the main entry point of the application. It sets up the Streamlit interface, handles user input, processes data, and integrates with the Chain, Portfolio, and EmailClient classes. It also provides functionality to generate and send cold emails.

**chains.py:** Contains the Chain class responsible for interacting with the language model to extract job postings and generate cold emails. It uses the Llama-3.1-70b versatile model from the Groq API.

**email_client.py:** Includes the EmailClient class which provides functionality to open pre-filled email drafts in different email services like Outlook, Gmail, and Yahoo Mail.

**portfolio.py:** Contains the Portfolio class that manages the portfolio data. It loads the portfolio from a CSV file and queries relevant links based on job requirements using ChromaDB.

**utils.py:** Provides utility functions, including clean_text, which preprocesses and cleans text extracted from web pages by removing HTML tags, URLs, special characters, and extra whitespace.

## my_portfolio.csv File
The my_portfolio.csv file contains information about your technical skills and portfolio links. It should have the following columns:

**Techstack:** A description of your technical skills and tools.
**Links:** URLs to your portfolio, projects, or relevant work samples.

This file is loaded by the Portfolio class and is used to provide relevant links when generating cold emails.

## Running the App
To run the Streamlit app, execute the following command in your terminal:
```bash
streamlit run main.py
