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
