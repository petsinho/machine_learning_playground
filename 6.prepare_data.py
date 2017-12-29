import matplotlib.pyplot as plt

housing = strat_train_set.drop("median_house_value", axis=1)
housing_labels = strat_train_set["median_house_value"].copy()

# for columns with missing values we can either
# 1. drop the entries that do not have values or
housing.dropna(subset=["total_bedrooms"])
# 2. drop the entire attribute or 
housing.drop("total_bedrooms", axis=1)
# 3. replace missing values with the median
median = housing["total_bedrooms"].median()
housing["total_bedrooms"].fillna(median, inplace=True)

# option 3 can also be accomplished using scikit-learn Imputer
# from sklearn.preprocessing import Imputer
# imputer = Imputer(strategy="median")
# housing_num = housing.drop("ocean_proximity", axis=1) #drop non-numerical attribute
# imputer.fit(housing_num) 
# X = imputer.transform(housing_num) # replace any missing values with their medians
# housing_tr = pd.DataFrame(X, columns=housing_num.columns)
