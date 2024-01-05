# MHIF-MSEA
Source code for paper "MHIF-MSEA：a novel model of miRNA functional enrichment analysis based on multi-source heterogeneous information fusion".

------

## data

Data obtained from different biological databases are preprocessed and a heterogeneous information network consisting of three miRNA similarity networks (Disease-Based, Target Gene GO Annotation-Based, Protein Sequence-Based)
## Fuse miRNA  Similarity Network 
------
In this section, we fused the three miRNA similarity matrices obtained from the data preprocessing step. We perform fusion between any two networks and aggregate.The specific steps for this fusion are as follows:

1. Obtain the intersection of multiple miRNA similarity networks.

```python
cd fusion_miRNA_network
python intersect_miRNA_networks.py
```

2. Process individual miRNA similarity network, remove similarity data for miRNA not in the intersection.

```python
python process_individual_miRNA_similarity_matrix.py
```

3. Matrix Fusion: After the second-step processing, the matrices should have the same rows and columns, with each position's similarity corresponding to one another.Therefore, the specific method for fusing multiple processed matrices is to compute the mean.

```python
python fusion_miRNA_networks_1.py
```

4. Matrix Fusion: The fused miRNA similarity matrix obtained in the third step only includes the similarity of shared miRNA. Therefore, it is necessary to add the similarity of unique miRNA from individual miRNA similarity matrices to the fused miRNA similarity matrix obtained in the third step. 
```python
python fusion_miRNA_networks_2.py
```
## Get Edge Lists
------
In this step, we extract edges from the miRNA similarity network where the similarity is greater than 0.6. These edges form an edge table, which serves as the input for Random Walk with Restart (RWR).Its specific steps are divided into the following two:

1. Retrieve edges with a similarity greater than 0.6 along with their corresponding similarity scores.
```python
cd get_edge_lists
python get_edge_lists1.py
```

2. Process the results from the previous step to format them as follows (tab-separated).

```python
python get_edge_lists2.py
```
```python
# format: source (int) \t target (int)
1	2
1	4
2	3
...
```
## Expand miRNA Lists
------
In this section, we expanded the miRNA list using a random walk algorithm with restarts, and then conduct enrichment analysis on the expanded list.

First, you need to install the code for the random walk algorithm with restarts for use. Click on "[pyrwr](https://github.com/jinhongjung/pyrwr)" to download it.

Then, integrate the pyrwr package and configure it for your project to start using it. We achieve our objectives by calling its interface.


```python
python expend_lists.py
```
## Enrichment analysis
Performing enrichment analysis using R language, and the source code is provided in the project.

```R
source("enrich.R")
```

