from category_encoders import HashingEncoder
import pandas as pd

categories = pd.Series(['Red', 'Blue', 'Green', 'Blue', 'Red'])

hashing_encoder = HashingEncoder(n_components=2)  

encoded_hashing = hashing_encoder.fit_transform(categories)

print("Hashing Encoded Data:\n", encoded_hashing)
