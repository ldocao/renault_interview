import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from revenue import Revenue


revenue = Revenue().clean()
revenue.info() 
revenue.describe()
for c in revenue.columns:
    if revenue[c].dtype == np.dtype("O"):
        print(c, revenue[c].unique())

plt.figure()
sns.pairplot(revenue)
plt.tight_layout()
plt.savefig("pairplot.png")
