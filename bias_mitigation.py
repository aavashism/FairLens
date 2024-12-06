from fairlearn.reductions import ExponentiatedGradient, DemographicParity
from data_preprocessing import load_and_preprocess_data

def mitigate_bias():
    X_train, X_test, y_train, y_test = load_and_preprocess_data()

    # Bias mitigation with ExponentiatedGradient
    mitigator = ExponentiatedGradient(
        estimator=RandomForestClassifier(random_state=42),
        constraints=DemographicParity()
    )
    mitigator.fit(X_train, y_train, sensitive_features=X_train['sex'])

    # Predict with mitigated model
    y_pred_mitigated = mitigator.predict(X_test)
    print("Bias mitigation applied.")
    return y_test, y_pred_mitigated, X_test['sex']
