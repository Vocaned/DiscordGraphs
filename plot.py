import plotly.express as px
import json

with open(f'data/{input("Channel ID: ")}.json', 'r', encoding='utf-8') as f:
    df = json.load(f)

fig = px.line(
    df['data'],
    x='date', y='count',
    labels={'date': 'Date', 'count': 'Messages per day'},
    title=f'Messages sent daily in {df["metadata"]["guild"]} {df["metadata"]["channel"]}',
    template='plotly_dark', color_discrete_sequence=px.colors.qualitative.Bold
)
fig.update_layout(
    font_family='Comic Sans MS',
)
fig.update_xaxes(
    dtick=7*24*60*60*1000
)
fig.show()
