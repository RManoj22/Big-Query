import os
from google.cloud import bigquery
from dotenv import load_dotenv

# Function to authenticate and set GOOGLE_APPLICATION_CREDENTIALS environment variable
def authenticate_with_credentials(credentials_path):
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = credentials_path
    load_dotenv()  # Load environment variables from .env file if needed

# Function to list datasets in a project
def list_tables_in_dataset(project_id, dataset_name):
    client = bigquery.Client(project=project_id)
    dataset_ref = client.dataset(dataset_name)
    
    try:
        tables = list(client.list_tables(dataset_ref))  # List all tables in the dataset
        return [table.table_id for table in tables] if tables else []
    except Exception as e:
        print(f"Error listing tables: {e}")
        return []

def get_columns_for_table(project_id, dataset_name, table_name):
    client = bigquery.Client(project=project_id)
    table_id = f"{project_id}.{dataset_name}.{table_name}"
    table = client.get_table(table_id)  # Fetch the table
    return [schema_field.name for schema_field in table.schema]  # Return column names

