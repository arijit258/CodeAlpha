# SMS Spam Classification Project

This project aims to develop a machine learning model to classify SMS messages as either spam or non-spam (ham). The project employs three popular machine learning algorithms: Logistic Regression, Naive Bayes, and Support Vector Machine (SVM) to achieve this task. The dataset used for training and testing these models is a collection of SMS messages labeled as spam or ham.

## Table of Contents

- [Dataset](#dataset)
- [Algorithms Used](#algorithms-used)
- [Requirements](#requirements)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Results](#results)

## Dataset

The dataset used for this project is not provided in this repository but can be obtained from various sources like the [SMS Spam Collection Dataset](https://www.kaggle.com/datasets/uciml/sms-spam-collection-dataset) on Kaggle. Make sure to download and preprocess the dataset before running the project.


## Algorithms Used

1. **Logistic Regression**: A binary classification algorithm that models the probability that a given input belongs to a particular class. It's known for its simplicity and interpretability.

2. **Naive Bayes**: A probabilistic algorithm based on Bayes' theorem with the "naive" assumption that the features are independent. It's often used for text classification tasks.

3. **Support Vector Machine (SVM)**: A powerful algorithm for binary classification that tries to find the hyperplane that best separates the data points belonging to different classes.

## Requirements

Make sure you have the following libraries and dependencies installed in your Python environment:

- Python 3.x
- pandas
- scikit-learn
- numpy

You can install these dependencies using the `requirements.txt` file provided in this repository.

```bash
pip install -r requirements.txt
```

## Getting Started

1. Clone this repository to your local machine:

```bash
git clone https://github.com/arijit/sms_spam_classification.git
```

2. Navigate to the project directory:

```bash
cd sms-spam-classification
```

3. Download the dataset and place it in the `data` directory (you may need to create the `data` directory if it doesn't exist).

4. Preprocess the dataset as needed. You can refer to the provided Jupyter Notebook or Python scripts for guidance on data preprocessing.

5. Train the models using the following command:


6. Once the models are trained, you can use them to make predictions on new SMS messages.


## Usage

- `train_models.py`: This script loads the preprocessed data, trains the Logistic Regression, Naive Bayes, and SVM models, and saves them in the `models` directory.

- `predict.py`: This script takes an input SMS message and uses the trained models to predict whether it's spam or ham.

## Results

After running the `train_models.py` script, you can evaluate the performance of the models on the test dataset. Metrics such as accuracy, precision, recall, and F1-score will be displayed in the console.

## Contributing

If you wish to contribute to this project, please fork the repository, make your changes, and submit a pull request. We welcome contributions that improve model performance, code quality, or documentation.
