import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import random

IMG_W=54
IMG_H=54

UPPER_TOP=(19,22)
UPPER_BOTTOM=(28,41)
UPPER_BLEND=(23,27)
UPPER_HT=14

LOWER_TOP=(19,22)
LOWER_BOTTOM=(28,41)
LOWER_BLEND=(23,27)
LOWER_HT=6

maps={}
keys=["S212_1","S212_2","S212_3","S212_4","S212_5","S216_1","S216_2","S216_3","S216_4","S216_5","S202_1","S202_2","S202_3","S202_4","S202_5","S206_1","S206_2","S206_3","S206_4","S206_5","S105_1","S105_2","S105_3","S102_1","S102_2","S102_3","S112_1","S112_2","S112_3","S115_1","S115_2","S115_3","SSL_1","SSL_2","SSL_3","SSL_4","SSL_5","SSR_1","SSR_2","SSR_3","SSR_4","SSR_5"]

#Left Upper

maps["S212_1"] = np.zeros((IMG_H,IMG_W))
maps["S212_1"][9:23,0:2] = 1.
maps["S212_1"][20:31,0:2] = 0.5
        
maps["S212_2"] = np.zeros((IMG_H,IMG_W))
maps["S212_2"][9:23,2:5] = 1.
maps["S212_2"][20:31,2:5] = 0.5

maps["S212_3"] = np.zeros((IMG_H,IMG_W))
maps["S212_3"][9:23,5:8] = 1.
maps["S212_3"][20:31,5:8] = 0.5

maps["S212_4"] = np.zeros((IMG_H,IMG_W))
maps["S212_4"][9:23,8:11] = 1.
maps["S212_4"][20:31,8:11] = 0.5

maps["S212_5"] = np.zeros((IMG_H,IMG_W))
maps["S212_5"][9:23,11:14] = 1.
maps["S212_5"][20:31,11:14] = 0.5

maps["S216_1"] = np.zeros((IMG_H,IMG_W))
maps["S216_1"][28:42,0:2] = 1.
maps["S216_1"][20:31,0:2] = 0.5
        
maps["S216_2"] = np.zeros((IMG_H,IMG_W))
maps["S216_2"][28:42,2:5] = 1.
maps["S216_2"][20:31,2:5] = 0.5

maps["S216_3"] = np.zeros((IMG_H,IMG_W))
maps["S216_3"][28:42,5:8] = 1.
maps["S216_3"][20:31,5:8] = 0.5

maps["S216_4"] = np.zeros((IMG_H,IMG_W))
maps["S216_4"][28:42,8:11] = 1.
maps["S216_4"][20:31,8:11] = 0.5

maps["S216_5"] = np.zeros((IMG_H,IMG_W))
maps["S216_5"][28:42,11:14] = 1.
maps["S216_5"][20:31,11:14] = 0.5


# Right Upper

maps["S206_1"] = np.zeros((IMG_H,IMG_W))
maps["S206_1"][9:23,-2:] = 1.
maps["S206_1"][20:31,-2:] = 0.5
        
maps["S206_2"] = np.zeros((IMG_H,IMG_W))
maps["S206_2"][9:23,-5:-2] = 1.
maps["S206_2"][20:31,-5:-2] = 0.5

maps["S206_3"] = np.zeros((IMG_H,IMG_W))
maps["S206_3"][9:23,-8:-5] = 1.
maps["S206_3"][20:31,-8:-5] = 0.5

maps["S206_4"] = np.zeros((IMG_H,IMG_W))
maps["S206_4"][9:23,-11:-8] = 1.
maps["S206_4"][20:31,-11:-8] = 0.5

maps["S206_5"] = np.zeros((IMG_H,IMG_W))
maps["S206_5"][9:23,-14:-11] = 1.
maps["S206_5"][20:31,-14:-11] = 0.5

maps["S202_1"] = np.zeros((IMG_H,IMG_W))
maps["S202_1"][28:42,-2:] = 1.
maps["S202_1"][20:31,-2:] = 0.5
        
maps["S202_2"] = np.zeros((IMG_H,IMG_W))
maps["S202_2"][28:42,-5:-2] = 1.
maps["S202_2"][20:31,-5:-2] = 0.5

maps["S202_3"] = np.zeros((IMG_H,IMG_W))
maps["S202_3"][28:42,-8:-5] = 1.
maps["S202_3"][20:31,-8:-5] = 0.5

maps["S202_4"] = np.zeros((IMG_H,IMG_W))
maps["S202_4"][28:42,-11:-8] = 1.
maps["S202_4"][20:31,-11:-8] = 0.5

maps["S202_5"] = np.zeros((IMG_H,IMG_W))
maps["S202_5"][28:42,-14:-11] = 1.
maps["S202_5"][20:31,-14:-11] = 0.5


# Right Lower

maps["S105_1"] = np.zeros((IMG_H,IMG_W))
maps["S105_1"][12:23,-16:-14] = 1.
maps["S105_1"][23:28,-16:-14] = 0.5
        
