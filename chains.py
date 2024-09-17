import os  # Import the 'os' module to interact with the operating system, such as accessing environment variables.
from langchain_groq import ChatGroq  # Import the 'ChatGroq' class from the 'langchain_groq' module, used to interact with the Groq API.
from langchain_core.prompts import PromptTemplate  # Import 'PromptTemplate' from 'langchain_core.prompts' to create prompts for the model.
from langchain_core.output_parsers import JsonOutputParser  # Import 'JsonOutputParser' from 'langchain_core.output_parsers' to parse JSON outputs from the model.
from langchain_core.exceptions import OutputParserException  # Import 'OutputParserException' to handle errors when parsing output.
from dotenv import load_dotenv  # Import 'load_dotenv' from 'dotenv' to load environment variables from a .env file.

load_dotenv()  # Load environment variables from a .env file. This makes API keys and other sensitive information available.

class Chain:
    def __init__(self):
        # Initialize the Chain class. This sets up the language model with a specific API key and model name.
        self.llm = ChatGroq(temperature=0, groq_api_key=os.getenv("GROQ_API_KEY"), model_name="llama-3.1-70b-versatile")

    def extract_jobs(self, cleaned_text):
        # Create a prompt template to extract job postings from text. This defines how the text should be processed by the model.
        prompt_extract = PromptTemplate.from_template(
            """
            ### SCRAPED TEXT FROM WEBSITE:
            {page_data}
            ### INSTRUCTION:
            The scraped text is from the career's page of a website.
            Your job is to extract the job postings and return them in JSON format containing the following keys: `role`, `experience`, `skills` and `description`.
            Only return the valid JSON.
            ### VALID JSON (NO PREAMBLE):
            """
        )
        # Create a chain that combines the prompt with the language model for extracting job postings.
        chain_extract = prompt_extract | self.llm
        # Invoke the chain with the cleaned text to extract job postings.
        res = chain_extract.invoke(input={"page_data": cleaned_text})
        try:
            # Create a JSON parser to parse the output from the model.
            json_parser = JsonOutputParser()
            # Parse the result into JSON format.
            res = json_parser.parse(res.content)
        except OutputParserException:
            # Handle the case where JSON parsing fails due to large context size.
            raise OutputParserException("Context too big. Unable to parse jobs.")
        # Return the result, ensuring it is a list of job postings.
        return res if isinstance(res, list) else [res]

    def write_mail(self, job, links):
        # Create a prompt template to generate an email based on the job description and portfolio links.
        prompt_email = PromptTemplate.from_template(
            """
            ### JOB DESCRIPTION:
            {job_description}

            ### INSTRUCTION:
            Your name is Astro42, a Senior Vice President at Astro Inc. Astro Inc is a Data, AI & Software Consulting company dedicated to facilitating
            the seamless integration of business processes through automated tools. 
            Over our experience, we have empowered numerous enterprises with tailored solutions, fostering scalability, 
            process optimization, cost reduction, and heightened overall efficiency. 
            Your job is to write a cold email to the client regarding the job mentioned above describing the capability of Astro
            in fulfilling their needs.
            Also add the most relevant ones from the following links to showcase Astro's portfolio: {link_list}
            Remember you are Nidheesh, BDE at Astro. 
            Do not provide a preamble.
            ### EMAIL (NO PREAMBLE):
            """
        )
        # Create a chain that combines the email prompt with the language model for generating the email.
        chain_email = prompt_email | self.llm
        # Invoke the chain with the job details and portfolio links to generate the email.
        res = chain_email.invoke({"job_description": str(job), "link_list": links})
        # Return the content of the generated email.
        return res.content

# This part of the code runs only if the script is executed directly (not imported as a module).
if __name__ == "__main__":
    # Print the Groq API key to the console (for debugging purposes, it should be kept secure).
    print(os.getenv("GROQ_API_KEY"))


# Explanation:
# Imports: Bringing in necessary modules and classes to work with environment variables, interact with APIs, and handle JSON.
# load_dotenv(): Loads environment variables (like API keys) from a .env file.
# Class Definition: Chain class that initializes a language model and provides methods for extracting job postings and writing emails.
# extract_jobs Method: Uses a prompt template to guide the model in extracting job postings from cleaned text and parsing the result into JSON.
# write_mail Method: Uses a prompt template to generate a cold email based on the job description and portfolio links.
# Main Block: Runs code when the script is executed directly, useful for debugging or standalone execution.