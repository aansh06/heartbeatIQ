
# import pickle
# from joblib import  load
# import streamlit as st
# from streamlit_option_menu import option_menu


# # loading the saved models
# heart_disease_model = load('heartbeatIQ_model.joblib')

# # heart_disease_model = pickle.load(open('heartbeatIQ_model.sav','rb'))


# # sidebar for navigation
# with st.sidebar:
    
#     selected = option_menu('HeartBeatIQ',
                          
#                           [
#                            'Heart Disease Prediction',
#                            ],
#                           icons=['activity','heart','person'],
#                           default_index=0)
    
    

    


# # Heart Disease Prediction Page
# if (selected == 'Heart Disease Prediction'):
    
#     # page title
#     st.title('Heart Disease Prediction using ML')
    
#     col1, col2, col3 = st.columns(3)
    
#     with col1:
#         age = st.text_input('Age')
        
#     with col2:
#         sex = st.text_input('Sex')
        
#     with col3:
#         cp = st.text_input('Chest Pain types')
        
#     with col1:
#         trestbps = st.text_input('Resting Blood Pressure')
        
#     with col2:
#         chol = st.text_input('Serum Cholestoral in mg/dl')
        
#     with col3:
#         fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')
        
#     with col1:
#         restecg = st.text_input('Resting Electrocardiographic results')
        
#     with col2:
#         thalach = st.text_input('Maximum Heart Rate achieved')
        
#     with col3:
#         exang = st.text_input('Exercise Induced Angina')
        
#     with col1:
#         oldpeak = st.text_input('ST depression induced by exercise')
        
#     with col2:
#         slope = st.text_input('Slope of the peak exercise ST segment')
        
#     with col3:
#         ca = st.text_input('Major vessels colored by flourosopy')
        
#     with col1:
#         thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')
        
        
     
     
#     # code for Prediction
#     heart_diagnosis = ''
    
#     # creating a button for Prediction
    
#     if st.button('Heart Disease Test Result'):
#         age = float(age)
#         sex = float(sex)
#         cp = float(cp)
#         trestbps = float(trestbps)
#         chol = float(chol)
#         fbs = float(fbs)
#         restecg = float(restecg)
#         thalach = float(thalach)
#         exang = float(exang)
#         oldpeak = float(oldpeak)
#         slope = float(slope)
#         ca = float(ca)
#         thal = float(thal)
#         heart_prediction = heart_disease_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg,thalach,exang,oldpeak,slope,ca,thal]])                          
        
#         if (heart_prediction[0] == 1):
#           heart_diagnosis = 'The person is having heart disease'
#         else:
#           heart_diagnosis = 'The person does not have any heart disease'
        
#     st.success(heart_diagnosis)
        
    
    
# from joblib import load
# import streamlit as st
# import numpy as np


# import sklearn
# import joblib
# print('scikit-learn version:', sklearn.__version__)
# print('joblib version:', joblib.__version__)


# # Load the saved model
# heart_disease_model = load('heartbeatIQ_model.joblib')

# # Sidebar for navigation
# with st.sidebar:
#     selected = st.selectbox('Select a Page', ['Heart Disease Prediction'])

# # Heart Disease Prediction Page
# if selected == 'Heart Disease Prediction':
#     # Page title
#     st.title('Heart Disease Prediction using ML')
    
#     # Input fields
#     age = st.number_input('Age')
#     sex = st.number_input('Sex')
#     cp = st.number_input('Chest Pain types')
#     trestbps = st.number_input('Resting Blood Pressure')
#     chol = st.number_input('Serum Cholestoral in mg/dl')
#     fbs = st.number_input('Fasting Blood Sugar > 120 mg/dl')
#     restecg = st.number_input('Resting Electrocardiographic results')
#     thalach = st.number_input('Maximum Heart Rate achieved')
#     exang = st.number_input('Exercise Induced Angina')
#     oldpeak = st.number_input('ST depression induced by exercise')
#     slope = st.number_input('Slope of the peak exercise ST segment')
#     ca = st.number_input('Major vessels colored by flourosopy')
#     thal = st.number_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')
    
#     # Prediction button
#     if st.button('Heart Disease Test Result'):
#         # Create input data array
#         input_data = np.array([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])
        
#         # Make prediction
#         prediction = heart_disease_model.predict(input_data)
        
#         # Display prediction result
#         if prediction[0] == 1:
#             result = 'The person is diagnosed with heart disease.'
#         else:
#             result = 'The person does not have heart disease.'
        
#         st.success(result)



# from joblib import load
# import streamlit as st
# import numpy as np

# # loading the saved model
# heart_disease_model = load('heartbeatIQ_model.joblib')

