# necassary libraries
import streamlit as st
import pandas as pd
from payroll import calculate_payroll
from user import authenticate, get_user_role
from utils import (init_emp_csv,load_emp_data,
                   save_emp_data,init_pay_csv,
                   load_pay_data,save_pay_data)

# init csv files if not exist
init_emp_csv()
init_pay_csv()

# session state
if "logged_in" not in st.session_state:
    st.session_state.logged_in  = False
    st.session_state.username = ""
    st.session_state.role=""

# login
if not st.session_state.logged_in  :
    st.title("🔒 Login to the HR & Payroll System")
    username = st.text_input("Username")
    password = st.text_input("Password",type="password")

    if st.button("Login"):
        if authenticate(username,password):
            st.session_state.logged_in  = True
            st.session_state.username=username
            st.session_state.role=get_user_role(username)
            st.success(f"✅ Logged in as {username} ({st.session_state.role}) ")
            st.rerun()
        else:
            st.error("❌ Invalid username or password")
    st.stop()

# Sidebar Logout
with st.sidebar:
    st.markdown(f"👥 **User:**'{st.session_state.username}' ")
    st.markdown(f"🤖 **Role**'{st.session_state.role}' ")
    if st.button("Logout"):
        st.session_state.logged_in  = False
        st.session_state.username = ""
        st.session_state.role = ""
        st.success("Logged out")
        st.rerun()

# Main menu
st.title("📚 HR & Payroll Management System")

menu = st.sidebar.selectbox("Select Module",["Employee's Management", "Payroll Management", "View Data"])
if menu == "Employee's Management":
    if st.session_state.role not in ["Admin","HR"]:
        st.warn("⚠️ Access is refused. ONly the admins and the HRs can manage.")
        st.stop()

    st.header("Add New Employee")
    name = st.text_input("Employee-Name")
    E_id = st.text_input("Employee-ID")
    dept = st.selectbox("Departments ",["HR", "IT",  "Finance", "Marketing"])
    join_date = st.date_input("Joining-Date")
    status = st.selectbox("Status",["Active","Inactive"])

    if st.button("Add Employee"):
        if not name or not E_id:
            st.warn("Id and the Names are required.")
        else:
            df = load_emp_data()
            if E_id in df['ID'].values:
                st.error("⚠️ Employee ID is already existing.")
            else:
                new_row = {"ID": E_id,
                         "Name": name,
                         "Department": dept,
                         "Joining-Date": join_date,
                         "Status": status
                         }
                df = pd.concat([df,pd.DataFrame([new_row])],ignore_index=True)
                save_emp_data(df)
                st.success(f"✅ Employee '{name}' added.")
    st.subheader("📃 Current Employees")
    st.dataframe(load_emp_data(),use_container_width  =  True)

# Payroll
elif menu ==  "Payroll Management":
    if st.session_state.role not in ["Admin","Payroll"]:
        st.warn("⚠️Access Denied. Only Admin or the HR can manage employees.")
        st.stop()
    st.header("Payroll  Calculator")
    emp_df = load_emp_data()
    if emp_df.empty:
        st.warn("⚠️  NO EMPLOYEE RECORD FOUND.")
    else:
        selected_id = st.selectbox("Select Employee ID",emp_df["ID"].tolist())
        emp_name = emp_df.loc[emp_df["ID"] == selected_id,"Name"].values[0]
        st.text(f"Employee Name: {emp_name}")
        hours = st.number_input("Hours Worked",min_value=0.0)
        rate = st.number_input("Hours Rate",min_value=0.0)
        if st.button("Calculate Payroll"):
            gross,tax,net=calculate_payroll(hours,rate)
            st.success(f"📃 Gross:${gross:.2f}")
            st.success(f"💸 Tax:${tax:.2f}")
            st.success(f"✅ Net:${net:.2f}")

            payroll_df = load_pay_data()
            new_row = {
                "ID":selected_id,
                "Name": emp_name,
                "Hours-worked":hours,
                "Hourly-Rate": rate,
                "Gross-Salary":gross,
                "Tax-Deducted":tax,
                "Net-Salary":net
            }
            payroll_df = pd.concat([payroll_df, pd.DataFrame([new_row])], ignore_index=True)
            save_pay_data(payroll_df)
            st.success("✅ Records for the payroll are saved.")

#View Data
elif menu == "View Data":
    st.header("🗃️ View the stored Data")
    view_choice = st.radio("Choose Data",["Employees",  "Payroll"])

    if view_choice == "Employees":
        st.subheader("Data for the Employees")
        st.dataframe(load_emp_data(),use_container_width=True)

    elif view_choice == "Payroll":
        st.subheader("💸 Records for the Payroll")
        st.dataframe(load_pay_data(),use_container_width=True)
