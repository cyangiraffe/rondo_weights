import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

weights = pd.read_csv("rondo_weights.csv")
weights['Date'] = pd.to_datetime(weights['Date'])
fig = px.line(weights, x="Date", y="Weight", color="Name", hover_name="Annotations", markers=True)
fig.write_html("rondo_weights.html")
fig.show()
