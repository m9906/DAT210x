import pandas as pd

# TODO: Load up the 'tutorial.csv' dataset
#
# .. your code here ..
csv_dataframe = pd.read_html('Module2/Datasets/tutorial.csv',sep=',')

# TODO: Print the results of the .describe() method
#
# .. your code here ..
table_dataframe.describe()

# TODO: Figure out which indexing method you need to
# use in order to index your dataframe with: [2:4,'col3']
# And print the results
#
# .. your code here ..
table_dataframe.loc[2:4,'col3']
