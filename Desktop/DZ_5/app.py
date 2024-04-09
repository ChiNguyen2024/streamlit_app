import streamlit as st
import pandas as pd
from streamlit_extras.stateful_button import button

st.title('Cardiovascular Diseases incidence')

df= pd.read_csv('./data/CVD_cleaned.csv')
df.drop(df.columns[[2,4,5,6,7,8,10,13,14,15,16,17,18]], axis=1, inplace=True)
st.dataframe(df)

is_clicked=button('Click to filter', key=1)
if is_clicked:
    gender= st.sidebar.radio(
        "Choose gender",
        options=df["Sex"].unique()
    )
    weight=st.sidebar.slider(
        label="Choose minimum weight",
        min_value=float(df["Weight_(kg)"].loc[df["Weight_(kg)"].idxmin()]),
        max_value=float(df["Weight_(kg)"].loc[df["Weight_(kg)"].idxmax()]),
        value= None,
        step=0.5
    )
    height=st.sidebar.slider(
        label="Choose minimum height",
        min_value=int(df["Height_(cm)"].loc[df["Height_(cm)"].idxmin()]),
        max_value=int(df["Height_(cm)"].loc[df["Height_(cm)"].idxmax()]),
        value= None,
    )
    heart=st.sidebar.selectbox(
        "Choose if you have a heart disease",
        options=df["Heart_Disease"].unique()
    )
    health= st.sidebar.multiselect(
        "Choose health condition",
        options=df["General_Health"].unique()
    )    
    checkup= st.sidebar.multiselect(
        "Choose frequency of health checkups",
        options=df["Checkup"].unique()
    )
    filtered_df = df[
        (df['Sex'] == gender) &
        (df['Weight_(kg)'] >= weight) &
        (df['Height_(cm)'] >= height) &
        (df['Heart_Disease'] == heart)
    ] 
    sec_filtered_df=filtered_df[(df['General_Health'].isin(health)) & (df['Checkup'].isin(checkup))]
    st.write(sec_filtered_df)





