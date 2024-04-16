#%% Import librarires
from pathlib import Path
import numpy as np

#%% Load data
root = Path(r"e:\18082023_Milka_StrCer_S4_g0\18082023_Milka_StrCer_S4_g0_imec0\ks4_wCatGT")            
cluster_file = "spike_clusters.npy"
template_file = "spike_templates.npy"

cluster_path = Path.joinpath(root,cluster_file)
cluster_templates = Path.joinpath(root,template_file)

clusters = np.load(cluster_path)
templates = np.load(cluster_templates)

#%% Find the templates
id_cluster_to_split = 1
idx_clusterX = np.where(clusters == id_cluster_to_split)
templates_in_merge = np.unique(templates[idx_clusterX])
print(templates_in_merge)

#%% Replace
for tmp in templates_in_merge:
    clusters[templates==tmp] = tmp

np.save(cluster_path,clusters)




