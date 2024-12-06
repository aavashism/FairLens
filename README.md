# FairLens: AI Bias Analysis and Mitigation Tool 
**Author**: Aavash Upadhyaya

---

## **Overview**
**FairLens** is an AI-powered bias analysis and mitigation tool designed to detect, evaluate, and address biases in machine learning models and datasets. It provides a structured approach to ensure that AI systems adhere to ethical principles of fairness, accountability, and transparency. By identifying biases across sensitive demographic groups, FairLens empowers developers and policymakers to make equitable and informed decisions.

---

## **Key Objectives**
1. **Bias Detection**: Analyze datasets and machine learning models to detect patterns of bias (e.g., gender, race, socioeconomic status).
2. **Fairness Metrics**: Evaluate fairness using standard metrics like demographic parity and equalized odds.
3. **Bias Mitigation**: Apply techniques to mitigate identified biases, such as reweighting or post-processing.
4. **Explainability**: Provide insights into how features impact model decisions using explainable AI tools.
5. **Interactive Visualization**: Enable users to explore fairness metrics and mitigation impacts through an intuitive dashboard.

---

## **Features**
1. **Comprehensive Bias Analysis**
   - Detect imbalances in datasets and model predictions.
   - Evaluate group-wise performance across sensitive attributes.

2. **Fairness Metrics**
   - Implements metrics like **Demographic Parity Difference**, **Equalized Odds**, and **Accuracy by Group**.

3. **Bias Mitigation**
   - Supports techniques such as **Exponentiated Gradient Reduction** for post-processing model outputs.

4. **Interactive Dashboard**
   - Visualize fairness metrics through a web-based dashboard built with Dash and Plotly.

5. **Customizable Framework**
   - Easily adaptable to various datasets and use cases (e.g., hiring, healthcare, criminal justice).

---

## **How It Works**
### **1. Data Preprocessing**
- Loads and preprocesses the dataset to ensure compatibility.
- Encodes categorical features and handles missing data.
- Splits the dataset into training and testing sets.

### **2. Model Training**
- Trains a machine learning model (e.g., Random Forest Classifier) to predict outcomes.
- Evaluates the model's overall accuracy before fairness analysis.

### **3. Fairness Analysis**
- Uses the Fairlearn library to calculate fairness metrics.
- Provides insights into model performance across sensitive groups (e.g., gender, race).

### **4. Bias Mitigation**
- Applies bias mitigation techniques such as:
  - Reweighting datasets.
  - Post-processing model outputs using **Demographic Parity** constraints.

### **5. Dashboard**
- Visualizes fairness metrics and mitigation impacts through an interactive web-based dashboard.
- Allows users to explore fairness and evaluate different mitigation strategies.

---

## **Technologies Used**
- **Programming Language**: Python
- **Machine Learning**: scikit-learn
- **Fairness Analysis**: Fairlearn
- **Visualization**: Dash, Plotly
- **Data Manipulation**: pandas, numpy
- **Web Framework**: Dash

---

## **Installation**
1. Clone the repository:
   ```bash
   git clone https://github.com/aavashism/FairLens.git
   cd FairLens
   ```

2. Set up a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

## **Usage**
1. **Data Preprocessing**:
   ```bash
   python data_preprocessing.py
   ```
   - Loads the dataset and splits it into training and testing sets.

2. **Model Training**:
   ```bash
   python model_training.py
   ```
   - Trains the machine learning model and evaluates its accuracy.

3. **Fairness Analysis**:
   ```bash
   python fairness_analysis.py
   ```
   - Analyzes fairness metrics and identifies biases in the model.

4. **Bias Mitigation**:
   ```bash
   python bias_mitigation.py
   ```
   - Applies mitigation techniques to reduce biases in model outputs.

5. **Interactive Dashboard**:
   ```bash
   python dashboard.py
   ```
   - Launches a web-based dashboard for visualizing fairness metrics.

---

## **Example Output**
- **Accuracy Before Mitigation**: 85%
- **Demographic Parity Difference Before Mitigation**: 0.25
- **Accuracy After Mitigation**: 83%
- **Demographic Parity Difference After Mitigation**: 0.05

---

## **Project Structure**
```
FairLens/
│
├── data_preprocessing.py      # Handles dataset loading and preprocessing
├── model_training.py          # Trains the machine learning model
├── fairness_analysis.py       # Analyzes fairness metrics
├── bias_mitigation.py         # Applies bias mitigation techniques
├── dashboard.py               # Creates an interactive visualization dashboard
├── requirements.txt           # Lists required Python libraries
├── README.md                  # Project documentation
└── .gitignore                 # Specifies files to be ignored by Git
```

---

## **Future Enhancements**
- **Broader Dataset Support**: Extend support for more datasets and sensitive attributes.
- **Real-Time Fairness Audits**: Enable live monitoring of fairness metrics during model inference.
- **Integration with Explainable AI**: Incorporate SHAP and LIME for deeper insights into model decisions.
- **Policy Recommendations**: Provide actionable suggestions for policymakers to address AI biases.


---

## **Contact**
**Aavash Upadhyaya**  
Email: aavashupadhyaya2000@gmail.com  
GitHub: https://github.com/aavashism
