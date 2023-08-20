from flask import Flask, request, jsonify
import pandas as pd

app = Flask(__name__)

df = pd.read_csv('/userapi/products.csv')

@app.route('/userapi', methods=['GET'])
def search_product():
    user_location = request.args.get('location')
    user_product = request.args.get('product')

    filtered_df = df[(df['Region'] == user_location) & (df['Product'] == user_product)]

    if filtered_df.empty:
        other_locations = df[df['Product'] == user_product]['Region'].unique().tolist()
        response = {
            'message': f"The product '{user_product}' is not available in {user_location}. It is available in the following locations:",
            'available_locations': other_locations
        }
    else:
        available_locations = filtered_df['Region'].unique().tolist()
        response = {
            'message': f"The product '{user_product}' is available in {user_location} at the following locations:",
            'available_locations': available_locations
        }

    return jsonify(response)

if __name__ == '_main_':
    app.run(debug=True, host='0.0.0.0')