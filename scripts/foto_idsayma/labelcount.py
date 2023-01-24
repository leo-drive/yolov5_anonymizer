from matplotlib import pyplot as plt
import seaborn as sns
import glob
from os.path import isfile

txts_path_default = "/home/leo/yolo_ws/yolov5/datasets/face_lp_dataset/"
label_path_default = "classes.txt"
re_label_path_default = ".*" + label_path_default + "$"
result_name = "RESULTS.txt"

if not isfile(label_path_default):
	print(label_path_default + " FILE is not found!!, insert it into the directory!!!")
	exit()

with open(label_path_default, 'r') as labels:
    labels = [(str(no), name) for no, name in enumerate(labels.read().split('\n'))]
    label_ids = {str(i): 0 for i in range(len(labels))}

for txt_path in glob.glob(txts_path_default + "*.txt"):
    if txt_path.split("/")[-1] == label_path_default or txt_path.split("/")[-1] == result_name:
        print(txt_path, " passed!")
        continue
    
    with open(txt_path, "r") as text:
        text_inside = text.read().split('\n')
        ids = [id.split()[0] for id in text_inside if id]
        
        for id in ids:
            label_ids[id] += 1

for no, name in labels:
    label_ids[name] = label_ids[no]
    del label_ids[no]
  
with open(result_name, "w") as result:
    for name, amount in label_ids.items():
        to_write = f"{name} -> {amount}\n"
        result.write(to_write)

x = list(label_ids.keys())
y = [int(value) for value in list(label_ids.values())]

plt.figure(figsize=(30,30))
sns.barplot(x=x, y=y)
plt.xticks(rotation=90)
plt.savefig(input("Give the name of plot: \n>") + ".png")
plt.show()

print("plot PNG and results txt saved to the current directory!!")
