from dash import Dash, html, dcc
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

ddata = pd.read_csv("base.csv", sep="|")

site_lat = ddata["latitude"]
site_lon = ddata["longetude"]

fig = px.scatter_mapbox(
    ddata,
    lat=site_lat,
    lon=site_lon,
    hover_data=["Bairro", "Lata"],
    color_discrete_sequence=["fuchsia"],
    zoom=15,
    height=600,

)
fig.update_layout(mapbox_style="open-street-map")
fig.update_layout(margin={"r": 65, "t": 25, "l": 65, "b": 25})
fig.update_traces(marker_size=15)

app = Dash(__name__)

app.layout = html.Div(
    children=[
        html.Div(children="SmartBucket",
                 style={
                     "font-family": "sans-serif",
                     "display": "flex",
                     "justify-content": "center",
                     "align-items": "center",
                     "background-color": "#000",
                     "height": "60px",
                     "color": "#fff",
                     "font-size": "28px"
                 }),

        dcc.Graph(
            id="Nivel x Hora",
            figure=px.bar(ddata, x=ddata["Lata"], y=ddata["Nivel"])

        ),

        dcc.Graph(figure=fig)
    ]
)

if __name__ == "__main__":
    app.run_server(debug=True)
