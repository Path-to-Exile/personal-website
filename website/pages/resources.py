import dash
from dash import html, dcc
import dash_bootstrap_components as dbc

dash.register_page(__name__)

layout = html.Div(
    [
        html.H2(children='Resources', style = {'margin-bottom': '20px'}),
        dbc.Accordion(
        [
            dbc.AccordionItem(
                [
                    html.P("""
                        In a world of standardized LinkedIn profiles and automatated CV's it is nice to do something.
                    """),
                ],
                title="Set up your own website",
            ),
            dbc.AccordionItem(
                [
                    html.P("This is the content of the second section"),
                    dbc.Button("Don't click me!", color="danger"),
                ],
                title="Item 2",
            ),
            dbc.AccordionItem(
                "This is the content of the third section",
                title="Item 3",
            ),
             dbc.AccordionItem(
                [
                    html.P("This is the content of the fourth section"),
                    dbc.Button("Click here"),
                ],
                title="Item 4",
            ),
            dbc.AccordionItem(
                [
                    html.P("This is the content of the fifth section"),
                    dbc.Button("Don't click me!", color="danger"),
                ],
                title="Item 5",
            ),
            dbc.AccordionItem(
                "This is the content of the sixth section",
                title="Item 6",
            ),
        ], start_collapsed=True, style = {'border-radius': '7px', 'border': '3px solid', 'margin-bottom': '100px'}
    ),
    ], className='fade-in',
)


