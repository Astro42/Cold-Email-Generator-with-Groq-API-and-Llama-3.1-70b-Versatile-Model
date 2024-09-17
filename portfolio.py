import pandas as pd  # Import the 'pandas' library for data manipulation and analysis.
import chromadb  # Import the 'chromadb' library for working with vector databases.
import uuid  # Import the 'uuid' library for generating unique identifiers.

class Portfolio:
    def __init__(self, file_path="Cold_Email_Generator_App/resources/my_portfolio.csv"):
        # Initialize the Portfolio class with a file path for the CSV file.
        # Load the data from the CSV file into a pandas DataFrame.
        self.file_path = file_path
        self.data = pd.read_csv(file_path)
        
        # Initialize the ChromaDB client for persistent storage.
        self.chroma_client = chromadb.PersistentClient('vectorstore')
        
        # Get or create a collection named "portfolio" in ChromaDB.
        self.collection = self.chroma_client.get_or_create_collection(name="portfolio")

    def load_portfolio(self):
        # Check if the collection is empty.
        if not self.collection.count():
            # Iterate over each row in the DataFrame.
            for _, row in self.data.iterrows():
                # Add each row's tech stack and links to the ChromaDB collection.
                # Generate a unique ID for each document.
                self.collection.add(documents=row["Techstack"],
                                    metadatas={"links": row["Links"]},
                                    ids=[str(uuid.uuid4())])

    def query_links(self, skills):
        # Query the ChromaDB collection for documents that match the given skills.
        # Return the metadata (links) of the top 2 results.
        return self.collection.query(query_texts=skills, n_results=2).get('metadatas', [])
