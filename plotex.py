from pylab import *
x = rand(20); y = rand(20)

subplot(211)
plot(x, y, 'r', lw=3)
scatter(x,y,s=120)

subplot(212)
plot(x, y, 'y', zorder=1, lw=3)
scatter(x,y,s=80, zorder=2)

# A new figure, with individually ordered items
x=frange(0,3*pi,npts=1000)
figure()
plot(x,sin(x),linewidth=10, color='black',label='zorder=10',zorder = 10)  # on top
plot(x,cos(1.3*x),linewidth=5, color='red', label='zorder=11',zorder = 11) # bottom
plot(x,sin(2.1*x),linewidth=3, color='green', label='zorder=3',zorder = 3)
axhline(0,linewidth=5, color='blue', label='zorder=2',zorder = 2)
l = legend()
l.set_zorder(50) # put the legend on top

show()				