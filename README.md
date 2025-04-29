# Empower_Hub
This project is a desktop-based Employee Management System built using **Python**, **CustomTkinter**, and **MySQL** for managing employee records such as name, phone, role, gender, and salary.

---

## ✅ Features
- Login screen with basic credential check
- Add new employees
- View all employees
- Search employee by any field
- Update employee information
- Delete a single or all employee records

---

## 🛠 Prerequisites
Make sure the following are installed:

### Software:
- Python 3.x
- MySQL Server (e.g., MySQL Workbench or XAMPP)

### Python Libraries:
```bash
pip install pymysql customtkinter Pillow
```

---

## 📂 Project Structure
Ensure all files are placed in the same folder:
```
project_folder/
├── login.py
├── employeemanagementsystem.py
├── database.py
├── backgroundimage.jpeg
├── office_style_image_930x158.png
```

---

## ⚙️ Database Setup
On first run, the program:
- Connects to MySQL using credentials (`root` / `1234@#aadi`)
- Creates a database `employee_data` (if it doesn't exist)
- Creates a table `data` to store employee records

> ⚠️ Change credentials in `database.py` if needed:
```python
conn = pymysql.connect(host='localhost', user='your_user', password='your_password')
```

---

## 🚀 How to Run
1. Start your MySQL server (e.g., via XAMPP or MySQL Workbench)
2. Run the login GUI:
```bash
python login.py
```
3. Enter credentials:
   - Username: `Aditya`
   - Password: `Aditya1234`

4. The main Employee Management System will open.

---

## 👤 ID Format
Employee ID must start with `EN`, e.g., `EN1`, `EN2`, etc.

---

## 🧠 Optional Improvements
- Use `and` in login check instead of `or` for better security
- Implement password encryption
- Add validation for fields like phone and salary
- Export/import data as CSV or Excel

---

## 📸 Screenshots

Login Page

![Screenshot (34)](https://github.com/user-attachments/assets/c90d0276-8be9-44e7-9ed7-de2d47c24869)

Dashboard

![Screenshot (35)](https://github.com/user-attachments/assets/2886ee92-21f6-4c37-823f-0dd32aeed8d1)

Data Insertion
![Screenshot (36)](https://github.com/user-attachments/assets/7dd705f4-05b9-460e-83c0-bb3ccf5a9aae)

Data Deletion
![Screenshot (37)](https://github.com/user-attachments/assets/e05b2f7a-75a5-4cdd-a740-4ecda67e5550)



