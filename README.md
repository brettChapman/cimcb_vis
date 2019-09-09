# MultiVis
The MultiVis package contains the necessary tools for visualisation of multivariate data.

## Installation

### Dependencies
multivis requires:
- Python (>=3.5)
- NumPy (>=1.12)
- Pandas
- Matplotlib
- Seaborn
- Networkx
- SciPy
- Scikit-learn
- tqdm
- xlrd

### User installation
The recommend way to install cimcb_vis and dependencies is to using ``conda``:
```console
conda install -c brett.chapman multivis
```
or ``pip``:
```console
pip install multivis
```
Alternatively, to install directly from github:
```console
pip install https://github.com/brettChapman/multivis/archive/master.zip
```

### API
For further detail on the usage refer to the docstring.

#### multivis
- [Edge](https://github.com/brettChapman/multivis/blob/master/multivis/Edge.py#L7-L429): Generates dataframe of nodes and edges.
	- [init_parameters](https://github.com/brettChapman/multivis/blob/master/multivis/Edge.py#L24-L33)
		- [peaktable] : Pandas dataframe containing peak data.
		- [scores] : Pandas dataframe containing correlation coefficients.
		- [pvalues] : Pandas dataframe containing correlation pvalues.
	- [methods](https://github.com/brettChapman/multivis/blob/master/multivis/Edge.py#L35-54)
		- [set_params] : Set parameters - filter score type, hard threshold, internal correlation flag and sign type
		- [run] : Builds the nodes and edges
		- [getNodes] : Returns a Pandas dataframe of all nodes.
		- [getEdges] : Returns a Pandas dataframe of all edges.

- [Network](https://github.com/brettChapman/multivis/blob/master/multivis/Network.py#L6-L109): Inherits from Edge and generates dataframe of nodes and edges, and a networkx graph.
	- [init_parameters](https://github.com/brettChapman/multivis/blob/master/multivis/Network.py#L25-L29)
		- [peaktable] : Pandas dataframe containing peak data.
		- [scores] : Pandas dataframe containing correlation coefficients.
		- [pvalues] : Pandas dataframe containing correlation pvalues.
	- [methods](https://github.com/brettChapman/multivis/blob/master/multivis/Network.py#L31-L51)
		- [set_params] : Set parameter - filter score type, hard threshold, internal correlation flag and sign type.
                - [run] : Builds nodes, edges and NetworkX graph.
                - [getNetworkx] : Returns a NetworkX graph.
                - [getLinkType] : Returns the link type parameter used in building the network.

- [edgeBundle](https://github.com/brettChapman/multivis/blob/master/multivis/edgeBundle.py#L9-L1304): Generates and displays a Hierarchical edge bundle plot.
	- [init_parameters](https://github.com/brettChapman/multivis/blob/master/multivis/edgeBundle.py#L23-27)
		- [edges] : Pandas dataframe containing edges generated from Edge.
	- [methods](https://github.com/brettChapman/multivis/blob/master/multivis/edgeBundle.py#L29-L99)
		- [set_params] : Set parameters - diameter, inner radius offset, group separation, link fade opacity, mouse over flag, font size, background colour, foreground colour, filter slider position offset, colour scale (value to colour edges by: 'Score' or 'Pvalue') and CMAP colour palette for edges.
		- [run] : Generates and outputs the hierarchical edge bundle.
		
- [plotNetwork](https://github.com/brettChapman/multivis/blob/master/multivis/plotNetwork.py#L12-L346): Generates and displays a static NetworkX graph given a user defined layout.
	- [init_parameters](https://github.com/brettChapman/multivis/blob/master/multivis/plotNetwork.py#L26-L32)
		- [g] : NetworkX graph.
	- [methods](https://github.com/brettChapman/multivis/blob/master/multivis/plotNetwork.py#L34-L191)
		- [set_params] : Set parameters - node parameters dictionary(node sizing columnn, node size scale, node size range, alpha opacity value, node labelling flag, font size and keep single nodes flag)
                				, filter parameters dictionary(filter column, filter threshold, filter operator and sign)
						, image filename, label edges flag, save image flag, NetworkX layout type, dpi, figure size.
		- [run] : Generates and displays the NetworkX graph.

- [springNetwork](https://github.com/brettChapman/multivis/blob/master/multivis/springNetwork.py): Interactive spring-embedded network which inherits data from the NetworkX graph.
	- [init_parameters](https://github.com/brettChapman/multivis/blob/master/multivis/springNetwork.py#L9-L1015)
		- [g] : NetworkX graph.
	- [methods](https://github.com/brettChapman/multivis/blob/master/multivis/springNetwork.py#L36-L101)
		- [set_params] : Set parameters - node parameters dictionary(node text size, fix node when moved flag, display node label flag
                                                        			, node size scale dictionary(peak table columns as index: dictionary(index as "scale": values ("linear", "reverse_linear", "log", "reverse_log"
                                                                                                            , "square", "reverse_square", "area", "reverse_area", "volume", "reverse_volume")
																			, index as "range": a number array of length 2)))
						, link parameters dictionary(link type used in building the network, link width
                                                        , link score colour dictionary("positive": colour value, "negative": colour value)) # Colour values can be HTML/CSS name, hex code, and (R,G,B) tuples
                                                        , background colour, foreground colour, canvas size, charge strength
		- [run] : Generates and returns JavaScript embedded HTML code for writing to HTML and displaying.

- [clustermap](https://github.com/brettChapman//multivis/blob/master/multivis/clustermap.py): Hierarchical Clustered Heatmap.
	- [init_parameters](https://github.com/brettChapman//multivis/blob/master/multivis/clustermap.py#L29-L39)
		- [scores] : Pandas dataframe containing similarity scores (e.g. correlation coefficients or Euclidean distance values).
		- [row_linkage] : Precomputed linkage matrix for the rows from a linkage clustered scores matrix
		- [col_linkage] : Precomputed linkage matrix for the columns from a linkage clustered scores matrix
	- [methods](https://github.com/brettChapman//multivis/blob/master/multivis/clustermap.py#L41-L331)
		- [set_params] : Set parameters - image file name, save image flag, dpi, figure size, ratio to shift position of dendrograms, font size
                                        	, heatmap parameters dictionary(X axis labels, Y axis labels, CMAP colour palette)
						, clustering parameters dictionary(CMAP colour palette, colour the row clusters flag, colour the column clusters flag, row colour clustering threshold, coloumn colour clustering threshold)
		- [run] : Generates and displays the Hierarchical Clustered Heatmap (HCH).

- [polarDendrogram](https://github.com/brettChapman/multivis/blob/master/multivis/polarDendrogram.py): Polar dendrogram
	- [init_parameters](https://github.com/brettChapman/multivis/blob/master/multivis/polarDendrogram.py#L22-L27)
		- [dn] : Dendrogram dictionary.
	- [methods](https://github.com/brettChapman/multivis/blob/master/multivis/polarDendrogram.py#L29-L144)
		- [set_params] : Set parameters - image file name, save image flag, dendrogram branch scale type ('linear', 'log', 'square'), gap value, display grid flag, style-sheet type, dpi, figure size
                                            , text parameters dictionary(font size, text colours dictionary(index from peak table: values as colours), text labels dictionary(index from peak table: values as labels from peak table))
		- [run] : Generates and displays the Polar dendrogram.

#### multivis.utils

TODO --add parameters and methods to below tools

- [loadData](https://github.com/brettChapman/multivis/blob/master/multivis/utils/loadData.py): Loads and validates the Data and Peak sheet from an excel file.
- [mergeBlocks](https://github.com/brettChapman/multivis/blob/master/multivis/utils/mergeBlocks.py): Merges multiply different data blocks into a single peak table and data table.
- [range_scale](https://github.com/brettChapman/multivis/blob/master/multivis/utils/range_scale.py): Scales a range of values between user chosen values.
- [corrAnalysis](https://github.com/brettChapman/multivis/blob/master/multivis/corrAnalysis.py): Correlation analysis with Pearson, Spearman or Kendall's Tau.
- [cluster](https://github.com/brettChapman/multivis/blob/master/multivis/utils/spatialClustering.py): Clusters data using a linkage cluster method. If the data is correlated the correlations are first preprocessed, then clustered, otherwise a distance metric is applied to non-correlated data before clustering.

### License
Multivis is licensed under the MIT license.

### Authors
- Brett Chapman
- https://scholar.google.com.au/citations?user=A_wYNAQAAAAJ&hl=en

### Correspondence
Dr. Brett Chapman, Post-doctoral Research Fellow at the Centre for Integrative Metabolomics & Computational Biology at Edith Cowan University.
E-mail: brett.chapman@ecu.edu.au, brett.chapman78@gmail.com

### Citation
If you would cite multivis in a scientific publication, you can use the following: [currently pending publication submission]
