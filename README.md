#                                                                  💼 HR & Payroll Management System

A simple and interactive **HR & Payroll Management System** built using **Python** and **Streamlit**. This system enables secure user login, employee record management, and payroll calculations with CSV-based data storage — making it lightweight and database-free.

## 🚀 Features

- 🔐 **User Authentication**
  - Role-based access: Admin, HR, Payroll.
  - Secure login/logout using `st.session_state`.

- 👥 **Employee Management**
  - Add new employees with basic details.
  - View all existing employee records.
  - Role-restricted access (Admin & HR only).

- 💰 **Payroll Management**
  - Calculate payroll based on hours and hourly rate.
  - View gross, tax, and net salary.
  - Save payroll records to CSV.
  - Accessible only by Admin or Payroll roles.

- 📊 **Data Viewer**
  - View employee data.
  - View payroll data.

## 🛠️ Technologies Used

- [Python](https://www.python.org/)
- [Streamlit](https://streamlit.io/)
- [Pandas](https://pandas.pydata.org/)
- CSV files for persistent storage

## 📁 Project Structure
├── app.py # Main Streamlit app
├── payroll.py # Payroll logic (calculate gross, tax, net)
├── user.py # User authentication and role handling
├── utils.py # CSV file operations (init, load, save)
├── employees.csv # Employee data (auto-created)
├── payroll_data.csv # Payroll data (auto-created)


## 🧠 User Roles

| Role     | Permissions                           |
|----------|----------------------------------------|
| Admin    | Full access to employee & payroll data |
| HR       | Manage employee records                |
| Payroll  | Manage payrolls                        |
| Viewer   | View data only (customize if needed)   |




