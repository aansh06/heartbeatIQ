from joblib import load
import streamlit as st

# loading the saved model
heart_disease_model = load('models/heartbeatIQ_model.joblib')

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
    st.title("Let's check your heart's life")

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
    if heart_prediction == 0:
        st.success('The person is predicted to have heart disease.')
    else:
        st.success('The person is predicted to be healthy and not have heart disease.')
