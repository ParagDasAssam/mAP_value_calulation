    #obj_name = json_data["detection_classes"][labels] # obj['label']
    #conf = json_data["detection_scores"][labels]
    #left = json_data["detection_boxes"][labels][0]
    #                    top = json_data["detection_boxes"][labels][1]
     #                   right = json_data["detection_boxes"][labels][2]
     #                   bottom = json_data["detection_boxes"][labels][3]
     #                   print(str(obj_name) + " " + str(conf) + " " + str(left) + " " + str(top) + " " + str(right) + " " + str(bottom) + '\n')

map_label = {1:'inv_num',2:'inv_dt', 3:'inv_tot', 4:'stotal', 5:'vendor', 6:'addr', 7:'tax'}

import os
import json
# os.chdir("C:\\Users\\M1050683\\Documents\\POC\\mAP\\Invoice_mAP\\input\\detection-results")
file_dir = "C:\\Users\\M1050683\\Documents\\POC\\mAP\\Invoice_mAP\\input\\detection-results\\"
detected_files = os.listdir(file_dir)
#print(detected_files,"\n",len(detected_files))



for files in detected_files:
    data = ""
    print(file_dir+files)
    fil = open(file_dir+files,'r')
    json_data = json.load(fil)
    print(json_data)
    #for key in json_data.keys():
    for i in range(7):
        obj_name = map_label[json_data["detection_classes"][i]]
        conf = json_data["detection_scores"][i]
        left = json_data["detection_boxes"][i][0]
        top = json_data["detection_boxes"][i][1]
        right = json_data["detection_boxes"][i][2]
        bottom = json_data["detection_boxes"][i][3]
        #print(str(obj_name) + " " + str(conf) + " " + str(left) + " " + str(top) + " " + str(right) + " " + str(bottom) + '\n')
        data = data + str(obj_name) + " " + str(conf) + " " + str(left) + " " + str(top) + " " + str(right) + " " + str(bottom) + '\n'
        #print("________________________________________")
    fil.closed
    print("\nData\n")
    print(data)
    name = files.replace(".json", ".txt")
    f1 = open(file_dir+name,'w')
    f1.write(data)
    f1.closed
