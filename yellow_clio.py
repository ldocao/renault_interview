#PURPOSE: answer question 2

from revenue import Revenue
import matplotlib.pyplot as plt
import seaborn as sns



revenue = Revenue().clean()
median_all = revenue.groupby(["Sex", "is_weekend"]).median()

is_clio = revenue["Model"] == "Clio"
is_yellow = revenue["Color"] == "yellow"
yellow_clio = revenue[is_clio & is_yellow]
yellow_clio = yellow_clio.drop(["Model", "Color", "Price"], axis=1)



plt.figure()
sns.pairplot(yellow_clio, hue="Sex")
plt.tight_layout()
plt.savefig("yellow_clio_pairplot.png")
