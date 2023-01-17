import pandas as pd
import numpy as np
import pickle
import streamlit as st
from PIL import Image
# loading in the model to predict on the data
pickle_in = open(r".\classifier.pkl", 'rb')
classifier = pickle.load(pickle_in)

print(classifier)

def prediction(Attributes):  
   
    prediction = classifier.predict([Attributes])
    print(prediction)
    return prediction

def toCategoricalVar(Age ,Gender,Country,state,self_employed ,family_history  ,work_interfere ,no_employees ,remote_work  ,tech_company ,benefits     ,care_options ,wellness_program,seek_help    ,anonymity    ,leave ,mental_health_consequence ,phys_health_consequence ,coworkers    ,supervisor   ,mental_health_interview ,phys_health_interview,mental_vs_physical,obs_consequence ):
    Age=0
    if Gender == "Male":
        Gender = 0
    else:
        Gender = 1


    Country=0
    state=0
    
    if self_employed=="Yes":
        self_employed=1
    else:
        self_employed=0
    
    if family_history=="Yes":
        family_history=1
    else:
        family_history=0
        
    # if treatment=="Yes":
    #     treatment=1
    # else:
    #     treatment=0
    
    if work_interfere=="Rarely":
        work_interfere=1
    elif work_interfere=="Often":
        work_interfere=0
    elif work_interfere=="Sometimes":
        work_interfere=2
    else:
        work_interfere=3
    
    no_employees=0
    
    if remote_work=="Yes":
        remote_work=1
    else:
        remote_work=0
    tech_company=0
    benefits=0
    #---------
    # if tech_company=="Yes":
    #     tech_company=1
    # else:
    #     tech_company=0
    # #---------
    # if benefits=="Yes":
    #     benefits=1
    # elif benefits=="Dont know":
    #     benefits=0
    # else:
    #     benefits=2
    
    if care_options=="Yes":
        care_options=1
    elif care_options=="No":
        care_options=0
    else:
        care_options=2
    
    if wellness_program=="Yes":
        wellness_program=1
    elif wellness_program=="Dont know":
        wellness_program=0
    else:
        wellness_program=2
    
    if seek_help=="Yes":
        seek_help=1
    elif seek_help=="Dont know":
        seek_help=0
    else:
        seek_help=2
        
    if anonymity=="Yes":
        anonymity=1
    elif anonymity=="Dont know":
        anonymity=0
    else:
        anonymity=2
        
    if leave=="Somewhat easy":
        leave=4
    elif leave=="Dont know":
        leave=3
    elif leave=="Somewhat difficult":
        leave=2
    elif leave=="Very difficult":
        leave=1
    else:
        leave=0

    if mental_health_consequence=="Yes":
        mental_health_consequence=1
    elif mental_health_consequence=="Maybe":
        mental_health_consequence=2
    else:
        mental_health_consequence=0

    if phys_health_consequence=="Yes":
        phys_health_consequence=1
    elif phys_health_consequence=="Maybe":
        phys_health_consequence=2
    else:
       phys_health_consequence =0
       
    if coworkers=="Yes":
        coworkers=1
    elif coworkers=="Some of them":
        coworkers=2
    else:
        coworkers=0
        
    if supervisor=="Yes":
        supervisor=1
    elif supervisor=="Some of them":
        supervisor=2
    else:
        supervisor=0
    if mental_health_interview=="Yes":
        mental_health_interview=1
    elif mental_health_interview=="Maybe":
        mental_health_interview=2
    else:
        mental_health_interview=0
        
    if phys_health_interview=="Yes":
        phys_health_interview=1
    elif phys_health_interview=="Maybe":
        phys_health_interview=2
    else:
        phys_health_interview=0

    if mental_vs_physical=="Yes":
        mental_vs_physical=1
    elif mental_vs_physical=="Dont know":
        mental_vs_physical =2
    else:
        mental_vs_physical=0
        
    if obs_consequence=="Yes":
        obs_consequence=1
    else:
        obs_consequence=0
        
    
    return [Age ,Gender,Country,state,self_employed ,family_history  ,work_interfere ,no_employees ,remote_work  ,tech_company ,benefits ,care_options ,wellness_program,seek_help    ,anonymity    ,leave ,mental_health_consequence ,phys_health_consequence ,coworkers    ,supervisor   ,mental_health_interview ,phys_health_interview,mental_vs_physical,obs_consequence ]
        
def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://images.ctfassets.net/h8qzhh7m9m8u/aD8jYxTLmzMC5ZNIRC6M1/b62a4e3dec1100cb6012fd5a4552fe70/2100x1200px_Article_Hero_Memory.png");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )




