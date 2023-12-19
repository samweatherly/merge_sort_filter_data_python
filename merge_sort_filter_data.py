import pandas as pd
import matplotlib
import seaborn as sns
from matplotlib import pyplot as plt


df_temp = pd.read_csv(r"tempYearly.csv")
df_rain = pd.read_csv(r"rainYearly.csv")


df_temp_f = df_temp.query('Temperature < 40 & Temperature > 0')
df_rain_f = df_rain.query('Rainfall < 6 & Rainfall > 0')


df_merge = pd.merge(df_temp_f, df_rain_f, on="Year", how="inner")
print(df_merge.sort_values(by="Temperature", ascending=False))

sns.set(rc={"figure.figsize": (12,6)})
sns.jointplot("Rainfall", "Temperature", data=df_merge, kind="reg")
# sns.jointplot(data=df_merge, kind="reg")
plt.show()