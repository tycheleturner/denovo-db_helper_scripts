#!/bin/python3

import pandas as pd
import argparse
import sys

def load_and_filter(filepath, gene, allowed_consequences):
    try:
        df = pd.read_csv(filepath, compression='gzip', delimiter='\t', low_memory=False)
    except Exception as e:
        print(f"Error reading {filepath}: {e}", file=sys.stderr)
        sys.exit(1)

    df_gene = df[df['SYMBOL'] == gene]
    if df_gene.empty:
        raise ValueError(f"No data found for gene: {gene} in file: {filepath}")

    print(f"Unique consequences for {gene} in {filepath}:", df_gene['Consequence'].unique())
    df_filtered = df_gene[df_gene['Consequence'].isin(allowed_consequences)]
    print(f"Unique phenotypes for {gene} in {filepath}:", df_filtered['PHENOTYPE'].unique())
    return df_filtered

def main():
    parser = argparse.ArgumentParser(description="Filter denovo-db files by gene and consequence.")
    parser.add_argument('--nonssc', required=True, help='Path to non-SSC gzip file')
    parser.add_argument('--ssc', required=True, help='Path to SSC gzip file')
    parser.add_argument('--gene', required=True, help='Gene symbol to filter by')
    parser.add_argument('--consequences', nargs='*', default=[
        'frameshift_variant',
        'missense_variant',
        'splice_donor_variant',
        'stop_gained'
    ], help='List of allowed variant consequences')

    args = parser.parse_args()

    try:
        nonssc_filtered = load_and_filter(args.nonssc, args.gene, args.consequences)
        nonssc_filtered.to_csv(f"{args.gene}_denovodb_nonssc.tsv", sep='\t', index=False)

        ssc_filtered = load_and_filter(args.ssc, args.gene, args.consequences)
        ssc_filtered.to_csv(f"{args.gene}_denovodb_ssc.tsv", sep='\t', index=False)

    except ValueError as ve:
        print(f"Error: {ve}", file=sys.stderr)
        sys.exit(2)

if __name__ == '__main__':
    main()

