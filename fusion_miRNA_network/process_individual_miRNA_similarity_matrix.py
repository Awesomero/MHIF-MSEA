""" Fusion miRNA Similarity Network
2.Process individual miRNA similarity network, remove similarity data for miRNA not in the intersection.
"""
import pandas as pd

# Read the similarity matrix file.
similarity_matrix = pd.read_excel('./data/go_similar.xlsx', index_col=0,engine='openpyxl')

# Read the file containing the list of miRNA names.
miRNA_list = pd.read_csv('intersection_list_go_seq.txt', header=None, names=['miRNA'])

# Obtain the similarity matrix for the intersected miRNAs.
filtered_similarity_matrix = similarity_matrix.loc[miRNA_list['miRNA'], miRNA_list['miRNA']]

# Save the new similarity matrix to a file.
filtered_similarity_matrix.to_excel('./go_seq/filtered_similarity_go.xlsx')
