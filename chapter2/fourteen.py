age_in_years = int(input("Enter age in years: "))

maximum_heart_rate_per_minute = 200 - age_in_years
print("user maximum heart rate is", maximum_heart_rate_per_minute)
target_heart_rate = 50/100 * maximum_heart_rate_per_minute and 85/100 * maximum_heart_rate_per_minute

if (50/100 * maximum_heart_rate_per_minute <= 85/100 * maximum_heart_rate_per_minute):
    print("Your heart rate is pretty much okay")
else:
    print("consult your Doctor ")
76