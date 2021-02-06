import streamlit as st
import pickle
import pandas as pd
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier

st.sidebar.title('Estimate Your Employee Leaves')

html_temp = """
<div style="background-color:tomato;padding:10px">
<h2 style="color:white;text-align:center;">Employee Churn Prediction</h2>
</div><br><br>"""

st.markdown(html_temp,unsafe_allow_html=True)

selection=st.selectbox("Select Your Model", ["GradientBoosting", "KNeighbour", "Random Forest"])

if selection =="GradientBoosting":
    st.write("You selected", selection, "model")
    model= pickle.load(open('gb', 'rb'))
elif selection =="KNeighbour":
    st.write("You selected", selection, "model")
    model= pickle.load(open('Knn', 'rb'))
else:
    st.write("You selected", selection, "model")
    model= pickle.load(open('R_F_C', 'rb'))
    
satisfaction=st.sidebar.slider("How well you satisfied with the Company?",0.1,1.0, step=0.1)
salary=st.sidebar.selectbox("What is your salary level (low:1, medium:2, high:3)?", (1, 2, 3))
time_spend=st.sidebar.slider("How long have you spend time in this company?", 1,10, step=1)
work_accident = st.sidebar.selectbox("Have you ever experienced any accident(no:0, yes:1)?", (0,1))
                            

#df=pickle.load(open("df", "rb"))    

my_dict = {
    "satisfaction": satisfaction,
    "salary": salary, 
    "time_spend": time_spend,
    "work_accident": work_accident
}
                            
columns = ["satisfaction", "salary", "time_spend", "work_accident"]                           
df = pd.DataFrame.from_dict([my_dict])

X = df

prediction = model.predict(X)

st.header("Profile of your employee is below")
st.table(df)
st.subheader("Press predict if configuration is okay")

if st.button('Predict'):
    if prediction ==1:
        st.write("your employee would probably will leave")
    else: st.write("your employee would probably stay")

                            
                            