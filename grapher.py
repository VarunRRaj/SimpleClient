from collections import deque

import matplotlib.pyplot as plt
import matplotlib.animation as animation

import os

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

def animate(dataArray):
    pullData = os.popen('tail -n 4000 log.csv').read()
    dataArray = pullData.split('\n')
    xar = []
    yar = []
    for eachLine in dataArray:
        if len(eachLine)>1:
            y,x = eachLine.split(',')
            xar.append(x)
            yar.append(y)
        
    ax1.clear()
    ax1.plot(xar,yar)

ani = animation.FuncAnimation(fig, animate, interval = 1000)
plt.show()
