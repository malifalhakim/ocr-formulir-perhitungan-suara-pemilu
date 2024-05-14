import cv2
import numpy as np
from pathlib import Path
from PIL import Image
from straug.geometry import Shrink,Perspective,Rotate
from straug.camera import Contrast,Pixelate
from pathlib import Path

# Load Image Train Path
train_image_path = "train/images"
train_image_path = list(Path(train_image_path).glob("*.jpg"))
train_image_path = sorted(train_image_path)
train_image_path = list(map(str, train_image_path))
train_images = train_image_path

# Load Image Test Path
test_image_path = "test/images"
test_image_path = list(Path(test_image_path).glob("*.jpg"))
test_image_path = sorted(test_image_path)
test_image_path = list(map(str, test_image_path))
test_images = test_image_path

# Load Image Train Label Path
train_label_path = "train/labels"
train_label_path = list(Path(train_label_path).glob("*.txt"))
train_label_path = sorted(train_label_path)
train_label_path = list(map(str,train_label_path))
train_label = train_label_path

# Load Image Test Label Path
test_label_path = "test/labels"
test_label_path = list(Path(test_label_path).glob("*.txt"))
test_label_path = sorted(test_label_path)
test_label_path = list(map(str,test_label_path))
test_label = test_label_path

def crop_image(image_path,label_path,is_train=True):
    img = cv2.imread(image_path)
    annotations_list = []
    with open(label_path) as f:
        for line in f:
            annotations = line.strip()
            annotations_list.append(annotations)
    for annotations in annotations_list:
        tokens = annotations.split(" ")
        class_id = int(tokens[0])
        if len(tokens) == 5:
            
            x_center = float(tokens[1])
            y_center = float(tokens[2])
            width = float(tokens[3])
            height = float(tokens[4])

            x_min = int((x_center - width/2) * img.shape[1])
            x_max = int((x_center + width/2) * img.shape[1])
            y_min = int((y_center - height/2) * img.shape[0])
            y_max = int((y_center + height/2) * img.shape[0])

            points = [(x_min,y_max),(x_min,y_min),(x_max,y_min),(x_max,y_max)]

            pts1 = np.float32([[points[0][0],points[0][1]],[points[1][0],points[1][1]],
                                 [points[2][0],points[2][1]],[points[3][0],points[3][1]]])
            
            width = 200
            height = 400

            pts2 = np.float32([[0,height],[0,0],[width,0],[width,height]])

            matrix = cv2.getPerspectiveTransform(pts1,pts2)
            img_output = cv2.warpPerspective(img,matrix,(width,height))

            file_name = "TPS_" + Path(image_path).stem.split("_")[1] + "_" + str(class_id+1) + ".jpg"

            if is_train:
                write_str = f"train_result\\{class_id+1}\\{file_name}"
            else:
                write_str = f"test_result\\{class_id+1}\\{file_name}"

            cv2.imwrite(write_str,img_output)

        else:
            x_max = float(tokens[1])
            y_min = float(tokens[2])
            x_min = float(tokens[3])
            y_max = float(tokens[6])

            x_min = int(x_min * img.shape[1])
            x_max = int(x_max * img.shape[1])
            y_min = int(y_min * img.shape[0])
            y_max = int(y_max * img.shape[0])

            points = [(x_min,y_max),(x_min,y_min),(x_max,y_min),(x_max,y_max)]

            pts1 = np.float32([[points[0][0],points[0][1]],[points[1][0],points[1][1]],
                                 [points[2][0],points[2][1]],[points[3][0],points[3][1]]])
            
            width = 200
            height = 400

            pts2 = np.float32([[0,height],[0,0],[width,0],[width,height]])

            matrix = cv2.getPerspectiveTransform(pts1,pts2)
            img_output = cv2.warpPerspective(img,matrix,(width,height))

            file_name = "TPS_" + Path(image_path).stem.split("_")[1] + "_" + str(class_id+1) + ".jpg"

            if is_train:
                write_str = f"train_result\\{class_id+1}\\{file_name}"
            else:
                write_str = f"test_result\\{class_id+1}\\{file_name}"

            cv2.imwrite(write_str,img_output)
    
for i in range(len(train_images)):
    crop_image(train_images[i],train_label[i])

for i in range(len(test_images)):
    crop_image(test_images[i],test_label[i],is_train=False)