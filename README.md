# Automated Vote Counting System

This repository contains the code and datasets used for an automated vote counting system. It includes raw datasets, annotations, image processing scripts, and OCR model training/inference using PaddleOCR.

## Repository Structure

### RawDataset
- **Description:** Contains the original, unprocessed dataset.
- **Contents:** Raw images, provided labels, and a sample submission file.

### AnnotationV1
- **Description:** Contains the first set of annotations for each image used for cropping.
- **Example Cropping Result:**
  ![alt text](TPS_001_2.jpg)

### AnnotationV2
- **Description:** Contains an alternative version of annotations for each image.
- **Example Cropping Result:**
  ![alt text](TPS_001_1.jpg)

### Image Processing
- **Description:** Contains Python scripts for bird’s-eye view image processing and image augmentation.
- **Structure:**
  - **train/test folders:** Each includes an `images` folder (source images from the RawDataset) and a `labels` folder (annotations for cropping).
  - **Output:** Cropped images are saved in `train_result` and `test_result`.
  - **Augmentation:** Contains an `augmentation` folder for images to be augmented using `augmentation.py`. Augmented images are saved in `augmentation_result`.

### DatasetV1
- **Description:** Contains the preprocessed data after cropping and augmentation.
- **Contents:** Cropped and augmented images, a label file, and a notebook for adjusting labels to match the dataset.

### Dataset V2
- **Description:** Contains preprocessed data produced solely by `image_processing.py`.
- **Contents:** A label file and a notebook to adjust labels according to the dataset.

### PaddleOCR
- **Description:** Contains the library and scripts for training an OCR model using PaddleOCR.
- **More Information:** [PaddleOCR GitHub](https://github.com/PaddlePaddle/PaddleOCR)
- **Training Instructions:**
  1. Move the dataset contents into the `Dataset` folder in PaddleOCR.
  2. Transfer 20% of the `Train` data to the `Eval` folder.
  3. Use the provided notebook to adjust labels according to PaddleOCR's format.
  4. Start training with:
     ```bash
     python tools/train.py -c configs/rec/PP-OCRv3/en_PP-OCRv3_rec.yml -o Global.checkpoints=./output/v3_en_mobile/latest
     ```
- **Inference Instructions:**
  1. Run the inference command:
     ```bash
     python tools/infer_rec.py -c configs/rec/PP-OCRv3/en_PP-OCRv3_rec.yml -o Global.pretrained_model=./output/v3_en_mobile/{model_name, e.g. latest} Global.infer_img=./Dataset/Test
     ```
  2. The inference output is saved in the `output/rec` folder.

### Predict Percentage
- **Description:** Contains the `percentage.ipynb` notebook used to calculate the valid vote percentage from prediction results.
- **Methodology:** 
  - Combines outputs from two prediction models.
  - Selects the prediction with the highest confidence score.
- **Exceptions:** 
  - For TPS 606, 648, and 700, the prediction from the first model is retained due to potential image misinterpretations (e.g., two circles in one column or filling errors).
  - TPS 700, having 5 columns and being unique in the dataset, is particularly challenging for the second model since it was not trained on similar data.

## Usage
- **Preprocessing:** Run the scripts in the **Image Processing** folder to crop and augment your images.
- **OCR Training & Inference:** Follow the instructions in the **PaddleOCR** folder.
- **Vote Percentage Calculation:** Use the `percentage.ipynb` notebook in the **Predict Percentage** folder to compute final predictions.

*For more details and updates, please refer to the repository contents and respective documentation files.*
