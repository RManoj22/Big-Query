import streamlit as st
from Utils.big_query_handler import authenticate_with_credentials, list_tables_in_dataset, get_columns_for_table

default_project_id = "bigquery-public-data"
default_dataset_name = "google_trends"

# Streamlit UI for file upload and input fields
st.title("Google BigQuery Table Viewer")

# Upload JSON key for Google Cloud credentials
uploaded_file = st.file_uploader("Upload Google Cloud Service Account JSON Key", type="json")
project_id = st.text_input("Project ID", default_project_id)
dataset_name = st.text_input("Dataset Name", default_dataset_name)

# Authenticate with the uploaded JSON file if available
if uploaded_file is not None:
    # Save the uploaded file to a temporary location
    with open("temp_credentials.json", "wb") as f:
        f.write(uploaded_file.getbuffer())
    
    # Authenticate using the uploaded JSON file
    authenticate_with_credentials("temp_credentials.json")
    st.success("Authentication successful!")

# Button to trigger the listing of tables
if st.button("List Tables"):
    if project_id and dataset_name:
        # List tables in the provided dataset
        tables = list_tables_in_dataset(project_id, dataset_name)
        
        if tables:
            st.write(f"Tables in dataset '{dataset_name}':")
            # Iterate over the tables and create an expander for each table
            for table in tables:
                with st.expander(table):  # Create a dropdown arrow for each table
                    # Get columns for the current table
                    columns = get_columns_for_table(project_id, dataset_name, table)
                    
                    if columns:
                        st.write(f"Columns in table '{table}':")
                        for column in columns:
                            st.write(f"- {column}")
                    else:
                        st.write(f"No columns found for table '{table}' or error occurred.")
        else:
            st.write(f"No tables found in dataset '{dataset_name}' or error occurred.")
    else:
        st.error("Please provide both Project ID and Dataset Name.")
