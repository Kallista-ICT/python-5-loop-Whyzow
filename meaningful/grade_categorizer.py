students = int(input("How many students? "))   # ask the amount of student
num = []

# Collect the students scores
for i in range(students):
    score = int(input(f"Enter score for student {i + 1}: "))
    num.append(score)

# Display the scores
print("\nStudent Scores and Categories:")
for scores in num:  # Classify the catogories
    if scores == 100:
        categories = "Perfect"
    elif scores >= 90:
        categories = "Excellent"
    elif scores >= 70:
        categories = "Average"
    elif scores >= 50:
        categories = "Bad"
    else:
        categories = "Disaster"    
    
    print(f"{scores} -> {categories}")

 

