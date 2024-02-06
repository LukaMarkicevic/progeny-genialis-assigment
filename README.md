
# Progeny-Genialis-Assignment

This Python package provides tools for fetching gene expression data from the Genialis platform and calculating PROGENy (Pathway RespOnsive GENes) scores. PROGENy scores estimate pathway activity based on gene expression data, offering insights into the biological pathways active in your dataset.

## Installation

Clone this repository and navigate to the project directory. You can install the package and its dependencies using the following command:

```
pip install -e .
```

This command will install the `progeny-genialis-assignment` package along with its required dependencies, including `resdk`, `decoupler`, `omnipath`, and `pytest` for testing.

## Project Structure

```
progeny/
├── __init__.py
├── api.py
└── cli.py
setup.py
```

- `progeny/api.py`: Contains the core functionality for fetching gene expression data and calculating PROGENy scores.
- `progeny/cli.py`: Implements the command-line interface for the package.
- `setup.py`: Configures the package setup, dependencies, and entry points.

## Features

- **Fetch Gene Expression Data**: Retrieve gene expression data from a specified dataset on the Genialis platform.
- **Calculate PROGENy Scores**: Compute PROGENy scores from gene expression data to assess pathway activities.

## Usage

### Command Line Interface

The package includes a command-line interface (CLI) to fetch gene expression data and calculate PROGENy scores. Use the CLI as follows:

```
progeny <dataset_name>
```

Replace `<dataset_name>` with the name of your dataset on the Genialis platform. The CLI will fetch the gene expression data for the specified dataset, calculate the PROGENy scores, and save them to a CSV file in the `./progeny_scores` directory.

### API Usage

You can also use the package's API directly in your Python scripts:

```python
from progeny.api import fetch_gene_expression_data, calculate_progeny_scores

# Fetch gene expression data
data = fetch_gene_expression_data('your_dataset_name')

# Calculate PROGENy scores
scores = calculate_progeny_scores(data)

# Now, you can work with the 'scores' DataFrame as needed
```