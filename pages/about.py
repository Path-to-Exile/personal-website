import dash
from dash import html, dcc

dash.register_page(__name__, path='/')

layout = html.Div(children=[
    html.H2(children='About'),

    html.P(children=["""
        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis auctor massa et nibh pharetra venenatis. Curabitur ullamcorper tellus dapibus 
        lacus mattis convallis. Proin luctus dolor tellus, at viverra enim commodo consectetur. Ut vel augue tortor. Etiam facilisis erat a luctus laoreet. 
        Pellentesque varius, elit nec molestie finibus, erat erat tincidunt orci, quis ultrices arcu enim vel neque. Duis et imperdiet sem, nec lobortis nisl. 
        Ut vitae dignissim neque. Nullam molestie rhoncus ornare. Sed mollis quis dolor nec sollicitudin. Integer vitae suscipit mauris, id porta nulla. Sed eget luctus leo. 
        Nulla at bibendum dolor, at vehicula velit. Donec eget odio feugiat, dapibus tellus in, volutpat lacus.""",
        html.Br(),
        """Aenean lacinia tortor et rutrum auctor. Nulla facilisi. Morbi gravida, mauris eget gravida consequat, tortor sem ornare eros, id gravida dui eros vel nisl. 
        Maecenas eget elementum ipsum. Donec bibendum lobortis odio eu ullamcorper. Nulla molestie eget mi eget bibendum. 
        Proin commodo, tortor vitae cursus fringilla, ex massa interdum nunc, ac tincidunt urna orci id dui. Aenean vitae erat pharetra, efficitur mauris nec, volutpat erat."""
        ],
        ),

], style={'margin-bottom': '100px'},
)