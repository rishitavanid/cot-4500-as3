# Numerical Methods for Differential Equations (Assignment 3a)

**Assignment 3a**, solves **differential equations** using two fundamental numerical methods:

✔ **Euler's Method** – a simple but effective approach for solving ODEs.  
✔ **Runge-Kutta (RK4) Method** – a higher-order method providing improved accuracy.

This project requires implementing these methods **from scratch** (without using SciPy) and ensuring the expected results are obtained.

---

## **Project Overview**
This assignment focuses on **solving the following ordinary differential equation (ODE):**

\[
dy/dt = t - y^2
\]

over the range **0 < t < 2**, with the initial condition **f(0) = 1**.

We'll approximate the solution using:
- **Euler's Method** (1st order accuracy)
- **Runge-Kutta Method (RK4)** (4th order accuracy)

The goal is to compute and verify the numerical solutions using **10 iterations** for each method.

---

## **Project Structure**
Project should be organized in the following structure:

```
cot-4500-as3/
│-- src/
│   │-- main/
│   │   │-- __init__.py
│   │   │-- assignment_3.py  # Main implementation of Euler & RK4 methods
│   │-- test/
│   │   │-- __init__.py
│   │   │-- test_assignment_3.py  # Unit tests for verifying correctness
│-- requirements.txt  # Dependencies (NumPy only)
│-- README.md  
```

### **What’s Inside?**
✔ `assignment_3.py` → The core implementation of **Euler & RK4** methods.  
✔ `test_assignment_3.py` → Unit tests to **ensure correctness**.  
✔ `requirements.txt` → The only external library needed is **NumPy**.  
✔ `README.md` → This file! **guide** to the project.

---

## **How to Run the Code**

### **1) Install Dependencies**
Ensure you have NumPy installed before running the code:
```sh
pip install -r requirements.txt
```

### **2) Run the Main Code**
To execute the numerical methods and view the computed values:
```sh
python src/main/assignment_3.py
```

### **3)Run the Tests**
To verify that the methods are correctly implemented, run:
```sh
python -m unittest discover -s src/test
```
If everything is correct, you’ll see:
```sh
Ran 2 tests in 0.001s

OK

Process finished with exit code 0
```
If errors occur, review your implementation carefully!

---

## **Expected Output**
After running `assignment_3.py`, you should see the following output:
```sh
Euler Method Result: 1.2446380979332121
Runge-Kutta Method Result: 1.251316587879806
```
These values align with the expected results from the assignment.

---

## **Restrictions**
- **Do NOT** use the SciPy library. You must implement the numerical methods manually.
- Ensure that your results match the expected output.
- Follow the required project structure strictly.

---

## **About This Project**
This assignment is part of **Numerical Calculus**, emphasizing practical numerical methods for solving differential equations. By implementing these methods, you will gain insights into numerical accuracy, step-size sensitivity, and stability considerations.

---

## **Final Checklist**
✔ Project files are structured correctly.  
✔ Euler & RK4 methods are properly implemented.  
✔ Test cases successfully pass.  
✔ README includes clear and detailed instructions.  
✔ Output matches expected values.

---

## **Need Help?**
If you encounter issues:
- Double-check the project structure.
- Ensure NumPy is installed.
- Verify that your implementation follows the provided equations and logic.
- Run the tests and debug as needed.

---

## **Final Words**
This project offers valuable hands-on experience with numerical methods for ODEs. 
