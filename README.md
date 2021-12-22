# ML_Cyber_Project_2021
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
├── bd_model
    └── sunglasses_bd_net.h5
    └── sunglasses_bd_weights.h5
    └── multi_trigger_multi_target_bd_net.h5
    └── multi_trigger_multi_target_bd_weights.h5
    └── anonymous_1_bd_net.h5
    └── anonymous_1_bd_weights.h5
    └── anonymous_2_bd_net.h5
    └── anonymous_2_bd_weights.h5
├── fine_pruned_model
    └── sunglasses_bd_model_pruned.h5
    └── anonymous_1_bd_model_pruned.h5
    └── anonymous_2_bd_model_pruned.h5
    └── multi_trigger_multi_target_bd_model_pruned.h5
├── eval
    └── eval_sunglasses.py
    └── eval_anonymous_1.py
    └── eval_anonymous_2.py
    └── eval_multi_trigger_multi_target.py
├── grid_search_results
    └── cl_acc_sunglasses.csv
    └── asr_sunglasses.csv
    └── cl_acc_anonymous_1.csv
    └── asr_anonymous_1.csv
    └── cl_acc_multi_trigger_multi_target.csv
    └── asr_multi_trigger_multi_target.csv
    └── combined_metrics.csv
├── Project_Final_Report__ECE_9383_.pdf //project report
├── ML_Cyber_Project.ipynb //source code of all experiment
├── goodmodel_reference.ipynb //example reference code for our GoodNets
```
## 1. Dataset
1. Download the validation and test datasets from [here](https://drive.google.com/drive/folders/13o2ybRJ1BkGUvfmQEeZqDo1kskyFywab?usp=sharing) and store them under data/ directory.
2. The dataset contains images from YouTube Aligned Face Dataset. We retrieve 1283 individuals each containing 9 images in the validation dataset.
## 2.Models
Repaired models for backdoor attacks on face recognition can be found in the [link](https://drive.google.com/drive/folders/1HSZfSBNjKsOLPnAboHK5mzFRpvToIasY?usp=sharing).
Repaired models are also stored in the fine_pruned_model on this repo.
## 3.Evaluation
1. Evaluation script can be found in the following [link](https://drive.google.com/drive/folders/1IP82wqKbl8LgidMKMqcUXbfg67_j1mWS?usp=sharing)
2. You can run evaluation script using the command: python [script path] --img_path [img_path] --bd_model_path [badnets_path] --pruned_model_path [fine_pruned_model path]. For exmaple, python /content/ML_Cyber_Project_2021/eval/eval_sunglasses.py --img_path /content/img.jpeg --bd_model_path /content/ML_Cyber_Project_2021/bd_model/sunglasses_bd_net.h5 --pruned_model_path /content/ML_Cyber_Project_2021/fine_pruned_model/sunglasses_bd_model_pruned.h5
3. For simplicity, you can directly run the goodmodel_reference.ipynb on [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1fVKeSfyWNd1JXSxkyk1MoIQgqifftZld?usp=sharing) following the code in the notebook.
