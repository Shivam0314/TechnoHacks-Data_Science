# Task 2: Employee turnover prediction

import streamlit as st
import pickle
import numpy as np
import warnings

warnings.simplefilter("ignore")

# Load the trained model and label encoder mapping
model = pickle.load(open("random_forest_model.pkl", "rb"))
label_encoder_mapping = pickle.load(open("label_encoder_mapping.pkl", "rb"))

st.title("Employee Attrition Prediction App")
# Y_pred = [[1, 113, 1, 7, 0, 1, 2, 1, 31, 1, 1, 6, 1, 1, 682, 1328, 1, 0, 12, 1, 3, 1, 10, 3, 2, 10, 7, 1, 7, 31]]
# # [2, 624, 2, 0, 1, 1, 1, 0, 64, 2, 1, 7, 3, 2, 809, 999, 8, 1, 0, 0, 0, 0, 8, 0, 0, 6, 4, 0, 5, 23]


# Mapping dictionaries
# attrition_mapping = {'No': 0, 'Yes': 1}

business_travel_mapping = {"Non-Travel": 0, "Travel_Frequently": 1, "Travel_Rarely": 2}
department_mapping = {"Human Resources": 0, "Research & Development": 1, "Sales": 2}
education_field_mapping = {
    "Human Resources": 0,
    "Life Sciences": 1,
    "Marketing": 2,
    "Medical": 3,
    "Other": 4,
    "Technical Degree": 5,
}
gender_mapping = {"Female": 0, "Male": 1}
job_role_mapping = {
    "Healthcare Representative": 0,
    "Human Resources": 1,
    "Laboratory Technician": 2,
    "Manager": 3,
    "Manufacturing Director": 4,
    "Research Director": 5,
    "Research Scientist": 6,
    "Sales Executive": 7,
    "Sales Representative": 8,
}
marital_status_mapping = {"Divorced": 0, "Married": 1, "Single": 2}
overtime_mapping = {"No": 0, "Yes": 1}


business_travel_value = st.selectbox(
    "Business Travel:", list(business_travel_mapping.keys())
)
st.write("Mapping for Business Travel:")
st.table(
    {"Value": business_travel_mapping.keys(), "Code": business_travel_mapping.values()}
)


department_value = st.selectbox("Department:", list(department_mapping.keys()))
st.write("Mapping for Department:")
st.table({"Value": department_mapping.keys(), "Code": department_mapping.values()})


education_field_value = st.selectbox(
    "Education Field:", list(education_field_mapping.keys())
)
st.write("Mapping for Education Field:")
st.table(
    {"Value": education_field_mapping.keys(), "Code": education_field_mapping.values()}
)


gender_value = st.selectbox("Gender:", list(gender_mapping.keys()))
st.write("Mapping for Gender:")
st.table({"Value": gender_mapping.keys(), "Code": gender_mapping.values()})


job_role_value = st.selectbox("Job Role:", list(job_role_mapping.keys()))
st.write("Mapping for Job Role:")
st.table({"Value": job_role_mapping.keys(), "Code": job_role_mapping.values()})


marital_status_value = st.selectbox(
    "Marital Status:", list(marital_status_mapping.keys())
)
st.write("Mapping for Marital Status:")
st.table(
    {"Value": marital_status_mapping.keys(), "Code": marital_status_mapping.values()}
)

overtime_value = st.selectbox("OverTime:", list(overtime_mapping.keys()))
st.write("Mapping for Overtime:")
st.table({"Value": overtime_mapping.keys(), "Code": overtime_mapping.values()})

