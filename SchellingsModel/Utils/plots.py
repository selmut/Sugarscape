from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import matplotlib.patches as mpatches
import numpy as np
import glob
import os


# plots a given generation's grid matrix and saves the image
def plot_living_area(area, agents_x, agents_y, img_loc, t):
    fig = plt.figure()
    plt.style.use('dark_background')
    # GnBu_r
    plt.imshow(area, cmap='copper', alpha=1)
    plt.scatter(agents_x, agents_y, c='mediumslateblue', s=30, alpha=1, edgecolors='darkslateblue', linewidths=0.1)
    plt.xticks([])
    plt.yticks([])
    plt.title('Time step: '+str(t))
    plt.savefig(img_loc + '/sugarscape_'+str(t)+'.png')
    plt.close(fig)


def plot_schellings(to_plot, time, name):
    fig = plt.figure()
    #plt.style.use('dark_background')
    plt.xticks([])
    plt.yticks([])
    plt.title('Schelling\'s model')
    cmap = {1: colors.to_rgb('midnightblue'), 100: colors.to_rgb('lavender'), 0: colors.to_rgb('dimgray')}
    labels = {1: 'Family A', 100: 'Family B', 0: 'Empty house'}
    to_show = np.array([[cmap[i] for i in j] for j in to_plot])
    patches = [mpatches.Patch(color=cmap[i], label=labels[i]) for i in cmap]
    plt.legend(handles=patches, loc=4, framealpha=0.9, edgecolor='k', labelcolor='k')
    plt.imshow(to_show)
    plt.savefig('graphics/img/schelling/'+name+str(time)+'.png', bbox_inches='tight')
    plt.close(fig)


def plot_happiness(happiness_A, happiness_B, happiness_total, moving_events, moving_times, timeSteps):
    times = np.arange(0, timeSteps, step=1000)
    fig = plt.figure()
    plt.plot(times, happiness_A, 'mediumslateblue', linewidth=2)
    plt.plot(times, happiness_B, 'turquoise', linewidth=2)
    plt.plot(times, happiness_total, 'mediumvioletred', linewidth=2)
    plt.scatter(moving_times, moving_events, c='k', s=5)
    plt.ylabel('p')
    plt.xlabel('time')
    plt.title('Happiness scores')
    plt.legend(['happiness (A)', 'happiness (B)', 'happiness (total)'])
    plt.savefig('graphics/img/happiness/happiness.png')
    plt.close(fig)


def make_gif(img_loc, name):
    # clear_dir(img_loc, '.png')

    frames = [Image.open(image) for image in sorted(glob.glob(img_loc+'/*.png'), key=os.path.getmtime)]
    frame_one = frames[0]
    frame_one.save('graphics/gifs/'+name+'.gif', format='GIF', append_images=frames, save_all=True, duration=5, loop=0)


