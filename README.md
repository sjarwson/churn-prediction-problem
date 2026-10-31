# Churn-prediction-problem
Predict whether a customer is likely to cancel or stop using the service by using billing, support, and demographics data, so the business can proactively retain at-risk customers.

## Project description
The point of this project is to analyze the data from churn_dataset.csv, perform exploratory data analysis, feature engineering and create a machine learning model that predicts customer churn. The predictions can help the business identify at-risk customers so that the business can take preventive action.

## Data description
The dataset contains 20 individual instances and 14 features for each instance. The dataset includes demographical features like age and gender, billing information such as the amount of months the individual has been a subscriber, monthly charges, and total charges, as well as support features like how many times the individual has contacted the support central. The dataset includes a target value which the model used for this project uses for training. This dataset is very small and is only used for educational purposes. The model results is therefore also reflective of this and any model results should not be taken seriously.

## Model
The model used for this project is logistic regression. This model was chosen because it is easy to interpret and had a perfect accuracy score of 1.0.

## Version control
Branch: decision-tree-experiment (not done)
Used for testing a new model

Branch: update-readme (not done)
Used for improving documentation.

## Pull request example
Title: Improve notebook descriptions

Summary: This update makes it easier to understand the workflow.

Changes: 
- Added a small description under each step in the notebook
- Updated README

Results: Project is easier to understand.

## How to run the project
Clone this repository:
git clone https://github.com/sjarwson/churn-prediction-problem.git

Navigate to the project folder:
cd churn-prediction-problem

Install the required dependencies:
pip install -r requirements.txt

Open the Jupyter Notebook:
jupyter notebook

Open notebooks/churn_experiment.ipynb and run the cells from top to bottom.
Make sure the dataset is located in the data/ folder before running the notebook.

## Summary of results
- Perfect results :)
