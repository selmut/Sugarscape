from PIL import Image
import matplotlib.pyplot as plt
import glob
import os


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

    plt.figure()
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


