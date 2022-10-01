#budget
import matplotlib.pyplot as plt
import numpy as np
import sys

#Income
i_crypto = int(input("Crypto profit this month"))
i_job = int(input("Job income"))
i_misc = int(input('Misc income'))
e_net = int(input('What are your total expense this month'))
i_total = i_crypto + i_job + i_misc
print('Your total income this month',i_total)

# Pie chart, where the slices will be ordered and plotted counter-clockwise:
labels = 'Crypto', 'Job', 'Misc'
sizes = [i_crypto, i_job, i_misc]
explode = (0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()

#Savings
s_crypto = 620
s_cash = 450
s_bank = 600
s_net = s_crypto + s_cash + s_bank + i_total
print("Your total savings is",s_net)

#Savings Pie Graph
labels = 'Crypto', 'Cash', 'Bank'
sizes = [s_crypto, s_cash, s_bank]
explode = (0, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()


#Expenses
print('Total expenses:',e_net)

#Net money
n_all = s_net - e_net
n_tm = i_total - e_net
print('Net this month',n_tm)

#comparison
lm_net = 1500
n_all

#Comparison chart
fig, ax = plt.subplots()

fruits = ['September', 'October']
counts = [lm_net,n_all]
bar_labels = ['red', 'blue',]
bar_colors = ['tab:red', 'tab:blue']

ax.bar(fruits, counts, label=bar_labels, color=bar_colors)

ax.set_ylabel('Savings')
ax.set_title('Savings per month')
ax.legend(title='Month color')

plt.show()
