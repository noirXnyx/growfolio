import logging
import multiprocessing
import numpy as np
import pandas as pd
import pytest

from sklearn.ensemble import GradientBoostingClassifier
from sklearn.model_selection import train_test_split, GridSearchCV

from ml.model import (
    train_model,
    compute_model_metrics,
)

@pytest.fixture
def mock_logger(monkeypatch):
    """
    Mocks logging.info to prevent cluttering test output and allow for verification.
    """
    def mock_info(msg, *args, **kwargs):
        print(f"[MOCK LOG] {msg}")
    monkeypatch.setattr(logging, "info", mock_info)


@pytest.fixture
def mock_cpu_count(monkeypatch):
    """
    Mocks multiprocessing.cpu_count to control parallelism in GridSearchCV.
    """
    monkeypatch.setattr(multiprocessing, "cpu_count", lambda: 2)

## Test 1
def test_compute_model_metrics_known_values():
    """
    Test compute_model_metrics on known input/output values.
    """
    y_true = np.array([1, 0, 1, 1])
    y_pred = np.array([1, 0, 0, 1])  # TP=2, FP=0, FN=1
    precision, recall, f1 = compute_model_metrics(y_true, y_pred)
    assert precision == pytest.approx(1.0)
    assert recall == pytest.approx(2 / 3, 0.01)
    assert f1 == pytest.approx(0.8, 0.01)

## Test 2
def test_train_model_returns_expected_type():
    """
    Ensure train_model returns GridSearchCV with a GradientBoostingClassifier estimator.
    """
    X = np.array([[0, 1], [1, 0], [1, 1], [0, 0], [2, 1], [1, 2]])
    y = np.array([0, 1, 0, 1, 0, 1])
    model = train_model(X, y)
    assert isinstance(model, GridSearchCV)
    assert isinstance(model.best_estimator_, GradientBoostingClassifier)

## Test 3
def test_data_split_shape():
    """
    Confirm train_test_split returns the expected train/test sizes and types.
    """
    df = pd.DataFrame({
        "feature": range(100),
        "salary": [">50K" if i % 2 == 0 else "<=50K" for i in range(100)]
    })
    train, test = train_test_split(df, test_size=0.2, stratify=df["salary"], random_state=42)
    assert isinstance(train, pd.DataFrame)
    assert isinstance(test, pd.DataFrame)
    assert len(train) == 80
    assert len(test) == 20

