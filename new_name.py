import os

#資料夾的檔案
all_files = []
all_paths = []
for path, dir, file in os.walk("new_img\\"): #資料夾路徑
    for f in file:
        if os.path.splitext(f)[-1] in ['.jpg']:
            all_files.append(f)
            all_paths.append(path)
#for i in range(len(all_files)):            
    #print(all_paths[i] + "\t" + all_files[i])

for i in range(len(all_files)):            
    print(all_paths[i]  + all_files[i])
    k =40 #檔案名稱從1開始
    fname = all_files[i]
    new_fname = "b"+str(i+k)+".jpg"  #檔案名稱
    os.rename(os.path.join(all_paths[i], fname), os.path.join(all_paths[i], new_fname))
