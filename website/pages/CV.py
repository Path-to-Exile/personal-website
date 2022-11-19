import dash
from dash import html, dcc

dash.register_page(
    __name__,
    path='/cv',
    title='CV',
    name='CV'
    )

layout = html.Div(children=[
    html.H2(children='This is our CV page'),

    html.Div(children='''
        This is our cv page content.
    '''),

], className='fade-in')