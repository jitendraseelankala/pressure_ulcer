# Automated Segmentation of Pressure Ulcers from Medical Images

## Project Overview

This project focuses on the **automated segmentation of pressure ulcers from medical images** using deep learning. Pressure ulcers are injuries to the skin and underlying tissue caused by prolonged pressure, commonly affecting immobile, elderly, and critically ill patients. Accurate wound assessment is important because it helps clinicians monitor healing progress, document wound size, and make better treatment decisions.

Traditional pressure ulcer assessment often depends on manual visual inspection and physical measurement. This process can be slow, subjective, and inconsistent because different clinicians may mark wound boundaries differently. Wounds may also have irregular shapes, unclear borders, different tissue colours, and inconsistent lighting conditions. These factors make manual segmentation difficult and reduce the reliability of wound assessment.

To address this issue, this project applies deep learning-based semantic segmentation models to automatically identify and outline pressure ulcer regions from clinical wound images. The model receives a wound image as input and produces a binary segmentation mask that separates the wound region from the background.

---

## Problem Statement

Pressure ulcer assessment is still heavily dependent on manual judgement. Manual wound review can be time-consuming, subjective, and affected by inter-observer variability. In clinical practice, wound boundaries may not always be clear, especially when there are differences in wound shape, skin tone, lighting, image quality, and tissue appearance.

The main problem addressed in this project is not only detecting whether a wound is present, but accurately outlining the wound area at pixel level. This is important because reliable segmentation can support objective wound measurement, healing progress tracking, and clinical documentation.

---

## Research Aim

The aim of this project is to **design, implement, and evaluate deep learning models for automated segmentation of pressure ulcers from medical images**, with the goal of improving objective and repeatable wound assessment.

---

## Objectives

The main objectives of this project are:

1. To prepare pressure ulcer images and their corresponding ground-truth masks for segmentation analysis.
2. To apply image preprocessing techniques such as resizing, normalisation, mask binarisation, and augmentation.
3. To implement and compare three deep learning segmentation models:
   - U-Net
   - Attention U-Net
   - DeepLabV3+
4. To evaluate model performance using segmentation metrics such as:
   - Dice coefficient
   - Intersection over Union
   - Precision
   - Recall
   - F1-score
   - Pixel accuracy
   - Loss
5. To identify the most suitable model for accurate and clinically useful pressure ulcer segmentation.

---

## Research Gap

Previous wound assessment approaches have included manual inspection, rule-based image processing, traditional machine learning, and general deep learning models. However, these approaches have limitations.

Manual assessment is subjective and difficult to reproduce. Rule-based methods such as thresholding, edge detection, and region growing are sensitive to lighting and colour variation. Traditional machine learning approaches such as Support Vector Machines and Random Forests require handcrafted features such as colour, texture, and shape. Many existing deep learning studies focus on other wound types, such as diabetic foot ulcers, and may not generalise well to pressure ulcer segmentation.

This project addresses the gap by comparing three specialised segmentation architectures using the same dataset, preprocessing pipeline, training strategy, and evaluation metrics. This allows a fair comparison of model performance for pressure ulcer image segmentation.

---

## Project Contribution

This project contributes by:

- Using pressure ulcer image-mask pairs for pixel-level segmentation.
- Comparing U-Net, Attention U-Net, and DeepLabV3+ under a common experimental setup.
- Evaluating models using clinically meaningful segmentation metrics.
- Identifying the best-performing model for pressure ulcer wound boundary detection.
- Demonstrating how automated segmentation can support objective wound monitoring.

---

## Dataset Description

The project uses a pressure ulcer image segmentation dataset containing clinical wound images and corresponding binary masks. Each image has a matching ground-truth mask that identifies the wound region at pixel level.

In the binary mask:

- `1` represents the wound region.
- `0` represents the background.

The dataset is organised into image and mask pairs and is used for training, validation, and testing. The images are resized for consistency, and the masks are converted into binary form before training.

> Note: The dataset is not included in this repository due to privacy, licensing, and file size restrictions. Users should download the dataset separately from the original approved source.

---

## Methodology

The project follows a structured deep learning segmentation pipeline.

### 1. Data Collection

