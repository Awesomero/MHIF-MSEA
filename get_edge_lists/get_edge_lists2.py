import csv

input_file = 'get_edge_lists/edge_go/0.90.csv'
output_file = 'get_edge_lists/edge_go/0.90.txt'

result_list = []

with open(input_file, 'r') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        # Extract the first two columns and convert the values to integers.
        values = list(map(int, row[:2]))
        result_list.append(values)

# Write to the output file, separated by tabs.
with open(output_file, 'w') as txtfile:
    for values in result_list:
        txtfile.write('\t'.join(map(str, values)) + '\n')

print("Task completed, results have been written.", output_file)
