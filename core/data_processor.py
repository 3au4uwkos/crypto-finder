from sklearn.impute import SimpleImputer

from .data_cleaner import preprocess
from sklearn.ensemble import RandomForestRegressor
from sklearn.pipeline import Pipeline
import pandas as pd


def train_model(df):
    preprocessor, X_train, X_test, y_train, y_test = preprocess(df)

    model = Pipeline([
        ('preprocessor', preprocessor),
        SimpleImputer(strategy='most_frequent'),
        ('regressor', RandomForestRegressor(n_estimators=100, random_state=42))
    ])

    # Обучаем модель
    model.fit(X_train, y_train)

    return model


def fill_column(df: pd.DataFrame, model) -> pd.DataFrame:
    """
    Добавляет в DataFrame колонку с предсказанными значениями ROI
    на основе колонок 'fund' и 'raise' с использованием обученной модели

    Параметры:
        df (pd.DataFrame): Исходный DataFrame
        model: Обученная модель (должна поддерживать .predict())

    Возвращает:
        pd.DataFrame: DataFrame с добавленной колонкой 'roi'
    """
    # Создаем копию DataFrame чтобы не изменять оригинал
    result_df = df.copy()

    # Проверяем наличие необходимых колонок
    required_columns = ['fund', 'raise']
    if not all(col in df.columns for col in required_columns):
        missing = [col for col in required_columns if col not in df.columns]
        raise ValueError(f"Отсутствуют необходимые колонки: {missing}")

    # Создаем временный DataFrame для предсказания
    predict_data = df[required_columns]

    # Делаем предсказания
    try:
        predictions = model.predict(predict_data)
        result_df['roi'] = predictions
    except Exception as e:
        raise ValueError(f"Ошибка при предсказании: {str(e)}")

    return result_df
