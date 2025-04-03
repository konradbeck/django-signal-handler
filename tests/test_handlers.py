import logging
from unittest.mock import MagicMock

import pytest
from django.db.models.signals import post_delete, post_save, pre_delete, pre_save

from signals.handlers import SignalHandler


class MockModel:
    def __init__(self, pk=None):
        self.pk = pk


@pytest.fixture
def signal_handler():
    return SignalHandler()


@pytest.fixture
def mock_instance():
    return MockModel()


def test_run_pre_save_new(signal_handler, mock_instance):
    signal_handler.pre_save_new = MagicMock()
    signal_handler.run(MockModel, mock_instance, signal=pre_save)
    signal_handler.pre_save_new.assert_called_once_with(mock_instance, signal=pre_save)


def test_run_pre_save_update(signal_handler, mock_instance):
    mock_instance.pk = 1
    signal_handler.pre_save_update = MagicMock()
    signal_handler.run(MockModel, mock_instance, signal=pre_save)
    signal_handler.pre_save_update.assert_called_once_with(mock_instance, signal=pre_save)


def test_run_post_save_new(signal_handler, mock_instance):
    signal_handler.post_save_new = MagicMock()
    signal_handler.run(MockModel, mock_instance, signal=post_save, created=True)
    signal_handler.post_save_new.assert_called_once_with(mock_instance, signal=post_save, created=True)


def test_run_post_save_update(signal_handler, mock_instance):
    signal_handler.post_save_update = MagicMock()
    signal_handler.run(MockModel, mock_instance, signal=post_save, created=False)
    signal_handler.post_save_update.assert_called_once_with(mock_instance, signal=post_save, created=False)


def test_run_pre_delete(signal_handler, mock_instance):
    signal_handler.pre_delete = MagicMock()
    signal_handler.run(MockModel, mock_instance, signal=pre_delete)
    signal_handler.pre_delete.assert_called_once_with(mock_instance, signal=pre_delete)


def test_run_post_delete(signal_handler, mock_instance):
    signal_handler.post_delete = MagicMock()
    signal_handler.run(MockModel, mock_instance, signal=post_delete)
    signal_handler.post_delete.assert_called_once_with(mock_instance, signal=post_delete)


def test_run_unknown_signal(signal_handler, mock_instance, caplog):
    unknown_signal = "unknown_signal"
    with caplog.at_level(logging.WARNING):
        signal_handler.run(MockModel, mock_instance, signal=unknown_signal)
    assert f"Unknown or missing signal in kwargs: {unknown_signal}" in caplog.text


def test_default_pre_save_new(signal_handler, mock_instance):
    signal_handler.pre_save_new(mock_instance)


def test_default_post_save_new(signal_handler, mock_instance):
    signal_handler.post_save_new(mock_instance)


def test_default_pre_save_update(signal_handler, mock_instance):
    signal_handler.pre_save_update(mock_instance)


def test_default_post_save_update(signal_handler, mock_instance):
    signal_handler.post_save_update(mock_instance)


def test_default_pre_delete(signal_handler, mock_instance):
    signal_handler.pre_delete(mock_instance)


def test_default_post_delete(signal_handler, mock_instance):
    signal_handler.post_delete(mock_instance)