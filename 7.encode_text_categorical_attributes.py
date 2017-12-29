from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder

encoder = LabelEncoder()
housing_cat = housing["ocean_proximity"]
housing_cat_encoded = encoder.fit_transform(housing_cat)
# <1h OCEAN converted to 0
# INLAND converted to 1, etc


# an improvement. This way the model will avoid thinking that 0 is close to 1
# we have one binary attribute instead 1=hot 0=cold
encoderHot = OneHotEncoder()
housing_cat_1hot = encoderHot.fit_transform(housing_cat_encoded.reshape(-1,1)) # housing_cat_encoded from 1D to 2D array
