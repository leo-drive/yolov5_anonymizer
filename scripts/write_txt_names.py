import os

with open('./datasets/train.txt', 'w') as out:
    for img in [f for f in os.listdir('/home/leo/yolo_ws/yolov5/datasets/train/') if f.endswith('jpg')]:
        out.write("/home/leo/yolo_ws/yolov5/datasets/train/" + img + '\n')
