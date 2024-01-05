"""
This section is written in R language for miRNA differential expression filtering.
R version: R 4.3.1
RStudio version: Open-source version (AGPL v3)
clusterProfiler version: 4.8.2
"""
library(DESeq2)
library(dplyr)
# Import the counts data matrix, with genes as rows and samples as columns.
count <- read.csv("Merge_miRNA_pre_Count.txt",header=T,row.names=1)

## Filter genes with expression less than 1 in all replicate samples, as expression levels below this threshold are not meaningful for the study.
count <- count[rowMeans(count)>1,]

## Load sample information.
data <- read.table("sample_data.txt",header = T,row.names = 1)

# Ensure conversion to factor data; otherwise, errors may occur when using the DESeq2 package for analysis.
data[,1] <- as.factor(data$Type)

# Check if gene expression levels and sample information match; if TRUE, it indicates a successful match.
all(rownames(data) %in% colnames(count))
all(rownames(data) == colnames(count))

# Perform differential analysis.
dds <-  DESeqDataSetFromMatrix(countData = count,colData = data,design = ~ Type)
dim(dds)

# Filter the results.
dds <- dds[rowSums(counts(dds)) > 1,]
nrow(dds)

## Perform differential comparison.
dep <- DESeq(dds)
res <- results(dep)
diff = res
diff <- na.omit(diff)  ## 去除缺失值NA
dim(diff)

## Save the results of the differential analysis.
write.csv(diff,"all_diff.csv")

## Adjust p-values.
foldChange = 1
padj = 0.05

diffsig <- diff[(diff$pvalue < padj & abs(diff$log2FoldChange) > foldChange),]
dim(diffsig)

## Differentially expressed genes.
write.csv(diffsig, "All_diffsig.csv")