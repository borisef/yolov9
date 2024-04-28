import yaml
import os


dataDir = '/home/borisef/data/css-data/' # css-data is the unzip path of the dataset
workingDir = '/home/borisef/projects/yolov9/data/' # Working Dir in google colab
num_classes = 10
classes = ['Hardhat', 'Mask', 'NO-Hardhat', 'NO-Mask', 'NO-Safety Vest', 'Person', 'Safety Cone', 'Safety Vest', 'machinery', 'vehicle']

file_dict = {
    'train': os.path.join(dataDir, 'test'),
    'val': os.path.join(dataDir, 'test'),
    'test': os.path.join(dataDir, 'test'),
    'nc': num_classes,
    'names': classes
}

with open(os.path.join(workingDir, 'data_css_try.yaml'), 'w+') as f:
  yaml.dump(file_dict, f)