Pressure ulcer images and their corresponding ground-truth masks are collected and organised into suitable folders for training and testing.

### 2. Data Preprocessing

Preprocessing is applied to make the data suitable for model training. This includes:

- Resizing images to a consistent shape
- Normalising image pixel values
- Converting masks into binary format
- Ensuring each image has a corresponding mask

### 3. Data Augmentation

Data augmentation is used to improve model generalisation. Augmentation techniques may include:

- Horizontal flipping
- Vertical flipping
- Rotation
- Random transformations

These transformations help the models learn wound features under different orientations and conditions.

### 4. Model Training

Three segmentation models are trained using the same dataset and training strategy:

- U-Net
- Attention U-Net
- DeepLabV3+

All models are trained for semantic segmentation, where each pixel is classified as either wound or background.

### 5. Model Evaluation

The trained models are evaluated using quantitative metrics and visual comparison of predicted masks. The evaluation focuses on how closely the predicted masks match the ground-truth masks.

### 6. Best Model Selection

The best model is selected based on Dice coefficient, IoU, F1-score, pixel accuracy, recall, and visual prediction quality.

---

## Models Used

### U-Net

U-Net is an encoder-decoder segmentation model widely used in medical image segmentation. It uses skip connections to combine low-level spatial features with high-level semantic features. In this project, U-Net is used as the baseline segmentation model.

### Attention U-Net

Attention U-Net improves the standard U-Net architecture by adding attention gates. These attention mechanisms help the model focus more strongly on wound regions and reduce the influence of irrelevant background information. This is useful when wound boundaries are unclear or when the wound area is small.

### DeepLabV3+

DeepLabV3+ is an advanced semantic segmentation model that uses atrous convolution and multi-scale feature extraction. This allows the model to capture wound regions at different sizes and improve boundary detection. In this project, DeepLabV3+ achieved the strongest overall segmentation performance.

---

## Implementation Details

The project was implemented using Python and deep learning libraries.

### Main Tools and Libraries

- Python
- Google Colab
- PyTorch
- segmentation_models_pytorch
- NumPy
- Pandas
- Matplotlib
- OpenCV
- Scikit-learn

### Training Setup

- Encoder: ResNet34 pretrained on ImageNet
- Loss function: DiceBCE Loss
- Optimiser: Adam Optimizer
- Training controls:
  - Early stopping
  - Learning-rate scheduling
  - Dropout
  - Batch loading using PyTorch DataLoader

---

## Evaluation Metrics

The following metrics were used to evaluate segmentation performance.

### Dice Coefficient

Dice coefficient measures the overlap between the predicted mask and the ground-truth mask. A higher Dice score means better segmentation performance.

### Intersection over Union

IoU measures the ratio of the overlapping area between the predicted and actual wound mask to the total combined area. A higher IoU indicates stronger agreement between prediction and ground truth.

### Precision

Precision measures how many pixels predicted as wound were actually wound pixels. High precision means fewer false positives.

### Recall

Recall measures how many actual wound pixels were correctly detected by the model. High recall is important in medical segmentation because missing wound areas can be clinically risky.

### F1-score

F1-score combines precision and recall into a single balanced metric.

### Pixel Accuracy

Pixel accuracy measures the percentage of correctly classified pixels across the full image.

---

## Results

The three models were evaluated using the same testing strategy. The results show that all models learned the segmentation task, but DeepLabV3+ achieved the best overall performance.

| Metric | U-Net | Attention U-Net | DeepLabV3+ |
|---|---:|---:|---:|
| Dice | 0.7883 | 0.7960 | 0.8041 |
| IoU | 0.6902 | 0.7030 | 0.7068 |
| Recall | 0.9234 | 0.9416 | 0.8988 |
| F1-score | 0.8223 | 0.8321 | 0.8345 |
| Pixel Accuracy | 0.9957 | 0.9960 | 0.9967 |

---

## Result Interpretation

DeepLabV3+ achieved the highest Dice coefficient, IoU, F1-score, and pixel accuracy. This shows that it produced the strongest overall segmentation performance and was better at matching the predicted wound masks with the ground-truth masks.

