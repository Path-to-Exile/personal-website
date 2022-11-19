from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import dash_bootstrap_components as dbc
import dash
from dash_bootstrap_templates import ThemeSwitchAIO


app = Dash(__name__, external_stylesheets=[dbc.themes.FLATLY], use_pages=True)

theme_switch = ThemeSwitchAIO(aio_id="theme", themes=[dbc.themes.FLATLY, dbc.themes.DARKLY])
#graph = html.Div(dcc.Graph(id="theme-switch-graph"), className="m-4")


app.layout = html.Div([
    dbc.Row([
        dbc.Col([
            dbc.Container([theme_switch], className="m-4 dbc"),
        ], width={"size": 5},),
        dbc.Col([
            html.Div([
                dbc.Button(" Add me", className="fab fa-linkedin fa-3x me-md-4", size = 'sm', color="primary", external_link=True, href="https://www.linkedin.com/in/bill-nye-science-guy-9488063b",),
                #dbc.Button(" Add me", className="fab fa-linkedin fa-3x me-md-4", size = 'sm', color="secondary", external_link=True, href="https://www.linkedin.com/in/bill-nye-science-guy-9488063b",),
                dcc.Link('hello@antonsuhr.me', title ='email_me', href='mailto:hello@antonsuhr.me',
                        target ='_blank', style = {'text-decoration': 'none'}, className='link-primary'),
            ],className="m-4 dbc",
            ),
        ], width={"size": 3,'offset': 4},),
    ]),
    dbc.Row([
        dbc.Col([
            html.Div(children=[
                html.H1("Hi, I'm Anton", className = 'inline-flex lg:hidden transition-color animation-reveal-text animation-reveal-text-active animation-delay-400'),
                html.Div([
                    html.Div(
                        dcc.Link(
                            f"{page['name']}", href=page["relative_path"], className = 'inline-flex lg:hidden transition-color animation-reveal-text animation-reveal-text-active animation-delay-400',
                            style = {'text-decoration': 'none'},
                        )
                    )
                    for page in dash.page_registry.values()
                ]),
            ],  style={'font-size': '40px', 'margin-right': '0px','margin-top': '100px', 'margin-left': '200px'}
            ),
        ], width={"size": 5,},),
	    dbc.Col([
            html.Div(
                dash.page_container, 
                style={'margin-left': '10px','margin-top': '109px', 'margin-right': '200px'},
            ),
        ], width={"size": 7,}),
    ]),
])

if __name__ == "__main__":
    app.run_server(debug=True, port = 5000)