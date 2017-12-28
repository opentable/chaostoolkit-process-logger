# -*- coding: utf-8 -*-

from process_logger.actions import empty_action


def test_empty_action():
    assert empty_action() is None