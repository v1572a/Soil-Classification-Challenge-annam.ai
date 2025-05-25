 Soil Classification Challenges – AI Competition 2025

This repository contains solutions to two separate soil image classification challenges conducted as part of an AI competition.

---

## Challenge 1: Soil Type Classification (Multiclass)

- Objective: Classify each image of soil into one of several soil types (e.g., Red, Black, Alluvial, etc.).
- Data: Labeled training images with known soil types and a test set with unknown labels.
- Type: Supervised multiclass image classification.
- Evaluation Metric: Macro F1 Score.
- Public Leaderboard Score: 0.9655

---

## Challenge 2: Soil vs Non-Soil Classification (Binary)

- Objective: Determine whether a given image contains soil or not (1 = soil, 0 = non-soil).
- Data: Training set contains only soil images. Test set contains a mix of soil and non-soil images.
- Type: One-class classification or anomaly detection.
- Evaluation Metric: F1 Score.
- Strategy: No negative examples in training.
- Public Leaderboard Score: 0.9801

## Setup Instructions
- Install python environment
- create a virtual environment using venv
- Go to directory containing challenge 1 or challenge 2
- pip install -r requirements.txt
- Download Dataset from kaggle and create a data folder and extract the data into the folder
- add corresponding path of dataset in training pynb at their needed positions respectively

