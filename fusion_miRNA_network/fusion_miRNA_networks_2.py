""" Fusion miRNA Similarity Network
4.Matrix Fusion: The fused miRNA similarity matrix obtained in the third step only
includes the similarity of shared miRNA. Therefore, it is necessary to add the similarity of unique miRNA from
individual miRNA similarity matrices to the fused miRNA similarity matrix obtained in the third step.
"""
import pandas as pd

# Read two miRNA similarity matrices.
matrix_file = "./data/go_similar.xlsx"
new_matrix_file = "./go_seq/average_similarity_matrix_go_seq.xlsx"
matrix = pd.read_excel(matrix_file, index_col=0, engine='openpyxl')
new_matrix = pd.read_excel(new_matrix_file, index_col=0, engine='openpyxl')

# Read the list of miRNA names.
miRNA_list_file = "intersection_list_go_seq.txt"
with open(miRNA_list_file, "r") as file:
    miRNA_list = [line.strip() for line in file]

# In the new matrix, select the similarity corresponding to miRNAs in the list and replace it in the original matrix.
matrix.loc[miRNA_list, miRNA_list] = new_matrix.loc[miRNA_list, miRNA_list]

# Save the modified similarity matrix.
output_file = "./go_seq/u_average_similarity_matrix_go_seq.xlsx"
matrix.to_excel(output_file)
