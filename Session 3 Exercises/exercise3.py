#Write a program that asks for the user’s score and prints a message based on the score.

score = int(input("Enter your score: "))
if score >= 90:
    print("Grade: Excellent")
elif score >= 75:
    print("Grade: Good")
elif score >= 50:
    print("Grade: Average")
else:
    print("Grade: Needs Improvement")
