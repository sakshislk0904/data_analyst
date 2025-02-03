import matplotlib.pyplot as plt

days =["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
sales=[160,150,140,145,175,165,180]

plt.plot(days, sales, marker='o')
plt.title("sales over days")
plt.xlabel("days")
plt.ylabel("sales")
plt.show()