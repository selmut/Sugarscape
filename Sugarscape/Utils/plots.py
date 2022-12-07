from PIL import Image
import matplotlib.pyplot as plt
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


def scatter_agents(agents_x, agents_y, img_loc, t):
    fig = plt.figure()
    plt.style.use('dark_background')
    plt.scatter(agents_x, agents_y, c='mediumslateblue', s=30, alpha=1, edgecolors='darkslateblue', linewidths=0.1)
    plt.xticks([])
    plt.yticks([])
    plt.title('Time step: '+str(t))
    plt.savefig(img_loc + '/living_area_'+str(t)+'.png')
    plt.close(fig)


def make_gif(img_loc, name):
    # clear_dir(img_loc, '.png')

    frames = [Image.open(image) for image in sorted(glob.glob(img_loc+'/*.png'), key=os.path.getmtime)]
    frame_one = frames[0]
    frame_one.save('graphics/gifs/'+name+'.gif', format='GIF', append_images=frames, save_all=True, duration=250, loop=0)


