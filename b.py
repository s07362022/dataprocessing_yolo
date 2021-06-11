import os
datasets = ['F:\\Dataset\\cap\\yolo\\'+ f for f in os.listdir('F:\\Dataset\\cap\\yolo\\') if not f.endswith('.txt')]
print(len(datasets) *0.75)


with open('F:\\Dataset\\cap\\train.txt', 'w') as f:
    f.write('\n'.join(datasets[0:285]))

with open('F:\\Dataset\\cap\\test.txt', 'w') as f:
    f.write('\n'.join(datasets[285:]))
