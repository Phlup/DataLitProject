import numpy as np
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt
from sklearn.covariance import EmpiricalCovariance, MinCovDet
from tueplots import bundles


plt.rcParams.update(bundles.neurips2021())
X = []
import pickle
with open("persons_filtered_keywords.pickle","rb") as f:
    persons=pickle.load(f)
for person in persons:
    X.append(person["word_count"])
X=np.array(X)

X_embedded = TSNE(n_components=2, learning_rate='auto',init='pca',metric='mahalanobis').fit_transform(X)
print(X_embedded)

colors = {"Q1387991":"yellow",
           "Q1023134":"black",
            "Q1007353":"green",
            "Q42575708":"blue",
            "Q1826856":"purple",
           "Q2207512":"red"}



parties = {"FDP": "Q1387991",
           "CDU": "Q1023134",
           "Grüne": "Q1007353",
           "AFD": "Q42575708",
           "Linke": "Q1826856",
           "SPD": "Q2207512"}
for i in range(len(X_embedded)):
    plt.plot(X_embedded[i][0],X_embedded[i][1],'ro',c=colors[persons[i]["factionID"]])

plt.title("T-SNE of the high frequency speakers")
plt.xlabel("TSNE-1")
plt.ylabel("TSNE-2")
plt.savefig("t-sne.png")
plt.clf()
exit(0)
n_outliers=10
robust_cov = MinCovDet().fit(X)
# fit a MLE estimator to data
emp_cov = EmpiricalCovariance().fit(X)
plt.scatter(X[:, 0], X[:, 1], color="black", label="inliers")
plt.scatter(
    X[:, 0][-n_outliers:], X[:, 1][-n_outliers:], color="red", label="outliers"
)
plt.title("T-SNE of the high frequency speakers")
plt.xlabel("TSNE-1")
plt.ylabel("TSNE-2")

plt.savefig("maha.png")
