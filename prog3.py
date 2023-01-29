# Program 3 UNIT 1
# ASTHA YADAV KMC PHYSICS HONORS

import math as m
import matplotlib.pyplot as plt
import numpy as np
import fontstyle as fs

print("\nLet's find out how far and high and object will go in a projectile. And how much time it will take.\nWe will use simple classical mechanics and the SI system, gravity = 9.8 metre per seconds square\n")
print("If you don't enter anything, default speed is 20 m/s, and angle 60 degrees.\n")
g = 9.8
o = str(input("\tWhat object would you like to throw? : ") or "object")
u = float(input("\tStarting speed of object in m/s : ") or "20")
ang = float(input("\tHow much angle in degrees you throw the object, with respect to horizontal axis: ") or "60")
a = m.radians(ang)

t = (2*u*m.sin(a))/g
h = (u*m.sin(a))**2/(2*g)
r = (u*u*m.sin(2*a))/g

t = round(t,2)
h = round(h,2)
r = round(r,2)
print("\n")
print(o.capitalize(),"will fly up high till",h,"meters, land",r,"meters far away and take",t,"seconds to do that.\n")
prompt = str(input("Ready to see the graph for it? Press Enter"))

# # # graph 

x = np.linspace(0,int(r+(r*0.2)),100) # start and end of x axis, number of parts its divided into
y = ((-4.9)*((x/(u*np.cos(a)))**2))+(np.tan(a)*x) # the equation

fig = plt.figure(figsize = (12,6)) # figure size of graph
#customizing the graph
plt.plot(x,y, alpha = 0.8, label = "Projectile Graph", color = 'purple', linestyle = "dashed", linewidth = 1.5)
plt.ylim(0,(h+(h*0.2))) # setting limit for y
plt.title('THE PATH OF THE %s' %o.upper())
plt.xlabel('R A N G E')
plt.ylabel('H E I G H T')

fig.text(0.65,0.75, "ASTHA YADAV PHY HONS KMC 2023", fontsize = 11, fontstyle='italic', family='serif', color = 'blue')
plt.grid(alpha = 0.5, linestyle = '--')
plt.legend()
plt.show()