from sklearn.preprocessing import OrdinalEncoder

categories = [['Low'], ['Medium'], ['High'], ['Medium'], ['Low']]

ordinal_encoder = OrdinalEncoder()


encoded_ordinal = ordinal_encoder.fit_transform(categories)

print("Ordinal Encoded Data:", encoded_ordinal.flatten())
