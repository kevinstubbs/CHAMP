'''
CHAMP (Convex Hull of Admissible Modularity Partitions) implementation
'''
from __future__ import absolute_import

from .plot_domains import plot_2d_domains
from .plot_domains import plot_single_layer_modularity_domains
from .plot_domains import plot_line_halfspaces
from .plot_domains import plot_line_coefficients
from .plot_domains import plot_similarity_heatmap_single_layer
from .plot_domains import plot_multilayer_community

from .champ_functions import create_coefarray_from_partitions
from .champ_functions import create_halfspaces_from_array
from .champ_functions import get_intersection
from .champ_functions import get_random_halfspaces

from .louvain_ext import create_multilayer_igraph_from_edgelist
from .louvain_ext import create_multilayer_igraph_from_adjacency
from .louvain_ext import call_slices_to_layers_from_edge_list
from .louvain_ext import PartitionEnsemble
from .louvain_ext import parallel_louvain
from .louvain_ext import run_louvain
from .louvain_ext import adjacency_to_edges





