""" Fusion miRNA Similarity Network
3.Matrix Fusion: After the second-step processing, the matrices should have the same rows and columns,
with each position's similarity corresponding to one another.
Therefore, the specific method for fusing multiple processed matrices is to compute the mean.
"""
import pandas as pd

# Read multiple similarity matrix files.
matrix1 = pd.read_excel('./go_seq/filtered_similarity_dis.xlsx', index_col=0, engine='openpyxl')
matrix2 = pd.read_excel('./go_seq/filtered_similarity_go.xlsx', index_col=0, engine='openpyxl')
matrix3 = pd.read_excel('./go_seq/filtered_similarity_seq.xlsx', index_col=0, engine='openpyxl')

# Calculate the average of two or three similarity matrices.
# average_matrix = (matrix1 + matrix2) / 2
average_matrix = (matrix1 + matrix2 + matrix3) / 3

# Save the new similarity matrix to a file.
average_matrix.to_excel('./go_seq/average_similarity_matrix_go_seq.xlsx')
