from ignition.functions.core import getData, funcEval, ptArray, ptIndex
import pytest
import os


def test_getData_initial():
    script_dir = os.path.dirname(__file__)
    file = os.path.join(script_dir, '../raw/press_data.txt')
    assert getData(file)[0] == 100
test_getData_initial()

def test_getData_mid():
    script_dir = os.path.dirname(__file__)
    file = os.path.join(script_dir, '../raw/press_data.txt')
    assert getData(file)[2] == 230
test_getData_mid()

def test_getData_final():
    script_dir = os.path.dirname(__file__)
    file = os.path.join(script_dir, '../raw/press_data.txt')
    assert getData(file)[4] == -400
test_getData_final()

def test_funcEval():
    script_dir = os.path.dirname(__file__)
    file = os.path.join(script_dir, '../raw/press_data.txt')
    data = getData(file)
    assert funcEval(data) == 900
test_funcEval()

def test_ptIndex():
    script_dir = os.path.dirname(__file__)
    file = os.path.join(script_dir, '../raw/press_data.txt')
    data = getData(file)
    assert ptIndex(data) == [0, 0, 0, 4, 0]
test_ptIndex()
