import pandas as pd 
import math

pizzas = pd.read_csv("C:\\Users\\27hap\\Documents\\techinar\\data\\pizzas.csv")

pizzas["Area"] = (pizzas["Size"] / 2 ** 2 * math.pi)
pizzas["Price_per_SqInch"] = (pizzas["Price"] / pizzas["Area"])
df = pd.DataFrame(pizzas)
pizza_df = df.sort_values(by=['Price_per_SqInch'], ascending=True)
print(pizza_df)

