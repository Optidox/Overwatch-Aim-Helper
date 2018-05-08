import imageio

vid = imageio.get_reader('testvid2.mp4')
for i, im in enumerate(vid):
    print('Mean of frame %i is %1.1f' % (i, im.mean()))