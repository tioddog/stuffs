# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math
#
#labels='frogs','hogs','dogs','logs'
#sizes=15,20,45,10
#colors='yellowgreen','gold','lightskyblue','lightcoral'
#explode=0,0.1,0,0
#plt.pie(sizes,explode=explode,labels=labels,colors=colors,autopct='%1.1f%%',shadow=True,startangle=50)
#plt.axis('equal')
#plt.show()
#
#
#x = np.linspace(0, 10, 1000)
#y = np.sin(x)
#z = np.cos(x**2)



dat = pd.read_csv("boe.csv", sep=",")

line_x = dat['x']
line_y = dat['y']
line_z = dat['z']

# plt.figure(figsize=(9,5))
# plt.plot(line_x, line_y, label="$boe crv$", color="gold", linewidth=2.5)
# plt.xlabel("xposition")
# plt.ylabel("yposition")
# plt.title("Original boe curv")
# plt.legend()
# plt.show()

#adaption to local section...

#exact local length
K = 5.6

#local A point coordination
Ax = 1.904129
Ay = 1.427906
Az = -0.03304653

#local B point coordination
Bx = 7.366
By = 1.439885
Bz = -0.03332581

k_line_x = K * line_x 
k_line_y = K * line_y
k_line_z = K * line_z

print('the minimum index')
print(k_line_x.idxmin())
print(k_line_x.iloc[k_line_x.idxmin()])
print(k_line_y.iloc[k_line_y.idxmin()])
print(k_line_z.iloc[k_line_z.idxmin()])

leftest_x = k_line_x.iloc[k_line_x.idxmin()]
leftest_y = k_line_y.iloc[k_line_x.idxmin()]
leftest_z = k_line_z.iloc[k_line_x.idxmin()]




plt.figure(figsize=(9,5))
ax = plt.gca()
# ax.set_aspect('equal')


#plot A point
plt.scatter(Ax,Ay,label="A point", color="red", marker="p")

#plot B point
plt.scatter(Bx,By,label="B point", color="blue", marker="p")

#move to the B point

translation_x = Bx - k_line_x.iloc[0]
translation_y = By - k_line_y.iloc[0]

k_line_x = k_line_x + translation_x
k_line_y = k_line_y + translation_y



#calculate intial angle phi for each position
delta_y = k_line_y - By
delta_x = k_line_x - Bx
delta_dist = np.sqrt(delta_x * delta_x + delta_y * delta_y)
# phi = np.arctan(np.nan_to_num(delta_y / delta_x))
phi = np.arctan(delta_y / delta_x)

print(phi.size)
print(phi.iloc[0])

print(phi.iloc[-1])


print('distance between b and 0')
print(Bx-k_line_x.iloc[0])
print(By-k_line_y.iloc[0])


#here you input the desired angle changement
theta = math.pi/200 + math.pi
# theta is a positive value

phi_new = phi - theta
k_line_x = Bx + abs(delta_x) * np.cos(phi_new)
k_line_y = By + abs(delta_x) * np.sin(phi_new)










#plot k'ed airfoil boe
plt.plot(k_line_x, k_line_y, label="$k_boe crv$", color="green", linewidth=2.5)
plt.scatter(k_line_x, k_line_y, marker='x', color='blue', alpha=0.7, label='pnts on crv')



plt.xlabel("xposition")
plt.ylabel("yposition")
plt.title("crvs and pnts")
plt.legend()
plt.show()

