from fairlearn.metrics import MetricFrame, demographic_parity_difference
from sklearn.metrics import accuracy_score
from model_training import train_model

def analyze_fairness():
    model, X_test, y_test, y_pred = train_model()

    # Sensitive feature (e.g., gender)
    sensitive_feature = X_test['sex']

    # Calculate fairness metrics
    dp_difference = demographic_parity_difference(
        y_test, y_pred, sensitive_features=sensitive_feature
    )
    print(f"Demographic Parity Difference: {dp_difference:.2f}")

    # Group-wise metrics
    metric_frame = MetricFrame(
        metrics={"Accuracy": accuracy_score},
        y_true=y_test,
        y_pred=y_pred,
        sensitive_features=sensitive_feature
    )
    print("Metrics by group:")
    print(metric_frame.by_group)
