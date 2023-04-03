import streamlit as st
import firebase_admin
from firebase_admin import credentials, firestore
from ims_lti_py import ToolProvider

# Initialize Firebase Admin SDK
cred = credentials.Certificate('path/to/serviceAccountKey.json')
firebase_admin.initialize_app(cred)
db = firestore.client()

# Define a function to register a new student or learner
def register_student(name, email, role, course_id):
    doc_ref = db.collection('students').document(email)
    doc_ref.set({
        'name': name,
        'email': email,
        'role': role,
        'course_id': course_id
    })

# Create a Streamlit app
st.title('Student/Learner Registration')
st.write('Enter your details to register as a student/learner.')

# Retrieve LTI launch parameters
launch_params = ToolProvider.from_flask_request(request).to_dict()

# Display the form to register a new student or learner
name = st.text_input('Name')
email = st.text_input('Email')
role = st.selectbox('Role', ['Student', 'Learner'])
course_id = st.text_input('Course ID', launch_params['context_id'])

# Register the student or learner when the form is submitted
if st.button('Register'):
    register_student(name, email, role, course_id)
    st.success('Registration successful.')