# Encode categorical values
# encoded_attrition = attrition_mapping[attrition_value]
encoded_business_travel = business_travel_mapping[business_travel_value]
DailyRate = st.number_input(
    "Daily Rate", min_value=0, max_value=1500, value=624, step=1
)
encoded_department = department_mapping[department_value]
DistanceFromHome = st.number_input(
    "Distance From Home", min_value=0, max_value=35, value=0, step=1
)
Education = st.number_input("Education", min_value=0, max_value=5, value=1, step=1)
encoded_education_field = education_field_mapping[education_field_value]
EnvironmentSatisfaction = st.number_input(
    "Environment Satisfaction", min_value=0, max_value=5, value=1, step=1
)
encoded_gender = gender_mapping[gender_value]
HourlyRate = st.number_input("Hourly Rate", min_value=0, max_value=70, value=64, step=1)
JobInvolvement = st.number_input(
    "Job Involvement", min_value=0, max_value=5, value=2, step=1
)
JobLevel = st.number_input("Job Level", min_value=0, max_value=5, value=1, step=1)
encoded_job_role = job_role_mapping[job_role_value]
JobSatisfaction = st.number_input(
    "Job Satisfaction", min_value=0, max_value=5, value=3, step=1
)
encoded_marital_status = marital_status_mapping[marital_status_value]
MonthlyIncome = st.number_input(
    "Monthly Income", min_value=0, max_value=1400, value=809, step=1
)
MonthlyRate = st.number_input(
    "Monthly Rate", min_value=0, max_value=1500, value=999, step=1
)
NumCompaniesWorked = st.number_input(
    "Number of Companies Worked", min_value=0, max_value=15, value=8, step=1
)
encoded_overtime = overtime_mapping[overtime_value]
PercentSalaryHike = st.number_input(
    "Percent of Salary Hike", min_value=0, max_value=20, value=0, step=1
)
PerformanceRating = st.number_input(
    "Performance Rating", min_value=0, max_value=5, value=0, step=1
)

RelationshipSatisfaction = st.number_input(
    "Relationship Satisfaction", min_value=0, max_value=5, value=0, step=1
)
StockOptionLevel = st.number_input(
    "Stock Option Level", min_value=0, max_value=0, value=0, step=1
)
TotalWorkingYears = st.number_input(
    "Total Working Years", min_value=0, max_value=45, value=8, step=1
)
TrainingTimesLastYear = st.number_input(
    "Training Times Last Year", min_value=0, max_value=10, value=0, step=1
)

WorkLifeBalance = st.number_input(
    "Work Life Balance", min_value=0, max_value=5, value=0, step=1
)
YearsAtCompany = st.number_input(
    "Years At Company", min_value=0, max_value=40, value=6, step=1
)
YearsInCurrentRole = st.number_input(
    "Years In Current Role", min_value=0, max_value=20, value=4, step=1
)
YearsSinceLastPromotion = st.number_input(
    "Years Since Last Promotion", min_value=0, max_value=20, value=0, step=1
)
YearsWithCurrManager = st.number_input(
    "Years With Current Manager", min_value=0, max_value=20, value=5, step=1
)
Age_Years = st.number_input("Age Years", min_value=0, max_value=50, value=23, step=1)


BusinessTravel = encoded_business_travel
Department = encoded_department
EducationField = encoded_education_field
Gender = encoded_gender
JobRole = encoded_job_role
MaritalStatus = encoded_marital_status
OverTime = encoded_overtime


if st.button("Predict"):
    Y_pred2 = [
        [
            BusinessTravel,
            DailyRate,
            Department,
            DistanceFromHome,
            Education,
            EducationField,
            EnvironmentSatisfaction,
            Gender,
            HourlyRate,
            JobInvolvement,
            JobLevel,
            JobRole,
            JobSatisfaction,
            MaritalStatus,
            MonthlyIncome,
            MonthlyRate,
            NumCompaniesWorked,
            OverTime,
            PercentSalaryHike,
            PerformanceRating,
            RelationshipSatisfaction,
            StockOptionLevel,
            TotalWorkingYears,
            TrainingTimesLastYear,
            WorkLifeBalance,
            YearsAtCompany,
            YearsInCurrentRole,
            YearsSinceLastPromotion,
            YearsWithCurrManager,
            Age_Years,
        ]
    ]

    prediction = model.predict(Y_pred2)
    if prediction[0] == 0:
        result = "No Attrition"
    else:
        result = "Attrition"

    st.success(f"Prediction: {result}")
