import matplotlib.pyplot as plt

# make a copy of housing to play around
housing = strat_train_set.copy()

# create a scatter plot using longtitude and latitude of the entries
housing.plot(kind="scatter", x="longitude", y="latitude")

# better visualization, using opacity to indicate density
housing.plot(kind="scatter", x="longitude", y="latitude", alpha=0.1)


housing.plot(kind="scatter", x="longitude", y="latitude", alpha=0.4,
    s=housing["population"]/100, label="population", figsize=(10,7),
    c="median_house_value", cmap=plt.get_cmap("jet"), colorbar=True,
)

plt.legend()