# mAP_value_calulation

Calculate mAP values for object detection model in Colab.
After clonning this repo, you have to make the internal file structure. So execute all the commands to create the dir with proper names.

# Create file dir:

%cd /content/
!mkdir mAP_value_calulation/input/
!mkdir mAP_value_calulation/input/detection-results/
!mkdir mAP_value_calulation/input/ground-truth/
!mkdir mAP_value_calulation/input/images-optional/



# What is mAP (mean Average Precision)?

AP (Average precision) is a popular metric in measuring the accuracy of object detectors like Faster R-CNN, SSD, etc. 
Average precision computes the average precision value for recall value over 0 to 1.

Precision & recall
•	Precision measures how accurate is your predictions. i.e. the percentage of your predictions are correct.
•	Recall measures how good you find all the positives. For example, we can find 80% of the possible positive cases in our top K predictions.

    TP = True Positive
    TN = True Negative
    FP = False Positive
    FN = False Negative

    Precision = TP/ TP + FP
    or 
    Precision = TP / total positive results


    Recall = TP/ TP + FN
    or
    Recall = TP/ total negative cases

    F1 = 2 (( precision X recall ) / ( Precision + recall ))

# IoU (Intersection over union)
IoU measures the overlap between 2 boundaries. We use that to measure how much our predicted boundary overlaps with the ground truth (the real object boundary). In some datasets, we predefine an IoU threshold (say 0.5) in classifying whether the prediction is a true positive or a false positive.

Usefull links: 

https://medium.com/@jonathan_hui/map-mean-average-precision-for-object-detection-45c121a31173
https://towardsdatascience.com/breaking-down-mean-average-precision-map-ae462f623a52
https://github.com/Cartucho/mAP
https://www.youtube.com/watch?v=oqXDdxF_Wuw
