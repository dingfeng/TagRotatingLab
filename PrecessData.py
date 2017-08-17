# -*- coding: UTF-8 -*-
# filename: PrecessData date: 2017/8/16 22:48  
# author: FD 

import numpy as np
import matplotlib.pyplot as plt
dir = './data'
axes = ['x', 'y', 'z']
axes_map = {}

for value in axes:
    axes_map[value]=[]
    angle = 0
    while angle < 360:
        filename = ''.join([dir,'/',value, '-', str(angle),'.csv'])
        angle += 30
        data = np.loadtxt(filename, delimiter=',', skiprows=1)
        data = data[:,5]
        phase_mean = np.average(data)
        axes_map[value].append(phase_mean)
x_value = [i for i in range(0,360,30)]
plt.figure()
plt.plot(x_value,axes_map['x'],'.')
plt.plot(x_value,axes_map['y'],'.')
plt.plot(x_value,axes_map['z'],'.')
plt.legend(['x','y','z'])
plt.show()

print u'横坐标'
print x_value
print u'纵坐标：'
print 'x: ',axes_map['x']
print 'y: ',axes_map['y']
print 'z: ',axes_map['z']