Attention U-Net achieved the highest recall score. This means it was better at detecting more of the wound area and missing fewer wound pixels. In clinical applications, high recall can be important because missing part of a wound may affect wound measurement and monitoring.

U-Net performed well as a baseline model, but it was slightly lower than Attention U-Net and DeepLabV3+ across the main evaluation metrics.

Based on the overall results, **DeepLabV3+ is selected as the best-performing model for this project**, while Attention U-Net is also useful in cases where capturing the complete wound area is more important.

---

## Key Findings

- Deep learning can support objective and repeatable pressure ulcer assessment.
- Automated segmentation can reduce the limitations of manual wound boundary marking.
- DeepLabV3+ produced the best overall segmentation performance.
- Attention U-Net achieved the strongest recall and was effective at capturing wound regions.
- Segmentation masks can support wound measurement, documentation, and healing progress monitoring.
- Further clinical validation is required before using the system in real healthcare settings.

---

## Project Structure

```text
pressure_ulcer/
│
├── pressure_ulcer.ipynb      # Main Google Colab notebook
├── README.md                 # Project documentation
├── requirements.txt          # Required Python libraries
├── .gitignore                # Files and folders ignored by Git
│
└── results/                  # Optional folder for graphs and output images
    ├── accuracy_graph.png
    ├── loss_graph.png
    ├── confusion_matrix.png
    └── sample_prediction.png
```

---

## How to Run the Project

### Option 1: Run in Google Colab

1. Open the notebook file:

```text
pressure_ulcer.ipynb
```

2. Upload or connect the dataset.

3. Install the required libraries:

```bash
pip install -r requirements.txt
```

4. Run all notebook cells from top to bottom.

5. View the training results, evaluation metrics, and predicted segmentation masks.

---

### Option 2: Run Locally

Clone the repository:

```bash
git clone https://github.com/jitendraseelankala/pressure_ulcer.git
```

Move into the project folder:

```bash
cd pressure_ulcer
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Open the notebook:

```bash
jupyter notebook pressure_ulcer.ipynb
```

---

## Requirements

The project requires the following main Python libraries:

```text
numpy
pandas
matplotlib
opencv-python
scikit-learn
torch
torchvision
segmentation-models-pytorch
```

Make sure your `requirements.txt` file includes all libraries used in the notebook.

---

## Limitations

This project has some limitations:

- The dataset annotations may not be fully clinically validated.
- Model performance may vary on images captured using different cameras, lighting conditions, or clinical environments.
- Some small wounds and complex wound boundaries may still produce segmentation errors.
- The model was tested in a research environment and has not been clinically deployed.
- The system should not be used as a replacement for professional medical judgement.

---

## Future Work

Future improvements may include:

- Using a larger and more diverse clinically validated dataset.
- Testing the model on images from different hospitals, devices, and lighting conditions.
- Adding explainable AI methods to improve clinical trust.
- Exploring ensemble models for better segmentation performance.
- Developing a web or mobile application for real-time wound monitoring.
- Validating the model with clinical experts before practical use.

---

## Medical Disclaimer

This project is for academic, educational, and research purposes only. It is not a certified medical device and should not be used for direct medical diagnosis, treatment planning, or clinical decision-making. Any healthcare-related use would require further testing, expert review, and clinical validation.

---

## Conclusion

This project demonstrates that deep learning can be used to automate pressure ulcer segmentation from medical images. By comparing U-Net, Attention U-Net, and DeepLabV3+ under the same experimental setup, the project shows that DeepLabV3+ provides the best overall segmentation performance, while Attention U-Net performs strongly in terms of recall.

The proposed approach can support objective wound assessment by producing repeatable wound masks, reducing reliance on manual boundary marking, and assisting wound documentation and monitoring. However, further validation with larger and clinically verified datasets is required before real-world clinical use.

---

## Author

**Jitendra Seelankala**

---

## References

Selected references related to this project include:

- Chang et al. — Pressure ulcer segmentation and CNN-based diagnosis
- Wang et al. — Deep learning and U-Net evolution in medical imaging
- Moorthy and Gandhi — Deep learning techniques for image analysis
- Kabir et al. — Wound tissue types and chronic wound burden
- Ghnemat et al. — AI performance and explainability
- Scebba et al. — Variability in wound documentation


