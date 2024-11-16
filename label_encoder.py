from sklearn.preprocessing import LabelEncoder


categories = ['Red', 'Blue', 'Green', 'Blue', 'Red']

label_encoder = LabelEncoder()


encoded_labels = label_encoder.fit_transform(categories)

print("Encoded Labels:", encoded_labels)
