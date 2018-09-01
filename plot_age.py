import matplotlib.pyplot as plt
import seaborn as sns

from revenue import Revenue

revenue = Revenue().clean()

are_old = revenue["Age"] > 60
plt.hist(revenue[are_old]["Age"], bins=50)
plt.show()
