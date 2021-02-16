import csv

import matplotlib.pyplot as plt


USE_INFLATION_AND_INCREASE = True
YEARLY_INFLATION_RATE = 1.5 / 100
YEARLY_SALARY_INCREASE_RATE = 1 / 100

TAX_GROUP = "I"  # I = Single | III = Married
SAVINGS_PERCENTAGE = 30 / 100

USE_INVESTMENTS = True
YEARLY_INTEREST = 3 / 100

IS_NETTO = True
IS_ACCUMULATED = True

IDADE_INICIAL = 23

IS_WITHDRAW = False
WITHDRAW_AMMOUNT = 200000


with open("arzt_gehalt.csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    csv_list = list(csv_reader)

if TAX_GROUP == "I":
    csv_list = csv_list[:40]
else:
    csv_list = csv_list[40:]

yearly_salary_list = []


for i in range(len(csv_list)):
    if IS_NETTO:
        yearly_salary_list.append(float(csv_list[i][3]) * 12)
    else:
        yearly_salary_list.append(float(csv_list[i][2]) * 12)


accumulated_list = []
accumulated_salary = 0
current_salary = 0
k = 0

for i in range(len(yearly_salary_list)):
    if USE_INFLATION_AND_INCREASE:
        current_salary = yearly_salary_list[i] * (1 + YEARLY_SALARY_INCREASE_RATE)
        accumulated_salary = accumulated_salary - (
            accumulated_salary * YEARLY_INFLATION_RATE
        )

    if USE_INVESTMENTS:
        accumulated_salary = accumulated_salary * (1 + YEARLY_INTEREST)

    accumulated_salary = (current_salary * SAVINGS_PERCENTAGE) + accumulated_salary

    if IS_WITHDRAW:
        if k == 0:
            if accumulated_salary >= WITHDRAW_AMMOUNT:
                accumulated_salary = accumulated_salary - WITHDRAW_AMMOUNT
                k = k + 1

    accumulated_list.append(round(accumulated_salary))

one_to_forty = []

for i in range(40):
    one_to_forty.append(str(i + 1 + IDADE_INICIAL))

monthly_salary_list = []

for i in range(len(yearly_salary_list)):
    monthly_salary_list.append(yearly_salary_list[i] / 12)

if IS_ACCUMULATED:
    x = one_to_forty
    y = accumulated_list

    plt.figure(figsize=(5, 3), dpi=100)
    plt.plot(x, y)

    plt.title("Accumulated Salary")
    plt.xlabel("Age")
    plt.ylabel("Total (€)")

    plt.show()

else:
    x = one_to_forty
    y = monthly_salary_list

    plt.figure(figsize=(5, 3), dpi=100)
    plt.plot(x, y)

    plt.title("Monthly salary")
    plt.xlabel("Age")
    plt.ylabel("Total (€)")

    plt.show()


end = input()
