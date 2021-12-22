# ML_Cyber_Project_2021
ML_Cyber_Project_2021
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1rMMmgmsrudhktGaoUVCDJatgG5m15i_1#scrollTo=7mDgUVTqwrTZ)

```
├── data 
    └── clean_validation_data.h5 // this is clean data used to evaluate the BadNet and design the backdoor defense
    └── clean_test_data.h5
    └── sunglasses_poisoned_data.h5
    └── anonymous_1_poisoned_data.h5
    └── Multi-trigger Multi-target
        └── eyebrows_poisoned_data.h5
        └── lipstick_poisoned_data.h5
        └── sunglasses_poisoned_data.h5
├── models
    └── sunglasses_bd_net.h5
    └── sunglasses_bd_weights.h5
    └── multi_trigger_multi_target_bd_net.h5
    └── multi_trigger_multi_target_bd_weights.h5
    └── anonymous_1_bd_net.h5
    └── anonymous_1_bd_weights.h5
    └── anonymous_2_bd_net.h5
    └── anonymous_2_bd_weights.h5
├── architecture.py
└── eval.py // this is the evaluation script
```
## 1. Dataset
1. Download the validation and test datasets from [here](https://drive.google.com/drive/folders/13o2ybRJ1BkGUvfmQEeZqDo1kskyFywab?usp=sharing) and store them under data/ directory.
2. The dataset contains images from YouTube Aligned Face Dataset. We retrieve 1283 individuals each containing 9 images in the validation dataset.
## 2.Models
Training models for backdoor attacks on face recognition can be found in the following link
https://drive.google.com/drive/folders/1HSZfSBNjKsOLPnAboHK5mzFRpvToIasY
## 3.Evaluation
Evaluation script can be found in the following link
https://drive.google.com/drive/folders/1IP82wqKbl8LgidMKMqcUXbfg67_j1mWS
