#Input percentage and print remarks: Excellent / Very Good / Good / Average / Fail.
perc = float(input("Enter percentage: "))

if perc >= 90:
    remark = "Excellent"
elif perc >= 75:
    remark = "Very Good"
elif perc >= 60:
    remark = "Good"
elif perc>= 40:
    remark = "Average"
else:
    remark = "Fail"

print(remark)