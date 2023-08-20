import pandas as pd
import random

# Define the products and regions
products = ['Gold Irish seas moss', 'Creed green Irish tweed men perfume spray', 'Stash black tea', 'Torani flavouring syrup', 'Kerry gold Irish butter']
regions = ['Dublin', 'Cork', 'Galway', 'Limerick', 'Waterford', 'Wexford', 'Kilkenny', 'Sligo', 'Donegal', 'Kerry', 'Letterkenny', 'Wexford']

# Create an empty DataFrame
df = pd.DataFrame(columns=['Product', 'Region', 'Price', 'Description'])

# Generate data for each product and region up to 1000 rows
for _ in range(1000)
    product = random.choice(products)
    region = random.choice(regions)
    price = round(random.uniform(10, 1000), 2)
    description = fDescription of {product} in {region}
    df = df.append({'Product' product, 'Region' region, 'Price' price, 'Description' description}, ignore_index=True)

# Add some products in all regions
for product in products[3]
    for region in regions
        price = round(random.uniform(10, 1000), 2)
        description = fDescription of {product} in {region}
        df = df.append({'Product' product, 'Region' region, 'Price' price, 'Description' description}, ignore_index=True)

# Add some products missing in certain regions
for product in products[3]
    for region in regions
        if random.random()  0.7  # Set probability of product missing in a region
            price = round(random.uniform(10, 1000), 2)
            description = fDescription of {product} in {region}
            df = df.append({'Product' product, 'Region' region, 'Price' price, 'Description' description}, ignore_index=True)

# Print the DataFrame
print(df)
df.to_csv('products.csv', index=False)