# # Map original parameter names to user-friendly names and options
# parameter_info = {
#     'age': ('Age', None),
#     'sex': ('Sex', {'Female': 0, 'Male': 1}),
#     'cp': ('Chest Pain Type', {'Typical angina': 0, 'Atypical angina': 1, 'Non-anginal pain': 2, 'Asymptomatic': 3}),
#     'trestbps': ('Resting Blood Pressure (mm Hg)', None),
#     'chol': ('Serum Cholesterol (mg/dl)', None),
#     'fbs': ('Fasting Blood Sugar', {'<= 120 mg/dl': 0, '> 120 mg/dl': 1}),
#     'restecg': ('Resting Electrocardiographic Results', {'Normal': 0, 'ST-T wave abnormality': 1, 'Probable or definite left ventricular hypertrophy': 2}),
#     'thalach': ('Maximum Heart Rate Achieved', None),
#     'exang': ('Exercise Induced Angina', {'No': 0, 'Yes': 1}),
#     'oldpeak': ('ST Depression Induced by Exercise', None),
#     'slope': ('Slope of the Peak Exercise ST Segment', {'Upsloping': 0, 'Flat': 1, 'Downsloping': 2}),
#     'ca': ('Number of Major Vessels Colored by Fluoroscopy', {str(i): i for i in range(4)}),
#     'thal': ('Thalassemia', {'Normal': 0, 'Fixed Defect': 1, 'Reversible Defect': 2})
# }

# # Sidebar for navigation
# with st.sidebar:
#     st.title('HeartBeatIQ')
#     selected = st.radio('Select Functionality', ['Heart Disease Prediction'])

# # Heart Disease Prediction Page
# if selected == 'Heart Disease Prediction':
#     # Page title
#     st.title('Heart Disease Prediction using Machine Learning')

#     # Input fields
#     user_inputs = {}
#     for param, info in parameter_info.items():
#         name, options = info
#         if options:
#             user_inputs[param] = st.selectbox(name, options.keys())
#         else:
#             user_inputs[param] = st.slider(name, min_value=0, max_value=200, step=1)

#     # Function to convert categorical inputs to numerical values
#     def convert_to_numeric(param, value):
#         options = parameter_info[param][1]
#         return options[value]

#     # Prepare input data for prediction
#     input_data = [convert_to_numeric(param, value) if param in parameter_info and parameter_info[param][1] else float(value) for param, value in user_inputs.items()]

#     # Make prediction
#     heart_prediction = heart_disease_model.predict([input_data])[0]

#     # Display prediction result
#     if heart_prediction == 1:
#         st.success('The person is predicted to have heart disease.')
#     else:
#         st.success('The person is predicted to be healthy and not have heart disease.')



from joblib import load
import streamlit as st

# loading the saved model
heart_disease_model = load('heartbeatIQ_model.joblib')

# Map original parameter names to user-friendly names and options
parameter_info = {
    'age': ('Age', None),
    'sex': ('Sex', {'Female': 0, 'Male': 1}),
    'cp': ('Chest Pain Type', {'Typical angina': 0, 'Atypical angina': 1, 'Non-anginal pain': 2, 'Asymptomatic': 3}),
    'trestbps': ('Resting Blood Pressure (mm Hg)', None),
    'chol': ('Serum Cholesterol (mg/dl)', None),
    'fbs': ('Fasting Blood Sugar', {'<= 120 mg/dl': 0, '> 120 mg/dl': 1}),
    'restecg': ('Resting Electrocardiographic Results', {'Normal': 0, 'ST-T wave abnormality': 1, 'Probable or definite left ventricular hypertrophy': 2}),
    'thalach': ('Maximum Heart Rate Achieved', None),
    'exang': ('Exercise Induced Angina', {'No': 0, 'Yes': 1}),
    'oldpeak': ('ST Depression Induced by Exercise', None),
    'slope': ('Slope of the Peak Exercise ST Segment', {'Upsloping': 0, 'Flat': 1, 'Downsloping': 2}),
    'ca': ('Number of Major Vessels Colored by Fluoroscopy', {str(i): i for i in range(4)}),
    'thal': ('Thalassemia', {'Normal': 0, 'Fixed Defect': 1, 'Reversible Defect': 2})
}

# Sidebar for navigation
with st.sidebar:
    st.title('HeartBeatIQ')
    selected = st.radio('Select Functionality', ['Heart Disease Prediction'])

# Heart Disease Prediction Page
if selected == 'Heart Disease Prediction':
    # Page title
    st.title('Heart Disease Prediction using Machine Learning')

    # Input fields
    user_inputs = {}
    for param, info in parameter_info.items():
        name, options = info
        if options:
            user_inputs[param] = st.selectbox(name, options.keys())
        else:
            # Adjust slider values as requested
            if param == 'age':
                user_inputs[param] = st.slider(name, min_value=0, max_value=100, step=1)
            elif param == 'chol':
                user_inputs[param] = st.slider(name, min_value=0, max_value=600, step=1)
            elif param == 'thalach':
                user_inputs[param] = st.slider(name, min_value=0, max_value=220, step=1)  # corrected max to realistic heart rate
            elif param == 'oldpeak':
                user_inputs[param] = st.slider(name, min_value=0.0, max_value=10.0, step=0.1)
            else:
                user_inputs[param] = st.slider(name, min_value=0, max_value=200, step=1)

    # Function to convert categorical inputs to numerical values
    def convert_to_numeric(param, value):
        options = parameter_info[param][1]
        return options[value]

    # Prepare input data for prediction
    input_data = [convert_to_numeric(param, value) if param in parameter_info and parameter_info[param][1] else float(value) for param, value in user_inputs.items()]

    # Make prediction
    heart_prediction = heart_disease_model.predict([input_data])[0]

    # Display prediction result
    if heart_prediction == 1:
        st.success('The person is predicted to have heart disease.')
    else:
        st.success('The person is predicted to be healthy and not have heart disease.')
