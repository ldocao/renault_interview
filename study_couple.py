import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from revenue import Revenue

revenue = Revenue().clean()
is_average = revenue["Incomes"] < 50e3
revenue = revenue[is_average]
is_couple = revenue["Sex"] == "Couple"
couple_revenue = revenue[is_couple]
non_couple_revenue = revenue[~is_couple]
print(couple_revenue.describe())
print(non_couple_revenue.describe())


PLOT_OPTIONS = {"bins": np.arange(30e3, 50e3, 2e3),
                "alpha": 0.3,
                "normed": 1} #area should sum to 1
plt.figure()
plt.hist(non_couple_revenue["Incomes"], color="b", **PLOT_OPTIONS)
plt.hist(couple_revenue["Incomes"], color="r", **PLOT_OPTIONS)
plt.xlabel("Incomes")
plt.tight_layout()
plt.savefig("study_couple_histogram_incomes.png")

plt.figure()
sns.jointplot(x="Incomes", y="Age", data=couple_revenue, kind="kde");
plt.savefig("study_couple_jointplot.png")



PLOT_OPTIONS = {"bins": 20,
                "alpha": 0.3,
                "normed": 1} #area should sum to 1

plt.figure()
plt.hist(non_couple_revenue["Age"], color="b", **PLOT_OPTIONS)
plt.hist(couple_revenue["Age"], color="r", **PLOT_OPTIONS)
plt.xlabel("Age")
plt.tight_layout()
plt.savefig("study_couple_histogram_age.png")
