import matplotlib.pyplot as plt

subjects = ["DSA","web devlopment","SAD","AI"]
marks = [90,80,75,60]

plt.pie(marks, labels=subjects, startangle=90)
plt.title("marks in different subject")
plt.show()

print("sakshi")