def main():
      # giving the webpage a title
    add_bg_from_url()

    st.markdown("<h1 style='text-align: center; color: black;'>Predict your Mental health</h1>", unsafe_allow_html=True)
    
    Age=0
    Country=0
    state=0
    no_employees=0
    tech_company=0
    benefits=0
    Gender = st.selectbox( 
    'Gender',
    ('select' , 'Male', 'Female')
    )
    self_employed = st.selectbox(
    'Are you Self Employed?',
    ('select' , 'Yes', 'No'))
    family_history = st.selectbox(
        'Do you have a family history of mental illness?',
        ('select' , 'Yes', 'No')
    )
    
    # treatment = st.selectbox(
    #     'Have you sought treatment for a mental health condition?',
    #     ('select' , 'Yes', 'No')
    # )
    work_interfere = st.selectbox("If you have a mental health condition, do you feel that it interferes with your work?", 
    ('select' , 'Often' , 'Rarely','Never','Sometimes'))
    
    remote_work = st.selectbox(
        'Do you work remotely (outside of an office) at least 50% of the time?',
        ('select' , 'Yes', 'No')
    )
    # benefits = st.selectbox(
    #     'Does your employer provide mental health benefits?',
    #     ('select' , 'Yes', 'No','Dont know')
    # )
    care_options = st.selectbox(
        'Do you know the options for mental health care your employer provides?',
        ('select' , 'Yes', 'No','Not sure')
    )
    wellness_program = st.selectbox(
        'Has your employer ever discussed mental health as part of an employee wellness program?',
        ('select' , 'Yes', 'No','Dont know')
    )
    seek_help = st.selectbox(
        'Does your employer provide resources to learn more about mental health issues and how to seek help?',
        ('select' , 'Yes', 'No','Dont know')
    )
    anonymity = st.selectbox(
        'Is your anonymity protected if you choose to take advantage of mental health or substance abuse treatment resources?',
        ('select' , 'Yes', 'No','Dont know')
    )
    leave = st.selectbox(
        'How easy is it for you to take medical leave for a mental health condition?',
        ('select' , 'Very easy','Somewhat easy', 'Very difficult','Somewhat difficult','Dont know')
    )
    mental_health_consequence = st.selectbox(
        'Do you think that discussing a mental health issue with your employer would have negative consequences?',
        ('select' , 'Yes', 'No','Maybe')
    )
    phys_health_consequence = st.selectbox(
        'Do you think that discussing a physical health issue with your employer would have negative consequences?',
        ('select' , 'Yes', 'No','Maybe')
    )
    coworkers = st.selectbox(
        'Would you be willing to discuss a mental health issue with your coworkers?',
        ('select' , 'Yes', 'No','Some of them')
    )
    supervisor = st.selectbox(
        'Would you be willing to discuss a mental health issue with your direct supervisor(s)?',
        ('select' , 'Yes', 'No','Some of them')
    )
    mental_health_interview  = st.selectbox(
        'Would you bring up a mental health issue with a potential employer in an interview?',
        ('select' , 'Yes', 'No','Maybe')
    )
    phys_health_interview  = st.selectbox(
        'Would you bring up a physcial health issue with a potential employer in an interview?',
        ('select' , 'Yes', 'No','Maybe')
    )
    mental_vs_physical = st.selectbox(
        'Do you feel that your employer takes mental health as seriously as physical health?',
        ('select' , 'Yes', 'No','Dont know')
    )
    obs_consequence = st.selectbox(
        'Have you heard of or observed negative consequences for coworkers with mental health conditions in your workplace?',
        ('select' , 'Yes', 'No')
    )
    
    
    
    Attributes = toCategoricalVar(Age ,Gender,Country,state,self_employed ,family_history ,work_interfere ,no_employees ,remote_work  ,tech_company ,benefits     ,care_options ,wellness_program,seek_help    ,anonymity    ,leave ,mental_health_consequence ,phys_health_consequence ,coworkers    ,supervisor   ,mental_health_interview ,phys_health_interview,mental_vs_physical,obs_consequence)
    # def prediction(Attributes):  
   
    # prediction = classifier.predict(
    #     [Attributes])
    # print(prediction)
    # return prediction
    
    result =""
    ans = ""
    if st.button("Predict"):
        result = prediction(Attributes)
        if result == 1:
            ans = "Your mental state is not stable, you may need to consult a doctor"
        else:
            ans = "Your mental health is completely alright!! go rock your day"
        st.success(ans)
     
if __name__=='__main__':
    main()