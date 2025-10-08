print("welcome to calorie meter")
print("track your meal calories and compare against your daily limit ")

meals=[]
calories=[]
num_meals=int(input("enter the number meal you taken:"))

for i in range(num_meals):
    meal_name=input(f"enter {i+1}th meals name:")
    cal =float(input(f"enter calories for {meal_name}:"))
    meals.append(meal_name)
    calories.append(cal)
    
total_calories=sum(calories)
avg_calories=total_calories/ num_meals

daily_limit=float(input("enter your daily calorie limit:"))

for i in range(num_meals):
    print(f"{meals[i]}:{calories[i]} calories")
    print(f"daily limit: {daily_limit}")
    
if total_calories >daily_limit:
    print(f"warning: you have exceeded your daily calorie limit{total_calories - daily_limit}")
    
else :
    print(f"You have got  calories left for the day.{daily_limit - total_calories}")