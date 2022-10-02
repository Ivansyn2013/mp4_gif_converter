import cv2

def convert_mp4_to_jpgs(path):
    '''creating jpeg frames from mp4'''
    video_capture = cv2.VideoCapture(path)
    still_reading, image = video_capture.read()
    frame_count = 0
    while still_reading:
        cv2.imwrite(f"outout/frame_{frame_count:03d}.jpg", image) #сохраняем
        still_reading, image = video_capture.read()
        frame_count += 1

if __name__ == '__main__':
    print( 'Запущен как main')



convert_mp4_to_jpgs('data/2.mp4')