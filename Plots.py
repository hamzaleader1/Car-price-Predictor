import streamlit as st,matplotlib.pyplot as plt, seaborn as sns, pandas as pd, numpy as np
def app(df):
	st.set_option('deprecation.showPyplotGlobalUse', False)
	st.header("Visualization")
	st.subheader("Scatterplot")
	selection=st.multiselect("Select the feature on the x-axis",tuple(df.columns))
	for i in selection:
		plt.figure(figsize=(25,10))
		st.subheader(f"This is a scatter plot between {i} and price")
		sns.scatterplot(x=df[i],y=df['price'])
		st.pyplot()

	st.subheader("More plots")
	selection2=st.multiselect("Select a plot that you require",("Histogram","Box Plot","Correlation Heatmap"))
	if "Histogram" in selection2:
		feat_select=st.multiselect("Choose the features for histogram",tuple(df.columns))
		for i in feat_select:
			plt.figure(figsize=(25,10))
			st.subheader(f"This is a histogram for {i}")
			plt.hist(df[i],bins='sturges',edgecolor='red')
			st.pyplot()
	if "Box Plot" in selection2:
		feat_select=st.multiselect("Choose the features for boxplot",tuple(df.columns))
		for i in feat_select:
			plt.figure(figsize=(25,10))
			st.subheader(f"This is a boxplot for {i}")
			sns.boxplot(x=df[i])
			st.pyplot()
	if "Correlation Heatmap" in selection2:
		plt.figure(figsize=(25,10))
		st.subheader("This is a correlation heatmap for the dataframe")
		sns.heatmap(df.corr(),annot=True)
		st.pyplot()
