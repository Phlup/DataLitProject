# DataLitProject: Reliability between speeches and policy statements in the german Bundestag
This project uses the data from https://openparliament.tv/ to search for correlations between parties and keywords.

#### Execution order:
- downloader_party_level.py
- people_speaches_downloader.py
- party_level_bar_plots.py
- people_graph_generator.py
- people_tsne.py
- chisquared.py

#### Dependencies:
- matplotlib
- scipy
- numpy
- urllib
- tueplots
- sklearn
