"""Basic openpyxl exporter tests."""
import pytest
from openpyxl import Workbook


def test_create_workbook():
    wb = Workbook()
    assert wb is not None
    ws = wb.active
    assert ws is not None
