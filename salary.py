# Inputs
hours_per_week = int(input("Enter hour of work this week: "))

# Outputs
hours_worked = 0
standard_amount = 0
ovr_time_amount = 0
gross_pay = 0
total_tax = 0
net_pay = 0


# Constants
STA_WORK_WEEK = 39  # Standard hour working per week
STA_PAY_RATE = 35  # Standard pay rate per hour
OVER_TIME_PAY = 50  # 50 euro additional hour
VAT_RATE = 21  # 21% Vat Rate
YEARLY_SALARY = 18000

# Assumed Constants
WORKED_WEEK = 32   # Weeks in a year
OVER_TIME = 5  # 5 Hours overtime per week

# Algorithm


pay = STA_WORK_WEEK * STA_PAY_RATE
gross_per_year = pay * 52
annual_salary = gross_per_year

if YEARLY_SALARY <= annual_salary:
    hours_worked = hours_per_week
    standard_amount = hours_worked * STA_PAY_RATE
    ovr_time_amount = hours_worked * STA_PAY_RATE + OVER_TIME * OVER_TIME_PAY
    gross_pay = gross_per_year / WORKED_WEEK
else:
    total_tax = (gross_pay * 21) / 100
    net_pay = gross_pay - total_tax


# Results

print("Hours Worked:", hours_worked)
print("Standard Pay Amount:", standard_amount)
print("Over Time Pay Amount:", ovr_time_amount)
print("Your Gross:", gross_pay)
# print(total_tax)
# print(net_pay)