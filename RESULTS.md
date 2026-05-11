# Results and Model Evaluation

## Overview

This file presents the detailed results of the pressure ulcer segmentation project. The project compared three deep learning models for automated pressure ulcer wound segmentation from medical images:

- U-Net
- Attention U-Net
- DeepLabV3+

The models were trained and evaluated using the same dataset preparation, preprocessing pipeline, and evaluation strategy to ensure a fair comparison.

---

## Evaluation Metrics

The models were evaluated using the following segmentation metrics:

### Dice Coefficient

Dice coefficient measures the overlap between the predicted segmentation mask and the ground-truth mask. A higher Dice score means the predicted wound region is closer to the actual wound region.

### Intersection over Union

Intersection over Union, also known as IoU, measures the overlap between the predicted wound mask and the true wound mask divided by their combined area. A higher IoU indicates better segmentation accuracy.

### Recall

Recall measures how many actual wound pixels were correctly detected by the model. In medical image segmentation, recall is important because missing wound areas may affect wound assessment and monitoring.

### F1-score

F1-score balances precision and recall. It provides an overall measure of the model's segmentation reliability.

### Pixel Accuracy

Pixel accuracy measures the percentage of correctly classified pixels across the image. However, in medical segmentation, pixel accuracy should be interpreted carefully because background pixels may dominate the image.

---

## Model Comparison Table

| Metric | U-Net | Attention U-Net | DeepLabV3+ |
|---|---:|---:|---:|
| Dice | 0.7883 | 0.7960 | 0.8041 |
| IoU | 0.6902 | 0.7030 | 0.7068 |
| Recall | 0.9234 | 0.9416 | 0.8988 |
| F1-score | 0.8223 | 0.8321 | 0.8345 |
| Pixel Accuracy | 0.9957 | 0.9960 | 0.9967 |

---

## Result Interpretation

The results show that all three models were able to learn the pressure ulcer segmentation task. However, there were differences in performance across the models.

### U-Net

U-Net performed well as a baseline medical image segmentation model. It produced a Dice score of 0.7883 and an IoU of 0.6902. These results show that U-Net was able to identify wound regions reasonably well, but its overall performance was slightly lower than Attention U-Net and DeepLabV3+.

### Attention U-Net

Attention U-Net improved over the standard U-Net in Dice score, IoU, recall, F1-score, and pixel accuracy. It achieved the highest recall score of 0.9416. This means Attention U-Net was the best model for capturing the largest amount of actual wound area.

High recall is important in healthcare-related segmentation because missing wound regions can be clinically risky. However, Attention U-Net did not achieve the highest overall Dice or IoU score.

### DeepLabV3+

DeepLabV3+ achieved the best overall performance. It produced the highest Dice score of 0.8041, highest IoU of 0.7068, highest F1-score of 0.8345, and highest pixel accuracy of 0.9967.

These results suggest that DeepLabV3+ provided the most balanced and reliable segmentation performance for this project. Its multi-scale feature extraction helped the model capture wound regions with different shapes and sizes.

---

## Best Performing Model

Based on the overall results, **DeepLabV3+ was selected as the best-performing model** for pressure ulcer segmentation.

DeepLabV3+ performed best in the following metrics:

- Dice coefficient
- Intersection over Union
- F1-score
- Pixel accuracy

Although Attention U-Net achieved the highest recall, DeepLabV3+ gave the strongest overall balance between overlap accuracy and segmentation reliability.

---

## Clinical Interpretation

The results indicate that deep learning can support more objective and repeatable pressure ulcer assessment. Automated segmentation can help outline wound boundaries more consistently than manual visual inspection.

DeepLabV3+ may be useful where accurate wound boundary detection and stable segmentation are important. Attention U-Net may be useful in situations where detecting the complete wound area is more important than avoiding false positives.

However, this project is not intended to replace clinicians. The model should be considered a decision-support tool that may assist with wound documentation, monitoring, and measurement after further clinical validation.

---

## Suggested Result Images

The following result images can be added to the `results/` folder:

```text
results/
├── accuracy_graph.png
├── loss_graph.png
├── model_comparison.png
└── sample_predictions.png
```

### accuracy_graph.png

This image should show the training and validation accuracy across epochs. It helps demonstrate how well the model learned during training.

### loss_graph.png

This image should show the training and validation loss across epochs. It helps show whether the model was improving and whether overfitting occurred.

### model_comparison.png

This image can show a bar chart comparing U-Net, Attention U-Net, and DeepLabV3+ using Dice, IoU, F1-score, recall, and pixel accuracy.

### sample_predictions.png

This image should show example input images, ground-truth masks, and predicted masks. This is especially useful for segmentation projects because it visually demonstrates how accurately the model identifies the wound region.

---

## Key Findings

- DeepLabV3+ achieved the strongest overall segmentation performance.
- Attention U-Net achieved the highest recall.
- U-Net performed well as a baseline model but was slightly weaker than the other two models.
- Dice and IoU results show that DeepLabV3+ produced the best wound-mask overlap.
- Automated segmentation can support objective wound assessment, documentation, and treatment monitoring.
- Further testing with larger and clinically validated datasets is required before real-world medical use.

---

## Limitations

The results should be interpreted with the following limitations:

- The dataset may not fully represent all real clinical environments.
- Image quality, lighting, camera type, and skin tone variation may affect performance.
- Some small wounds or complex wound boundaries may still be difficult to segment accurately.
- The ground-truth masks may not be fully clinically validated.
- The project has not been deployed or tested in a real clinical workflow.

---

## Conclusion

This result analysis shows that deep learning models can be used for automated pressure ulcer segmentation. Among the three models tested, DeepLabV3+ achieved the best overall performance and was selected as the most suitable model for this project.

Attention U-Net also showed strong performance, especially in recall, making it useful in cases where detecting the full wound area is important.

Overall, this project demonstrates the potential of deep learning to support objective, consistent, and repeatable pressure ulcer wound assessment.
