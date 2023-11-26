import streamlit as st
def app(df):
	st.header("This page shows the raw data used for prediction")
	with st.beta_expander("View data set"):
		st.write(df)
	st.subheader("Column description")
	if st.checkbox("Summary"):
		st.table(df.describe())
	col_1,col_2,col_3=st.beta_columns(3)
	with col_1:
		if st.checkbox("Show column names"):
			st.table(df.columns)
	with col_2:
		if st.checkbox("View data dimensions"):
			st.write("rows",df.shape[0])
			st.write("columns",df.shape[1])
	with col_3:
		if st.checkbox("View column data"):
			selection=st.selectbox("Select a column",tuple(df.columns))
			st.write(df[selection])
