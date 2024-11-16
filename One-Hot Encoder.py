from sklearn.preprocessing import OneHotEncoder
import numpy as np

categories = np.array(['Red', 'Blue', 'Green', 'Blue', 'Red']).reshape(-1, 1)

one_hot_encoder = OneHotEncoder(sparse_output=False)

encoded_one_hot = one_hot_encoder.fit_transform(categories)

print("One-Hot Encoded Data:\n", encoded_one_hot)
