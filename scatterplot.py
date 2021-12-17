import pandas as pd
import plotly.express as px

df = pd.read_csv("Copy+of+data+-+data.csv")
fig = px.scatter(df, x="Date", y="No of Cases",
	          size="Percentage",color="Country",
                   size_max=60)
fig.show()
