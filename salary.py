if hours_worked <= STA_WORK_WEEK:  # If hours work is less than standard work hour
    standard_amount = STA_PAY_RATE * hours_worked
    gross_pay = standard_amount
    ovr_time_amount = 0         # there's no overtime
    if gross_pay > weekly_threshold:  # If gross pay is more than 18000 tax threshold
        total_tax = round((gross_pay - weekly_threshold) * TAX_RATE, 2)
    else:
        net_pay = gross_pay
else:                              # If there's overtime
    standard_amount = STA_PAY_RATE * STA_WORK_WEEK
    extra_hours = hours_worked - STA_WORK_WEEK  # Get extra hours work
    ovr_time_amount = extra_hours * OVER_TIME_PAY
    gross_pay = standard_amount + ovr_time_amount
    if gross_pay > weekly_threshold:
        total_tax = round((gross_pay - weekly_threshold) * TAX_RATE, 2)
        net_pay = gross_pay - total_tax
    else:
        net_pay = gross_pay