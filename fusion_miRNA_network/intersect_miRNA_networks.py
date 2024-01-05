""" Fusion miRNA Similarity Network
1.Obtain the intersection of multiple miRNA similarity networks.
"""
import openpyxl
import pandas as pd

# Obtain the user-submitted list of differentially expressed miRNAs.
mirna_list = pd.read_excel('mirna_name_go.xlsx', header=None, names=['miRNA'], engine='openpyxl')
miRNA_list = mirna_list['miRNA'].tolist()
print(miRNA_list)

# user_list_num represents the number of lncRNAs in the differentially expressed miRNA list submitted by the user.
user_list_num = len(mirna_list)

# ----------------------Generate the intersection of differentially expressed lncRNAs and all miRNAs--------------------
wb1 = openpyxl.load_workbook('mirna_name_seq.xlsx')  # 取出全部miRNA
sh1 = wb1['Sheet1']
# Initialize the list for the intersection of lncRNAs.
intersection_list = []
# Find the intersection between the user-submitted list and all lncRNAs.
for i in range(user_list_num):
    for j in range(495):
        if mirna_list['miRNA'][i] == sh1.cell(j + 1, 1).value:
            intersection_list.append(mirna_list['miRNA'][i])

# Save the intersection list to a txt file.
with open('intersection_list_go_seq.txt', 'w') as file:
    for item in intersection_list:
        file.write("%s\n" % item)