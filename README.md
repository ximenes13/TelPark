# 🚗 Telpark Automation Testing

Automated UI tests using Python, Selenium, and Pytest for core user actions on the [Telpark web application](https://app.telpark.com).  
This project was developed as part of a learning experience for automation tests.

---

## 🧪 Features Tested

This test suite currently includes:

- ✅ **Successful Login**  
- ❌ **Unsuccessful Login** *(intentional failure test)*  
- ➕ **Add a New Vehicle**  
- 🗑️ **Delete a Vehicle**

---

## 🛠️ Technologies Used

- **Python 3.10+**
- **Selenium WebDriver** – for browser automation
- **Pytest** – for structuring and running test cases
- **PyCharm** – development environment
- **Google Chrome** + **Chromedriver**

---

## 📂 Project Structure

- **test_login.py**  
  🔐 Tests valid and invalid login scenarios  
  🕵️ Uses `WebDriverWait` for reliable element access  
  🧪 Validates page titles, UI feedback, and error messages

- **test_vehicle.py**  
  ➕ Adds a new vehicle to the user profile  
  🗑️ Removes an existing vehicle  
  ♻️ Reuses session via login fixture  
  ⏱️ Avoids `sleep()` in favor of explicit waits

---

## 🛠️ Setup

### Step 1: Clone the Repository

To get started, clone this repository to your local machine using the following command:

`git clone https://github.com/your-username/TelPark.git`

### Step 2: Dependencies

Make sure you have Python 3.x installed. You can check your version with:

`python3 --version`

Install Selenium and pytest as well:

`pip install selenium` <br>
`pip install pytest`

### Step 3: Run the project

Once you've installed the dependencies, you can run both Python scripts to check the automation tests for login and vechiles.

`python3 login_test.py` <br>
`python3 vehicle_test.py`

---

# 🤝 Contributing

Contributions are welcome! If you'd like to improve the project, feel free to:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-name`).
3. Make your changes and commit them (`git commit -m 'Add new feature'`).
4. Push to your branch (`git push origin feature-name`).
5. Submit a pull request.

If you find bugs or have feature requests, please [open an issue](https://github.com/ximenes13/Calculator/issues).
