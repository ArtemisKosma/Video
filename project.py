import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation

fig = plt.figure()  #ftiaxnei to figure
ax = plt.axes(xlim=(0, 10), ylim=(0, 10))   #ftiaxnei tous aksones x:[0,10] kai y:[0,10]

#orismos kentrou peristrofhs antikeimenwn
x_peristrofhs = 5   #tetmhmenh kentrou peristrofhs
y_peristrofhs = 5   #tetagmenh kentrou peristrofhs

#orismos aktinas peristrofhs antikeimenwn
#aktina_peristrofhs = 4

#orizei ton arithmo twn antikeimenwn
num_objects = 4

colors = ['r', 'b', 'g', 'y']   #some colors for the objects

values = [2, 1, 0, 3]

#orizei to plhthos twn frames gia to animation
num_of_frames = 360

#sunarthsh arxikopoihshs animation
def init():
    # arxikopoihsh adeias listas antikeimenwn
    return []

#sunarthsh gia to animation
def animate(i):
    #plt.cla()  #katharismos twn aksonwn apo prohgoumenes times
    objects = [] #arxikopoihsh adeias listas antikeimenwn
    r_circle = 0.45 #aktina kuklwn
    
    
        
    
    if(i >= 270):
        i = -i
    
    #domh epanalhpshs pou ftiaxnei kuklous pou kinountai se kuklikh troxia 
    #kai isapexoun metaksu tous, sthn sunexeia ta topothetei me thn bohtheia 
    #twn aksonwn sthn katallhlh thesh    
    for t in range(num_objects): 
            objects.append(ax.add_patch( plt.Circle((x_peristrofhs + animate.aktina_peristrofhs * np.sin(2 * t * np.pi/(num_objects) + np.radians(-i)), y_peristrofhs + animate.aktina_peristrofhs * np.cos(2 * t * np.pi/(num_objects) + np.radians(-i))),r_circle,color=colors[t % 4]) ))
    
    return objects

animate.z = 0
animate.aktina_peristrofhs = 1 #static metablhth ths sunarthshs animate

    
#klhsh sunarthshs gia na epiteuxthei to animation    
anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=num_of_frames, interval=20, blit=True)

#eksagwgh animation se video                               
anim.save("v2.mp4", fps=30)
