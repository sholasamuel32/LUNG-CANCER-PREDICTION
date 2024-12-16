import pandas as pd
import streamlit as st
import pickle

filename = "Log Pred for Lung Cancer.sav"
model = pickle.load(open(filename, 'rb')) 


st.title ('Lung Cancer Prediction app')
st.subheader('This app takes in certain variable to enable prediction')
st.subheader('Developed by: ImmsyBlaq')

def user_imput():
    Age = st.slider('How old are you?', 0, 150)
    Smoking = st.selectbox('Do you smoke(puff)?, HINT 2 for yes and 1 for no', options = [2,1], index = 1)
    Yellow_finger = st.selectbox('Are your fingers yellow?, HINT 2 for yes and 1 for no', options = [2,1], index = 1)
    Anxiety = st.selectbox('Are you always anxious?, HINT 2 for yes and 1 for no', options = [2,1], index = 1)
    Peer_Pressure = st.selectbox('Do you have Peer Pressure issue?, HINT 2 for yes and 1 for no', options = [2,1], index = 1)
    Chronic_Disease = st.selectbox('Do you have any chronic Disease?, HINT 2 for yes and 1 for no', options = [2,1], index = 1)
    Fatigue = st.selectbox('Do you feel fatigue ?, HINT 2 for yes and 1 for no', options = [2,1], index = 1)
    Allergy = st.selectbox('Do you have any allergy(ies)?, HINT 2 for yes and 1 for no', options = [2,1], index = 1)
    Wheezing = st.selectbox('Do you have Wheezling issue?, HINT 2 for yes and 1 for no', options = [2,1], index = 1)
    Alcohol = st.selectbox('Do you drink Alcohol?, HINT 2 for yes and 1 for no', options = [2,1], index = 1)
    Cough = st.selectbox('Do you cough?, HINT 2 for yes and 1 for no', options = [2,1], index = 1)
    Short = st.selectbox('Do you experience shortness in breathing?, HINT 2 for yes and 1 for no', options = [2,1], index = 1)
    Swallowing = st.selectbox('Do you have difficulties when swallowing?, HINT 2 for yes and 1 for no', options = [2,1], index = 1)
    Chest = st.selectbox('Do you feel Chest pain?, HINT 2 for yes and 1 for no', options = [2,1], index = 1)
    
    

    data = {'AGE':Age,
            'SMOKING':  Smoking,
            'YELLOW_FINGERS': Yellow_finger,
            'ANXIETY':  Anxiety,  
            'PEER_PRESSURE':Peer_Pressure,
            'CHRONIC DISEASE':Chronic_Disease,
            'FATIGUE ':Fatigue,
            'ALLERGY ': Allergy,
            'WHEEZING': Wheezing,
            'ALCOHOL CONSUMING': Alcohol,
            'COUGHING': Cough,
            'SHORTNESS OF BREATH': Short,
            'SWALLOWING DIFFICULTY': Swallowing,
            'CHEST PAIN':Chest
            #'page':page
           
           
           }

    features = pd.DataFrame(data, index=[0])  #- convert the dictionary to dataframe
    
    return features

df = user_imput()



def prediction():
    predict = model.predict(df)
    result = ''
    if predict == 0:
        result = 'Negative Result'
    else:
        result= 'Positive Result'
    return result


submit = st.button('Get prediction')
result = prediction()
if submit:
    st.success('Thank you for filling the form. It is a  {}'.format(result))

