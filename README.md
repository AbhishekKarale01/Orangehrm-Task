# OrangeHRM Dashboard Automation

## Overview

This project is a Dashboard-Driven RPA Automation solution developed using **Python, FastAPI, Selenium, HTML, and CSS**.

The application provides a web-based dashboard where users can enter OrangeHRM login credentials and employee information. Upon submission, the automation performs employee management operations on the OrangeHRM demo website and displays the results back on the dashboard.

Website Used:

https://opensource-demo.orangehrmlive.com

---

## Features

### Dashboard Functionality

* Enter OrangeHRM login credentials
* Enter employee details:

  * First Name
  * Last Name
  * Employee ID
* Trigger automation from the dashboard
* Display automation status
* Display inserted employee details
* Display extracted employee list data

### Automation Functionality

* Open OrangeHRM website
* Login using dashboard credentials
* Navigate to PIM module
* Add a new employee
* Verify employee creation
* Extract employee list data
* Export employee data to Excel
* Logout from the application

### Additional Features

* Logging for all automation steps
* Exception handling
* Dynamic credential handling (no hardcoded credentials)
* Excel export using Pandas
* Responsive UI

---

## Technology Stack

### Backend

* Python 3.x
* FastAPI

### Automation

* Selenium WebDriver
* ChromeDriver

### Frontend

* HTML5
* CSS3
* Jinja2 Templates

### Data Handling

* Pandas
* OpenPyXL

### Logging

* Python Logging Module

---

## Project Structure

```text
orangehrm_automation/
│
├── main.py
├── automation.py
├── requirements.txt
│
├── templates/
│   └── index.html
│
├── static/
│   └── style.css
│
├── logs/
│   └── automation.log
│
├── employee_list.xlsx
│
└── README.md
```

---

## Installation

### Clone Repository

```bash
git clone https://github.com/your-username/orangehrm-dashboard-automation.git
cd orangehrm-dashboard-automation
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

Windows:

```bash
venv\Scripts\activate
```

Linux/Mac:

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Run Application

Start FastAPI Server:

```bash
uvicorn main:app --reload
```

Open Browser:

```text
http://127.0.0.1:8000
```

---

## Demo Credentials

```text
Username: Admin
Password: admin123
```

---

## Automation Workflow

1. User enters credentials and employee details on dashboard.
2. Dashboard sends request to FastAPI backend.
3. Selenium launches browser.
4. Login to OrangeHRM.
5. Navigate to PIM module.
6. Add employee.
7. Verify employee creation.
8. Extract employee list.
9. Export data to Excel.
10. Logout from application.
11. Display results on dashboard.

---

## Generated Output

### Dashboard Output

* Automation Status
* Employee Details
* Employee List

### Files Generated

```text
employee_list.xlsx
logs/automation.log
```

---

## Logging

All automation activities are logged inside:

```text
logs/automation.log
```

Example:

```text
Website Opened
Login Successful
PIM Opened
Employee Added
Employee List Extracted
Excel Exported
Logout Successful
```

---

## Error Handling

The application handles:

* Login failures
* Element not found exceptions
* Timeout exceptions
* Browser launch failures
* Export failures

All exceptions are logged for troubleshooting.

---

## Assignment Requirements Covered

✔ Dashboard-driven automation

✔ Login using dashboard credentials

✔ Employee creation

✔ Employee verification

✔ Employee list extraction

✔ Dashboard result display

✔ Excel export

✔ Logging

✔ Exception handling

✔ FastAPI backend

✔ Selenium automation

---

## Author

**Abhishek Karale**

Python Developer | FastAPI | Django | Selenium | Automation | AI/ML Enthusiast
