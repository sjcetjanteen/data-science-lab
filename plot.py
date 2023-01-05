from matplotlib import pyplot as plt
x=['mon','tues','wed','thurs','fri']
y=[300,450,150,400,650]
plt.subplot(2,1,1)
plt.xlabel('day')
plt.ylabel('drinks')
plt.title('sales details')
plt.plot(x,y,color='cyan',linestyle='dotted',marker='d',markerfacecolor='green',markeredgecolor='red')
plt.grid(color='blue',linestyle='dotted')

x=['mon','tues','wed','thurs','fri']
y=[400,500,350,300,500]

plt.subplot(2,1,2)
plt.xlabel('day')
plt.ylabel('food')
plt.title('food details')
plt.plot(x,y,linestyle='dashed',color='yellow',marker='h',markerfacecolor='magenta',markeredgecolor='black')
plt.grid(color='blue',linestyle='dotted')
plt.show()