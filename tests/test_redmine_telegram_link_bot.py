# -*- coding: utf-8 -*-
import sys

sys.path.append('../')

import pytest

import settings
settings.REDMINE_URL = "https://redmine.example.org"

from redmine_link_telegram_bot import extract_issue_urls

@pytest.mark.parametrize('message, expected_result', [
    ('https://redmine.example.org/issues/94642?tab=time_entries', [('https://redmine.example.org/issues/94642', '94642')])
])
def test_extract_issue_urls(message, expected_result):
    result = extract_issue_urls(message)
    
    assert result == expected_result
