hours_worked = int(input("Enter hour of work this week: "))

# Outputs
standard_amount = 0
ovr_time_amount = 0
gross_pay = 0
total_tax = 0
net_pay = 0


# Constants
STA_WORK_WEEK = 39 # Standard hour working per week
STA_PAY_RATE = 35 # Standard pay rate per hour
OVER_TIME_PAY = 50 # 50 euro additional hour
TAX_RATE = 0.21  # 21% Vat Rate
YEARLY_SALARY = 18000

# Assumed Constants
WORKED_WEEK = 52   # Weeks in a year
OVER_TIME = 1 # 1 Hour

# Algorithm

standard_amount = STA_PAY_RATE * hours_worked

ovr_time_amount = OVER_TIME * OVER_TIME_PAY


weekly_pay = standard_amount + ovr_time_amount  # Before Tax
weekly_tax = weekly_pay * TAX_RATE  # After Tax

yearly_pay = weekly_pay * WORKED_WEEK     # Annual Salary
over_threshold = yearly_pay / WORKED_WEEK  # Need Tax
print(over_threshold)

tax_threshold = round(YEARLY_SALARY / WORKED_WEEK)  # No Tax
print(tax_threshold)


if OVER_TIME:
    gross_pay = standard_amount + ovr_time_amount
    if gross_pay > tax_threshold:
        total_tax = (gross_pay - tax_threshold) * TAX_RATE
        net_pay = gross_pay - total_tax
    else:
        total_tax = 0

else:
    gross_pay = standard_amount - ovr_time_amount
    if gross_pay > tax_threshold:
        total_tax = (gross_pay - tax_threshold) * TAX_RATE
        net_pay = gross_pay - total_tax
    else:
        total_tax = 0


print("Hours Worked :", hours_worked)
print("Standard Amount :", standard_amount)
print("Over Time Amount :", ovr_time_amount)
print("Gross Pay:", gross_pay)
print("Total Tax :", total_tax)
print("Your Net Pay :", net_pay)