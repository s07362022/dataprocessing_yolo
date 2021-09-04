 coding: utf-8
# author: hxy
# 2020-6-15
"""
 The code is used to convert yolo’s txt label format to kitti’s txt label format;
"""
import os
import cv2
import time

class_name = ' '


# Restore the coordinates in the txt to the coordinates of the original photo
def restore_coordinate(yolo_bbox, image_w, image_h):
    box_w = float(yolo_bbox[3]) * image_w
    box_h = float(yolo_bbox[4]) * image_h
    x_mid = float(yolo_bbox[1]) * image_w + 1
    y_mid = float(yolo_bbox[2]) * image_h + 1
    xmin = int(x_mid - box_w / 2)
    xmax = int(x_mid + box_w / 2)
    ymin = int(y_mid - box_h / 2) + 5 # Added an offset of 5;
    ymax = int(y_mid + box_h / 2) + 5
    return [xmin, ymin, xmax, ymax]


# Generate txt tag file in kitti format
def write_to_kitti_txt(save_path, box, name):
    with open(os.path.join(save_path, name + '.txt'), 'w') as f:
        # kitti tag file contains 15 parameters
        new_info = class_name + ' ' + '0.00' + ' ' + '0' + ' ' + '0.00' + ' '\
                   + str(box[0]) + ' ' + str(box[1]) + ' ' + str(box[2]) + ' ' + str(box[3]) \
                   + ' ' + '0.00' + ' ' + '0.00' + ' ' + '0.00' + ' ' + '0.00' + ' ' + '0.00' \
                   + ' ' + '0.00' + ' ' + '0.00'
        f.writelines(new_info)
    f.close()


# Get the labels file and images file of the photo, and generate a new label file
def restore_results(images_folder, labels_folder):
    labels = os.listdir(labels_folder)
    for label in labels:
        name = label.split('.')[0]
        print(name)
        with open(os.path.join(labels_folder, label), 'r') as f:
            info = f.readline().strip('\n')
            label = list(info.split(' '))
            img = cv2.imread(os.path.join(images_folder, name + '.jpg'))
            w = img.shape[1]
            h = img.shape[0]
            ori_box = restore_coordinate(label, w, h)
            write_to_kitti_txt('./kitti_labels', ori_box, name)
            # Draw the converted coordinate value onto the original picture and display it for viewing
            # cv2.rectangle(img, (ori_box[0], ori_box[1]), (ori_box[2], ori_box[3]), (0, 255, 255), 2)
            # cv2.imshow('Transfer_label', img)
            # if cv2.waitKey(100) & 0XFF == ord('q'):
            #     break
        f.close()
    # cv2.destoryAllWindows()


if __name__ == '__main__':
    s = time.time()
    print('----Data conversion start---')

    restore_results('./images',
                    './labels')

    print('---Time-consuming: {:.3f}ms'.format(time.time() - s))
    print('---Data conversion succeeded---')

