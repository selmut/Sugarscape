from PIL import Image
import matplotlib.pyplot as plt
import glob
import os
import numpy as np


# plots a given generation's grid matrix and saves the image
def plot_living_area(area, agents_x, agents_y, img_loc, t):
    fig = plt.figure()
    plt.imshow(area, cmap='Greys', vmax=5)
    plt.scatter(agents_x, agents_y, c='black', s=10)
    plt.xticks([])
    plt.yticks([])
    plt.title('Time step: '+str(t))
    plt.savefig(img_loc + '/sugarscape_'+str(t)+'.png')
    plt.close(fig)


def scatter_agents(agents_x, agents_y, img_loc, t):
    fig = plt.figure()
    #plt.style.use('dark_background')
    plt.scatter(agents_x, agents_y, c='mediumslateblue', s=30, alpha=1, edgecolors='darkslateblue', linewidths=0.1)
    plt.xticks([])
    plt.yticks([])
    plt.title('Time step: '+str(t))
    plt.savefig(img_loc + '/living_area_'+str(t)+'.png')
    plt.close(fig)


def plot_vision_hist(visions_dict0, visions_dict_end):
    visions0 = list(visions_dict0.keys())
    n0 = visions_dict0.values()

    visions_end = list(visions_dict_end.keys())
    n_end = visions_dict_end.values()

    plt.figure()
    plt.title('Vision distribution')
    plt.ylabel('n')
    plt.xlabel('Vision')
    plt.bar(visions0, n0, color='mediumslateblue')
    plt.bar(visions_end, n_end, color='mediumvioletred')
    plt.legend(['Initial', 'Final'])
    plt.savefig('graphics/img/distributions/visions.png')


def plot_sugar_hist(sugar0_dict, sugar20_dict, sugar40_dict, sugar60_dict, sugar80_dict):
    sugar0 = list(sugar0_dict.keys())
    sugar20 = list(sugar20_dict.keys())
    sugar40 = list(sugar40_dict.keys())
    sugar60 = list(sugar60_dict.keys())
    sugar80 = list(sugar80_dict.keys())

    n0 = sugar0_dict.values()
    n20 = sugar20_dict.values()
    n40 = sugar40_dict.values()
    n60 = sugar60_dict.values()
    n80 = sugar80_dict.values()

    fig = plt.figure()
    plt.title('Wealth distribution')
    plt.ylabel('n')
    plt.xlabel('Wealth')

    plt.bar(sugar0, n0, color='mediumslateblue')
    plt.bar(sugar20, n20, color='greenyellow')
    plt.bar(sugar40, n40, color='turquoise')
    plt.bar(sugar60, n60, color='orange')
    plt.bar(sugar80, n80, color='mediumvioletred')
    plt.legend(['t=0', 't=20', 't=40', 't=60', 't=80'])
    plt.savefig('graphics/img/distributions/sugar.png')
    plt.close(fig)


def plot_lorentz(lorentz0, lorentz20, lorentz40, lorentz60, lorentz80):
    indexes0 = np.arange(0, len(lorentz0), step=1)
    indexes20 = np.arange(0, len(lorentz20), step=1)
    indexes40 = np.arange(0, len(lorentz40), step=1)
    indexes60 = np.arange(0, len(lorentz60), step=1)
    indexes80 = np.arange(0, len(lorentz80), step=1)

    fig = plt.figure()
    plt.plot(indexes0/indexes0[-1], lorentz0/lorentz0[-1], color='mediumslateblue')
    plt.plot(indexes20/indexes20[-1], lorentz20/lorentz20[-1], color='greenyellow')
    plt.plot(indexes40/indexes40[-1], lorentz40/lorentz40[-1], color='turquoise')
    plt.plot(indexes60/indexes60[-1], lorentz60/lorentz60[-1], color='orange')
    plt.plot(indexes80/indexes80[-1], lorentz80/lorentz80[-1], color='mediumvioletred')
    plt.xlabel('$F_i/Q$')
    plt.ylabel('$L_i/Q$')
    plt.title('Lorentz curve')
    plt.legend(['t=0', 't=20', 't=40', 't=60', 't=80'])
    plt.savefig('graphics/img/distributions/lorentz.png')
    plt.close(fig)


def plot_gini(gini, timeSteps):
    indexes = np.arange(0, timeSteps, step=1)

    fig = plt.figure()
    plt.plot(indexes, gini, color='mediumslateblue')
    plt.xlabel('$n$')
    plt.ylabel('$G(n)$')
    plt.title('Gini coefficient (without inheritance)')
    plt.savefig('graphics/img/distributions/gini.png')
    plt.close(fig)

def plot_meta_hist(meta_dict0, meta_dict_end):
    visions0 = list(meta_dict0.keys())
    n0 = meta_dict0.values()

    visions_end = list(meta_dict_end.keys())
    n_end = meta_dict_end.values()

    plt.figure()
    plt.title('Metabolism distribution')
    plt.ylabel('n')
    plt.xlabel('Metabolism')
    plt.bar(visions0, n0, color='mediumslateblue')
    plt.bar(visions_end, n_end, color='mediumvioletred')
    plt.legend(['Initial', 'Final'])
    plt.savefig('graphics/img/distributions/metabolisms.png')


def make_gif(img_loc, name):
    # clear_dir(img_loc, '.png')

    frames = [Image.open(image) for image in sorted(glob.glob(img_loc+'/*.png'), key=os.path.getmtime)]
    frame_one = frames[0]
    frame_one.save('graphics/gifs/'+name+'.gif', format='GIF', append_images=frames, save_all=True, duration=250, loop=0)


