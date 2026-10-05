import numpy as np

np.random.seed(42)

employees = np.array(
    [
        "Aarav",
        "Bibek",
        "Carlos",
        "Diana",
        "Emma",
        "Frank",
        "Grace",
        "Hari",
        "Ishan",
        "Jessica",
    ]
)

departments = np.array(
    ["IT", "HR", "IT", "Finance", "Marketing", "IT", "HR", "Finance", "IT", "Marketing"]
)

salaries = np.array(
    [45000, 52000, 68000, 60000, 48000, 75000, 55000, 62000, 80000, 51000]
)

performance = np.array([72, 85, 91, 78, 69, 95, 88, 74, 98, 81])

experience = np.array([2, 4, 7, 5, 2, 9, 6, 4, 10, 3])
total_employees = employees.shape[0]
# finding average salary
average_salary = np.mean(salaries)
# finding median of the salary
median_salary = np.median(salaries)
# finding highest salary
highest_salary = np.max(salaries)
# finding lowest salary
lowest_salary = np.min(salaries)
# salary standard deviation
salary_sd = np.std(salaries)
# finding highest paid employee
index_of_highest_salary = np.argmax(salaries)
highest_paid_employee = employees[index_of_highest_salary]
# finding lowest paid employee
index_of_lowest_salary = np.argmin(salaries)
lowest_paid_employee = employees[index_of_lowest_salary]
employees_earning_more_than_60k_boolean = salaries > 60000
employees_earning_more_than_60k = employees[employees_earning_more_than_60k_boolean]
salary_of_employee_earning_more_than_60k = salaries[
    employees_earning_more_than_60k_boolean
]
high_performance = performance > 90
high_performance_name = employees[high_performance]  # people with 90 above performance
high_performance_performance = performance[high_performance]
high_performance_salary = salaries[high_performance]
high_exp = experience > 5
employee_with_60k_and_performance_85 = (salaries > 60000) & (performance >= 85)
performance_category = np.where(
    performance >= 90,
    "Excellent",
    (
        np.where(
            performance >= 80,
            "Good",
            (np.where(performance >= 70, "Try Hard", "Keep going")),
        )
    ),
)
# giving 10% salary increase
new_salaries = salaries * 1.10
salary_difference = new_salaries - salaries
salary_order = np.argsort(salaries)
sorted_employee = employees[salary_order]
sorted_salary = salaries[salary_order]
print(f"""========================================
       EMPLOYEE ANALYSIS REPORT
========================================\n
Total Employees :{total_employees}\n
Average Salary : {average_salary}\n
Median Salary : {median_salary}\n
Highest Salary : {highest_salary}\n
Lowest Salary : {lowest_salary}\n
Salary Standard Deviation : {salary_sd}\n
----------------------------------------
HIGHEST PAID EMPLOYEE
----------------------------------------
Name : {highest_paid_employee}\n
Salary: {salaries[index_of_highest_salary]}\n
Department : {departments[index_of_highest_salary]}\n
Performance : {performance[index_of_highest_salary]}\n
Experience : {experience[index_of_highest_salary]}""")
print("""----------------------------------------
HIGH PERFORMERS
----------------------------------------""")
for name, salary, perform in zip(
    high_performance_name, high_performance_salary, high_performance_performance
):
    print(f"Name : {name} \nSalary : {salary} \nPerformance : {perform}")
print("""----------------------------------------
SALARY ANALYSIS
----------------------------------------\n""")
print("Employees earning above $60,000 :\n")
for high_salary_name, high_salary_salary in zip(
    employees_earning_more_than_60k, salary_of_employee_earning_more_than_60k
):
    print(f"Name : {high_salary_name}\n Salary : {high_salary_salary}")
print("""----------------------------------------
PERFORMANCE CATEGORIES
----------------------------------------""")
for name, remark in zip(employees, performance_category):
    print(f"{name} - {remark}")
print("""----------------------------------------
SORTED EMPLOYEES BY SALARY
----------------------------------------""")
for sorted_name, sorted_income in zip(sorted_employee, sorted_salary):
    print(f"Name : {sorted_name}\n Salary : {sorted_income}")
