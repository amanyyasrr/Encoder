from category_encoders import TargetEncoder
import pandas as pd

data = pd.DataFrame({
    'Category': ['Red', 'Blue', 'Green', 'Blue', 'Red'],
    'Target': [1, 2, 3, 2, 1]
})


target_encoder = TargetEncoder()


encoded_target = target_encoder.fit_transform(data['Category'], data['Target'])

print("Target Encoded Data:\n", encoded_target)
