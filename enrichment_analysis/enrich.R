"""
This section is written in R language for enrichment analysis.
R version: R 4.3.1
RStudio version: Open-source version (AGPL v3)
clusterProfiler version: 4.8.2
"""
library(clusterProfiler)

# Read the manually prepared background gene set.
background_genes <- read.delim('mirset.txt', stringsAsFactors = FALSE)

# Read the gene names (gene_id) from the miRNA gene list file.
miRNA_genes <- read.delim('BreastCancer_miRNA_Original_Lists.txt', stringsAsFactors = FALSE)$gene_id

# Extract disease names and miRNA names from the background gene set.
background_names <- background_genes[c('Description', 'gene_id')]

# Perform enrichment analysis.
enrichment_results <- enricher(gene = miRNA_genes,  # 待富集的miRNA基因列表
                               TERM2GENE = background_names,  # 背景基因集
                               # TERM2NAME = background_names,  # 使用相同的背景基因集作为TERM2NAME
                               pAdjustMethod = 'BH',
                               pvalueCutoff = 0.05,
                               qvalueCutoff = 0.2)

# Output enrichment results.
write.table(enrichment_results, 'BreastCancer_miRNA_Original_enrichment_results.txt', sep = '\t', row.names = FALSE, quote = FALSE)

# Visualize the results.
barplot(enrichment_results)  #富集柱形图
dotplot(enrichment_results)  #富集气泡图
