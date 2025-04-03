# Model Card

For additional information see the Model Card paper: https://arxiv.org/pdf/1810.03993.pdf

## Model Details
- Model type: Gradient Boosting Classifier with hyperparameter tuning via GridSearchCV
- Machine learning library: Scikit-learn
- Hyperparameters tuned: n_estimators: [10, 20, 30], max_depth: [5, 10], min_samples_split: [20, 50, 100], learning_rate: [1.0]
- Saved models: model/model.pkl, model/encoder.pkl

## Intended Use
- Academic research on income prediction.
- Fairness and bias auditing across demographic groups.
- Educational machine learning demonstrations.

## Training Data
- Dataset: UCI Census Income Dataset, https://archive.ics.uci.edu/dataset/20/census+income
- Size: 48,842 records
- Split: 80% training / 20% testing, by salary
- Features: 14 features including age, workclass, education, marital-status, occupation, race, sex, hours-per-week, and more
- Label: Binary classification according to salary <=50K or >50K annual income

## Evaluation Data
- Test set: 20% of dataset
- Evaluation metrics: compute_model_metrics(), performance_on_categorical_slice()
- Slice Evaluation Output: Logged in slice_output.txt

## Metrics
- Metrics are computed based on: Precision: How many predicted >$50K incomes are correct, Recall: How many actual >$50K incomes are detected, F1 Score (F-beta, β=1): mean of precision and recall
- Model's overall test performance: Precision: 0.8697 | Recall: 0.7343 | F1: 0.7962

## Ethical Considerations
- Data quality. Missing values in some columns like workclass, occupation, native-country
- Bias and fairness concerns. The model performs better on majority and higher-education groups, while some groups like Jamaica, Ireland, and Poland receive zero recall.

## Caveats and Recommendations
- Clean and process the dataset before performing any model test/training.
- Resample or weight training data to improve representation of underrepresented classes.