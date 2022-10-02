import glob
from PIL import Image

def make_gif(frame_folder):
    images = glob.glob(f"{frame_folder}/*.jpg")
    images.sort()
    frames = [Image.open(image) for image in images]
    frames = [frame.crop((100,0,725,625)) for frame in frames] # Для обрезки
    frame_one = frames[0]
    frame_one.save("test.gif",  save_all=True, append_images=frames[1:], optimize=True, duration=200,
                   loop=0) # сборка всех фреймов в фаил и другие настройки


if __name__ == '__main__':
    make_gif("outout")