maps["S105_2"] = np.zeros((IMG_H,IMG_W))
maps["S105_2"][12:23,-18:-16] = 1.
maps["S105_2"][23:28,-18:-16] = 0.5

maps["S105_3"] = np.zeros((IMG_H,IMG_W))
maps["S105_3"][12:23,-20:-18] = 1.
maps["S105_3"][23:28,-20:-18] = 0.5

maps["S102_1"] = np.zeros((IMG_H,IMG_W))
maps["S102_1"][28:39,-16:-14] = 1.
maps["S102_1"][23:28,-16:-14] = 0.5
        
maps["S102_2"] = np.zeros((IMG_H,IMG_W))
maps["S102_2"][28:39,-18:-16] = 1.
maps["S102_2"][23:28,-18:-16] = 0.5

maps["S102_3"] = np.zeros((IMG_H,IMG_W))
maps["S102_3"][28:39,-20:-18] = 1.
maps["S102_3"][23:28,-20:-18] = 0.5



# Left Lower

maps["S112_1"] = np.zeros((IMG_H,IMG_W))
maps["S112_1"][12:23,14:16] = 1.
maps["S112_1"][23:28,14:16] = 0.5
        
maps["S112_2"] = np.zeros((IMG_H,IMG_W))
maps["S112_2"][12:23,16:18] = 1.
maps["S112_2"][23:28,16:18] = 0.5

maps["S112_3"] = np.zeros((IMG_H,IMG_W))
maps["S112_3"][12:23,18:20] = 1.
maps["S112_3"][23:28,18:20] = 0.5

maps["S115_1"] = np.zeros((IMG_H,IMG_W))
maps["S115_1"][28:39,14:16] = 1.
maps["S115_1"][23:28,14:16] = 0.5
        
maps["S115_2"] = np.zeros((IMG_H,IMG_W))
maps["S115_2"][28:39,16:18] = 1.
maps["S115_2"][23:28,16:18] = 0.5

maps["S115_3"] = np.zeros((IMG_H,IMG_W))
maps["S115_3"][28:39,18:20] = 1.
maps["S115_3"][23:28,18:20] = 0.5


# SSL

maps["SSL_1"] = np.zeros((IMG_H,IMG_W))
maps["SSL_1"][0:2,18:25] = 1.
maps["SSL_1"][0:2,25:29] = 0.5

maps["SSL_2"] = np.zeros((IMG_H,IMG_W))
maps["SSL_2"][2:4,18:25] = 1.
maps["SSL_2"][2:4,25:29] = 0.5

maps["SSL_3"] = np.zeros((IMG_H,IMG_W))
maps["SSL_3"][4:6,18:25] = 1.
maps["SSL_3"][4:6,25:29] = 0.5

maps["SSL_4"] = np.zeros((IMG_H,IMG_W))
maps["SSL_4"][6:8,18:25] = 1.
maps["SSL_4"][6:8,25:29] = 0.5

maps["SSL_5"] = np.zeros((IMG_H,IMG_W))
maps["SSL_5"][8:11,18:25] = 1.
maps["SSL_5"][8:11,25:29] = 0.5



# SSR

maps["SSR_1"] = np.zeros((IMG_H,IMG_W))
maps["SSR_1"][0:2,-26:-18] = 1.
maps["SSR_1"][0:2,25:29] = 0.5

maps["SSR_2"] = np.zeros((IMG_H,IMG_W))
maps["SSR_2"][2:4,-26:-18] = 1.
maps["SSR_2"][2:4,25:29] = 0.5

maps["SSR_3"] = np.zeros((IMG_H,IMG_W))
maps["SSR_3"][4:6,-26:-18] = 1.
maps["SSR_3"][4:6,25:29] = 0.5

maps["SSR_4"] = np.zeros((IMG_H,IMG_W))
maps["SSR_4"][6:8,-26:-18] = 1.
maps["SSR_4"][6:8,25:29] = 0.5

maps["SSR_5"] = np.zeros((IMG_H,IMG_W))
maps["SSR_5"][8:11,-26:-18] = 1.
maps["SSR_5"][8:11,25:29] = 0.5


all_maps = np.zeros((IMG_H,IMG_W))

for s in keys:
    all_maps += (99.+random.random()*20.)*maps[s]

all_maps[all_maps == 0.] = 'nan'

img = plt.imread("analysis/RAC2.png")
fig, ax = plt.subplots()
mat = ax.matshow(all_maps, vmin=90, vmax=120, alpha=1, cmap="Reds")
plt.axis('off')
cbar = plt.colorbar(mat)
cbar.set_label('Noise Levels (dB)', labelpad=20,rotation=270)
plt.savefig("analysis/no_backdrop.png")
plt.show()
plt.clf()

fig2, ax2 = plt.subplots()
ax2.imshow(img)
mat2 = ax2.matshow(all_maps, vmin=90, vmax=120, alpha=0.75, cmap="Reds")
plt.axis('off')
cbar = plt.colorbar(mat2)
cbar.set_label('Noise Levels (dB)', labelpad=20,rotation=270)
plt.savefig("analysis/with_backdrop.png")
plt.show()
