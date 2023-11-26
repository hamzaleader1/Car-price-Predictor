import streamlit as st,matplotlib.pyplot as plt, seaborn as sns, pandas as pd, numpy as np
from sklearn.model_selection import train_test_split as tts
from sklearn.linear_model import LinearRegression as LR
from sklearn.metrics import r2_score as r2, mean_absolute_error as mae, mean_squared_error as mse, mean_squared_log_error as msle

def prediction(df,carwidth, enginesize, horsepower, drivewheel_fwd, car_company_buick):
	X=df.drop(columns='price')
	y=df['price']
	X_train,X_test,y_train,y_test=tts(X,y,random_state=42,test_size=0.3)

	model=LR().fit(X_train,y_train)
	score=model.score(X_train,y_train)
	y_test_pred=model.predict(X_test)
	r_2=r2(y_test,y_test_pred)
	m_ae=mae(y_test,y_test_pred)
	m_se=mse(y_test,y_test_pred)
	m_sle=msle(y_test,y_test_pred)

	pred_price=model.predict([[carwidth, enginesize, horsepower, drivewheel_fwd, car_company_buick]])

	return r_2,m_ae,m_se,m_sle,pred_price

def app(df):
	st.markdown("<p style='color:yellow;font-size:30px'>This app uses <b>Linear Regression</b> to predict the price of the car based on your inputs</p>", unsafe_allow_html = True)
	carwidth=st.slider("Enter the value for carwidth",float(df['carwidth'].min()),float(df['carwidth'].max()))
	enginesize=st.slider("Enter the value for enginesize",float(df['enginesize'].min()),float(df['enginesize'].max()))
	horsepower=st.slider("Enter the value for horsepower",float(df['horsepower'].min()),float(df['horsepower'].max()))
	drivewheel_fwd=st.radio("Is it a fwd or not",("Yes","No"))
	if drivewheel_fwd=="Yes":
		drivewheel_fwd=1
	else:
		drivewheel_fwd=0

	car_company_buick=st.radio("Is it manufactured by buick or not",("Yes","No"))
	if car_company_buick=="Yes":
		car_company_buick=1
	else:
		car_company_buick=0

	if st.button("Predict"):
		r_2,m_ae,m_se,m_sle,pred_price=prediction(df,carwidth, enginesize, horsepower, drivewheel_fwd, car_company_buick)
		st.subheader("Prediction results")
		st.info(f"Predicted price of the car is {round(pred_price[0],2)}")
		st.info(f"r2 score is {round(r_2,2)}")
		st.info(f"mean_absolute_error is {round(m_ae,2)}")
		st.info(f"mean_squared_error is {round(m_se,2)}")
		st.info(f"mean_squared_log_error is {round(m_sle,2)}")

