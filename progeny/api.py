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
    # Extract gene expression data as TPM-normalized reads.
    exp = tables.exp
    # Ensure that column names in the expression DataFrame are strings for renaming.
    exp.columns = exp.columns.astype(str)
    # Rename columns and indices in the DataFrame to more readable forms.
    exp = exp.rename(columns=tables.readable_columns, index=tables.readable_index)
    return exp

def calculate_progeny_scores(expression_data):
    """
    Calculate PROGENy scores for the provided gene expression data.

    Parameters:
    - expression_data (pandas.DataFrame): The gene expression data for which to calculate
      PROGENy scores. It should have samples as rows and genes as columns.

    Returns:
    - pandas.DataFrame: A DataFrame containing the PROGENy scores for the specified dataset,
      with samples as rows and pathways as columns.

    This function uses the decoupler library to compute PROGENy (Pathway RespOnsive GENes)
    scores, estimating pathway activity based on gene expression data.
    """
    # Get the PROGENy network for human organism.
    progeny = dc.get_progeny(organism='human')

    # Calculate pathway activity scores using machine learning model.
    result = dc.run_mlm(
        mat=expression_data, # Input expression data.
        net=progeny, # Network data (PROGENy).
        source='source',
        target='target',
        weight='weight',
        verbose=True # Print additional information during calculation.
    )

    return result[0]
