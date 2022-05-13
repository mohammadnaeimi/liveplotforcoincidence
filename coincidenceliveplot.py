import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import random
from time import sleep
import numpy as np
import TimeTagger
from TimeTagger import Countrate, Coincidence, createTimeTagger

style.use('fivethirtyeight')

obj_tagg = createTimeTagger()
obj_tagg.reset()
obj_tagg.setTriggerLevel(1, 0.5)
obj_tagg.setTriggerLevel(2, 0.5)
obj_tagg.sync()
sleep(0.5)
coin_window = 6700
coin_rate = Coincidence(obj_tagg, channels= [1, 2], coincidenceWindow= coin_window)


def data_aq():
    return 3500 + float(random.randint(-10,10)) / 10.0

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)
x = []
y = []
i = 0
while True:
    i += 1
    x.append(i)
    ans = Countrate(obj_tagg, channels= [1, 2, coin_rate.getChannel()])
    res_list = ans.getData()
    y.append(res_list[2])
    ax1.clear()
    ax1.plot(x, y, linewidth= 0.9)
    plt.pause(0.1)

plt.show()