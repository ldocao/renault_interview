#PURPOSE: answer question 2

from revenue import Revenue
import matplotlib.pyplot as plt
import seaborn as sns



revenue = Revenue().clean()
median_all = revenue.groupby(["Sex", "is_weekend"]).median()[["Age", "Incomes"]]

is_clio = revenue["Model"] == "Clio"
is_yellow = revenue["Color"] == "yellow"
yellow_clio = revenue[is_clio & is_yellow]
yellow_clio = yellow_clio.drop(["Model", "Color", "Price"], axis=1)
median_yellow_clio = yellow_clio.groupby(["Sex", "is_weekend"]).median()




comparison = median_all.merge(median_yellow_clio,
                              left_index=True,
                              right_index=True,
                              suffixes=["_all", "_yc"])
comparison["age_diff"] = comparison["Age_yc"] - comparison["Age_all"]
comparison["incomes_diff"] = comparison["Incomes_yc"] - comparison["Incomes_all"]
comparison = comparison.drop(["Age_all", "Incomes_all", "Age_yc", "Incomes_yc"], axis=1)

plt.figure()
sns.pairplot(yellow_clio, hue="Sex")
plt.tight_layout()
plt.savefig("yellow_clio_pairplot.png")
