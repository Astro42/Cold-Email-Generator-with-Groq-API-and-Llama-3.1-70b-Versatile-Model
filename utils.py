import re  # Import the 're' library for working with regular expressions.

def clean_text(text):
    # Remove HTML tags from the text using a regular expression.
    text = re.sub(r'<[^>]*?>', '', text)
    
    # Remove URLs from the text using a regular expression.
    text = re.sub(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', '', text)
    
    # Remove special characters (anything not a letter, number, or space) from the text.
    text = re.sub(r'[^a-zA-Z0-9 ]', '', text)
    
    # Replace multiple consecutive spaces with a single space.
    text = re.sub(r'\s{2,}', ' ', text)
    
    # Remove leading and trailing whitespace from the text.
    text = text.strip()
    
    # Remove extra whitespace by splitting the text into words and then joining them with a single space.
    text = ' '.join(text.split())
    
    return text  # Return the cleaned text.
