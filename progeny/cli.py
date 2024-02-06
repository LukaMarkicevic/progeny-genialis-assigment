import argparse
import os
from progeny.api import fetch_gene_expression_data, calculate_progeny_scores

def main():
    # Initialize argument parser to handle command line inputs.
    parser = argparse.ArgumentParser(description="Retrieve PROGENy scores for a dataset.")
    # Add an argument for the dataset name, which is required to fetch gene expression data.
    parser.add_argument('dataset_name', type=str, help="Name of the dataset")
    
    # Parse the arguments provided by the user on the command line.
    args = parser.parse_args()
    
    # Fetch gene expression data for the specified dataset name using the provided API.
    data = fetch_gene_expression_data(args.dataset_name)
    # Calculate PROGENy scores based on the fetched gene expression data.
    scores = calculate_progeny_scores(data)
    
    # Ensure the directory for saving PROGENy scores exists.
    os.makedirs("./progeny_scores", exist_ok=True)
    # Save the PROGENy scores to a CSV file in the specified directory.
    scores.to_csv(f"./progeny_scores/{args.dataset_name}_progeny_scores.csv")
    # Inform the user where the PROGENy scores have been saved.
    print(f"PROGENy scores for dataset {args.dataset_name} have been saved to ./progeny_scores/{args.dataset_name}_progeny_scores.csv")

if __name__ == "__main__":
    main()