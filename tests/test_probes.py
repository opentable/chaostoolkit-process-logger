# -*- coding: utf-8 -*-

from process_logger.probes import run_process_with_log


def test_empty_probe():
    assert run_process_with_log(path='./file_path') is True

