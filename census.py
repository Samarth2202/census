# Open Sublime text editor, create a new Python file, copy the following code in it and save it as 'census_app.py'.

# Import modules
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

@st.cache()
def load_data():
	# Load the Adult Income dataset into DataFrame.

	df = pd.read_csv('https://student-datasets-bucket.s3.ap-south-1.amazonaws.com/whitehat-ds-datasets/adult.csv', header=None)
	df.head()

	# Rename the column names in the DataFrame using the list given above. 

	# Create the list
	column_name =['age', 'workclass', 'fnlwgt', 'education', 'education-years', 'marital-status', 'occupation', 'relationship', 'race','gender','capital-gain', 'capital-loss', 'hours-per-week', 'native-country', 'income']

	# Rename the columns using 'rename()'
	for i in range(df.shape[1]):
	  df.rename(columns={i:column_name[i]},inplace=True)

	# Print the first five rows of the DataFrame
	df.head()

	# Replace the invalid values ' ?' with 'np.nan'.

	df['native-country'] = df['native-country'].replace(' ?',np.nan)
	df['workclass'] = df['workclass'].replace(' ?',np.nan)
	df['occupation'] = df['occupation'].replace(' ?',np.nan)

	# Delete the rows with invalid values and the column not required 

	# Delete the rows with the 'dropna()' function
	df.dropna(inplace=True)

	# Delete the column with the 'drop()' function
	df.drop(columns='fnlwgt',axis=1,inplace=True)

	return df

census_df = load_data()

st.set_option('deprecation.showPyplotGlobalUse',False)

# Write the code to design the web app

# Add title on the main page and in the sidebar.
st.title('Census Data Visualisation Web App')
st.sidebar.title('Menu')
# Using the 'if' statement, display raw data on the click of the checkbox.
if st.sidebar.checkbox('display raw data'):
  st.table(census_df)
# Add a multiselect widget to allow the user to select multiple visualisations.
# Add a subheader in the sidebar with the label "Visualisation Selector"
st.sidebar.subheader('Visualisation Selector')

# Add a multiselect in the sidebar with label 'Select the Charts/Plots:'
# Store the current value of this widget in a variable 'plot_list'.
plot_lists = st.sidebar.multiselect('Select the Charts/Plots : ',('Histogram', 'Box Plot', 'Count Plot'))

# Display pie plot using matplotlib module and 'st.pyplot()'
if plot_lists == 'Pie Plot':
  st.title('Pie chart')
  pie_data = census_df['income','gender']
  for i in pie_data.columns:
    plt.figure(figsize=(5,5))
    plt.title('Distributions of record for different ',i,' groups')
    plt.pie(pie_data, labels=pie_data.index,autopct='%1.2f%%',startangle = 30, explode=np.linspace(.06,.16,6) 
    st.pyplot()

# Display box plot using matplotlib module and 'st.pyplot()'
if plot_lists=='Box Plot':
  st.title('Box Plot')
  for i in ['income', 'gender']:
    plt.figure(figsize=(12,2))
    plt.title('Distribution of hours-per-week for different ',i,' groups.')
    sns.boxplot(census_df['hours-per-week'], hue=i)
    st.pyplot()

# Display count plot using seaborn module and 'st.pyplot()' 
if plot_lists=='Count Plot':
  st.title('Count Plot')
  plt.figure(figsize=(12,6))
  plt.title('Count plot for distribution of records for unique workclass group')
  sns.count_plot(x='workclass',data=census_df)
  st.pyplot()