# -*- coding: utf-8 -*-

import os
import pytest

from engines import BingEngine


@pytest.fixture(scope="module")
def engine():
    engine = BingEngine(api_key=os.environ["BING_API_KEY"])
    return engine

@pytest.fixture(scope="module")
def results(engine):
    return engine.search(u"python")

@pytest.fixture(scope="module")
def chinese_results(engine):
    return engine.search(u"豆瓣")

def test_request(results):
    assert isinstance(results, list)

def test_chinese_request(chinese_results):
    assert isinstance(chinese_results, list)

def test_result_item(results):
    item = results[0]
    assert hasattr(item, "title")
    assert hasattr(item, "url")
    assert hasattr(item, "description")
    assert item.source.name == 'bing'

def test_result_priority(results):
    item = results[2]
    assert item.priority == 2

def test_count(engine):
    results = engine.search("python", limit=5)
    assert len(results) == 5