# requires load_data.py to run first which exposes housing variable
# following only works in Jupyter notebook
%matplotlib inline 
import matplotlib.pyplot as plt
housing.hist(bigs=50, figsize=(20,15))
plt.show()