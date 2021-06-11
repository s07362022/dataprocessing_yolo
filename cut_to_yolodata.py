from bs4 import BeautifulSoup
import os
import shutil
list1 =[]
status_dic = {"cap":0,"person":1}
def getYoloFormat(filename,label_path, img_path, yolo_path, newname):
    with open(label_path+ filename, 'r',encoding="utf-8") as f:
        soup = BeautifulSoup(f.read(), 'xml')
        imgname = soup.select_one('filename').text
        
        image_w = int(soup.select_one('width').text)
        image_h = int(soup.select_one('height').text)
        ary = []
        for obj in soup.select('object'):
            xmin = int(obj.select_one('xmin').text)
            xmax = int(obj.select_one('xmax').text)
            ymin = int(obj.select_one('ymin').text)
            ymax = int(obj.select_one('ymax').text)
            objclass = status_dic.get(obj.select_one('name').text)

            x = (xmin + (xmax-xmin)/2) * 1.0 / image_w
            y = (ymin + (ymax-ymin)/2) * 1.0 / image_h
            w = (xmax-xmin) * 1.0 / image_w
            h = (ymax-ymin) * 1.0 / image_h
            ary.append(' '.join([str(objclass), str(x),str(y),str(w),str(h)]))
            #print(ary)
            if os.path.exists(img_path + imgname):
                shutil.copyfile(img_path + imgname, yolo_path + newname + '.jpg')
                print(newname)
            with open(yolo_path + newname + '.txt', 'w') as f:
                f.write('\n'.join(ary))
        
import os
labelpath = 'F:\\Dataset\\cap\\k_clab\\'
imgpath   = 'F:\\Dataset\\cap\\k_cimg\\'
yolopath  = 'F:\\Dataset\\cap\\yolo\\'
ary = []
for idx, f in enumerate(os.listdir(labelpath)):
    try:
        getYoloFormat(f, labelpath,imgpath, yolopath, str(idx))
        print(f)
        print(idx)
    except Exception as e:
        print(e)