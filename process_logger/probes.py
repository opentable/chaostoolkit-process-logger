# -*- coding: utf-8 -*-

from chaoslib.exceptions import FailedActivity
from chaoslib.types import Activity, Configuration, Secrets
from chaoslib.provider.process import run_process_activity
from logzero import logger
from typing import Any

__all__ = ["run_process_with_log", "query_interval"]


def run_process_with_log(**arguments) -> Any:
    path = arguments['path']
    activity = {'type': 'probe', 'name': '',
                'provider': {
                    'type': 'process',
                    'path': path,
                    'arguments': {}}}
    result = run_process_activity(activity, {}, {})
    stdout = result[1]
    status_code = result[0]
    logger.info(stdout)
    return status_code
