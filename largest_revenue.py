#PURPOSE: answer question 1

from revenue import Revenue


revenue = Revenue().clean()

UNIT = 1e6 #euros
print(revenue.groupby("Model")["Price"].sum().sort_values(ascending=False)/UNIT)
