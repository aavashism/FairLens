import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

def load_and_preprocess_data():
    # Load dataset
    url = "https://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.data"
    columns = ['age', 'workclass', 'fnlwgt', 'education', 'education-num', 
               'marital-status', 'occupation', 'relationship', 'race', 'sex', 
               'capital-gain', 'capital-loss', 'hours-per-week', 'native-country', 'income']
    data = pd.read_csv(url, header=None, names=columns, na_values=' ?', skipinitialspace=True)
    data = data.dropna()

    # Encode categorical variables
    data['income'] = LabelEncoder().fit_transform(data['income'])
    data['sex'] = LabelEncoder().fit_transform(data['sex'])
    data['race'] = LabelEncoder().fit_transform(data['race'])

    # Select features and target
    X = data.drop(columns=['income'])
    y = data['income']

    # One-hot encode categorical variables
    X = pd.get_dummies(X, drop_first=True)

    # Split data into training and test sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
    return X_train, X_test, y_train, y_test
