from resdk import Resolwe
from resdk.tables.rna import RNATables
import decoupler as dc

def fetch_gene_expression_data(dataset_name):
    """
    Fetch gene expression data for a specified dataset name from the Genialis platform.

    Parameters:
    - dataset_name (str): The name of the dataset to fetch gene expression data from.

    Returns:
    - pandas.DataFrame: A DataFrame containing the gene expression data with genes as rows,
      samples as columns, and expression values as entries. Columns and indices are renamed
      for readability.

    This function initializes a connection to Resolwe, retrieves a specific dataset collection,
    and processes the gene expression data for readability.
    """
    # Initialize Resolwe object with the URL of the Genialis platform.
    res = Resolwe(url='https://app.genialis.com')
    # Retrieve a collection from Resolwe by dataset name.
    collection = res.collection.get(dataset_name)
    # Initialize RNA tables for the collection with specified cache directory.
    tables = RNATables(collection)
    # Extract gene expression data as a pandas DataFrame.
    exp = tables.exp
    # Ensure that column names in the expression DataFrame are strings.
    exp.columns = exp.columns.astype(str)
    # Rename columns and indices in the DataFrame to more readable forms.
    exp = exp.rename(columns=tables.readable_columns, index=tables.readable_index)
    return exp
