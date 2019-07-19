import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import dbm
import plotly.graph_objs as go
import re


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
            id='product-dropdown',
            options=dict_products,
            multi=True,
            value = ["Ben & Jerry's Wake and No Bake Cookie Dough Core Ice Cream","Brewdog Punk IPA"]
        ),
        dcc.Graph(
            id='product-like-bar'
        )
    ], style={'width': '40%', 'display': 'inline-block'}),
    html.Div([
        html.H2('All product info'),
        html.Table(id='my-table'),
        html.P(''),
    ], style={'width': '55%', 'float': 'right', 'display': 'inline-block'}),
    html.Div([
        html.H2('price graph'),
        dcc.Graph(id='product-trend-graph'),
        html.P('')
    ], style={'width': '100%',  'display': 'inline-block'})

])



@app.callback(Output('product-like-bar', 'figure'), [Input('product-dropdown', 'value')])
def update_graph(selected_dropdown_value):
    product_df_filter = product_df[(product_df['product_title'].isin(selected_dropdown_value))]

    # Take the one with max datetime and remove duplicates for this bar chart
    product_df_filter = product_df_filter.sort_values('datetime', ascending=False).drop_duplicates(['index'])

    #Rating count check
    def format_rating(rating):
        return re.sub('\((\d+)\)', r'\1', rating)

    product_df_filter['rating_count'] = product_df_filter['rating_count'].apply(format_rating)

    figure = {
        'data': [go.Bar(
            y=product_df_filter.product_title,
            x=product_df_filter.rating_count,
            orientation='h'
        )],
        'layout':go.Layout(
            title= 'Product Rating Trends',
            yaxis = dict(
                # autorange=True,
                automargin=True
            )
        )
    }
    return figure


# For the top topics graph
@app.callback(Output('product-trend-graph', 'figure'), [Input('product-dropdown', 'value')])
def update_graph(selected_dropdown_value):
    product_df_filter = product_df[(product_df['product_title'].isin(selected_dropdown_value))]

    data = timeline_top_product_filtered(product_df_filter,selected_dropdown_value)
    # Edit the layout
    layout = dict(title='Product Price Trends',
                  xaxis=dict(title='datetime'),
                  yaxis=dict(title='Price'),
                  )
    figure = dict(data=data,layout=layout)
    return figure

def timeline_top_product_filtered(top_product_filtered_df, selected_dropdown_value):
    # Make a timeline
    trace_list = []
    for value in selected_dropdown_value:
        top_product_value_df = top_product_filtered_df[top_product_filtered_df['product_title']==value]
        trace = go.Scatter(
            y=top_product_value_df.product_price,
            x=top_product_value_df.datetime,
            name = value
        )
        trace_list.append(trace)
    return trace_list


# for the table
@app.callback(Output('my-table', 'children'), [Input('product-dropdown', 'value')])
def generate_table(selected_dropdown_value, max_rows=20):
    product_df_filter = product_df[(product_df['product_title'].isin(selected_dropdown_value))]
    product_df_filter = product_df_filter.sort_values(['index','datetime'], ascending=True)

    return [html.Tr([html.Th(col) for col in product_df_filter  .columns])] + [html.Tr([
        html.Td(product_df_filter.iloc[i][col]) for col in product_df_filter  .columns
    ]) for i in range(min(len(product_df_filter  ), max_rows))]

if __name__ == '__main__':
    app.run_server(debug=True)



# For the product price graph individual
# @app.callback(Output('my-graph', 'figure'), [Input('my-dropdown', 'value')])
# def update_graph(selected_dropdown_value):
#     product_df_filter = product_df[(product_df['product_title'].isin(selected_dropdown_value))]
#
#     return {
#         'data': [{
#             'x': product_df_filter.datetime,
#             'y': product_df_filter.product_price
#         }]
#     }
