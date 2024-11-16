from category_encoders import BinaryEncoder
import pandas as pd


categories = pd.Series(['Red', 'Blue', 'Green', 'Blue', 'Red'])

binary_encoder = BinaryEncoder()

encoded_binary = binary_encoder.fit_transform(categories)

print("Binary Encoded Data:\n", encoded_binary)
