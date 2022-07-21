import altair as alt
import pandas as pd
from vega_datasets import data

def plot_wells(well_data):
    wells = pd.DataFrame(well_data, columns=['latitude', 'longitude', 'depth', 'gradient'])
    states = alt.topo_feature(data.us_10m.url, feature='states')

    # US states background
    background = alt.Chart(states).mark_geoshape(
        fill='lightgray',
        stroke='white'
    ).properties(
        width=500,
        height=300
    ).project('albersUsa')

    # airport positions on background
    points = alt.Chart(wells).mark_circle().encode(
        longitude='longitude:Q',
        latitude='latitude:Q',
        color=alt.Color('gradient:Q', scale=alt.Scale(scheme='inferno')),
        tooltip=[
            alt.Tooltip('depth:Q', title='Depth (m)', format='d'),
            alt.Tooltip('gradient:Q', title='Gradient (°C/m)', format='0.2f')
        ]
    ).properties(
        title='Well Locations'
    )

    chart = background + points
    
    return chart.to_json()
