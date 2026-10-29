import pandas as pd

df = pd.read_excel("AXIA3_evolucao.xlsx")
print(df)

df["valor"].max()
df["valor"].min()
df["valor"].mean()
df["valor"].std()

df[0:1]

colunas = ["conta", "valor"]
df[23:24][colunas]

linhas = df["conta"] == "lucro"
colunas = ["valor"]






import seaborn as sns
import matplotlib.pyplot as plt
linhas = df["conta"] == "lucro"
colunas = ["trimestre", "valor"]
dados = df[linhas][colunas]
sns.lineplot(dados, x="trimestre", y="valor")
plt.title("Grafico de lucro")