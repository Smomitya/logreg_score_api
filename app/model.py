from sklearn.datasets import make_moons
from sklearn.linear_model import LogisticRegression
import pickle

X, y = make_moons(n_samples=700, noise=0.1, random_state=42)
logreg = LogisticRegression()
logreg.fit(X, y)
pickle.dump(logreg, open("logreg.pickle", "wb"))