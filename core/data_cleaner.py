from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.model_selection import train_test_split

def preprocess(data):
    preprocessor = ColumnTransformer(
        transformers=[
            ('num', StandardScaler(), ['raise']),
            ('cat', OneHotEncoder(handle_unknown='ignore'), ['fund'])
        ])

    # Разделяем данные
    X = data[['fund', 'raise']]
    y = data['roi']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    return preprocessor, X_train, X_test, y_train, y_test