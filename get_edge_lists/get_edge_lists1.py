import csv

# Read CSV file
input_file = 'data/miRNA_similarity_networks/go_similarity.csv'
output_file = 'get_edge_lists/edge_go/0.90.txt'

# Save rows, columns, and similarity values that meet the conditions.
result_list = []

with open(input_file, 'r', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    matrix = [row for row in reader]

# Iterate through the similarity matrix.
for i in range(0, len(matrix)):
    for j in range(0, len(matrix[i])):
        similarity = float(matrix[i][j])
        if 0.58 <= similarity < 1:
            result_list.append([i, j, similarity])

# Write to the output file.
with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(result_list)

print("Task completed, results have been written.", output_file)
