import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import dbm

# Set up the app
app = dash.Dash(__name__)
server = app.server

global product_df
global dict_products



def create_dict_list_of_product():
    dictlist = []
    unique_list = product_df.product_title.unique()
    for product_title in unique_list:
        dictlist.append({'value': product_title, 'label': product_title})
    return dictlist

def dict_product_list(dict_list):
    product_list = []
    for dict in dict_list:
        product_list.append(dict.get('value'))
    return product_list

product_df = dbm.read()
dict_products = create_dict_list_of_product()

app.layout = html.Div([
    html.Div([
        html.H1('Price Optimization Dashboard'),
        html.H2('Choose a product name'),
        dcc.Dropdown(
            id='my-dropdown',
            options=dict_products,
            multi=True,
            # value=dict_product_list(dict_products)
        ),
        html.H2('price graph'),
        dcc.Graph(id='my-graph'),
        html.P('')
    ], style={'width': '40%', 'display': 'inline-block'}),
    html.Div([
        html.H2('All product info'),
        html.Table(id='my-table'),
        html.P(''),
    ], style={'width': '55%', 'float': 'right', 'display': 'inline-block'})
])


# For the product price graph
@app.callback(Output('my-graph', 'figure'), [Input('my-dropdown', 'value')])
def update_graph(selected_dropdown_value):
    product_df_filter = product_df[(product_df['product_title'].isin(selected_dropdown_value))]

    return {
        'data': [{
            'x': product_df_filter.datetime,
            'y': product_df_filter.product_price
        }]
    }


# for the table
@app.callback(Output('my-table', 'children'), [Input('my-dropdown', 'value')])
def generate_table(selected_dropdown_value, max_rows=20):
    product_df_filter = product_df[(product_df['product_title'].isin(selected_dropdown_value))]

    return [html.Tr([html.Th(col) for col in product_df_filter  .columns])] + [html.Tr([
        html.Td(product_df_filter.iloc[i][col]) for col in product_df_filter  .columns
    ]) for i in range(min(len(product_df_filter  ), max_rows))]

if __name__ == '__main__':
    app.run_server(debug=True)