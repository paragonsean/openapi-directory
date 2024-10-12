from typing import List, Dict
from aiohttp import web

from openapi_server.models.standard_error import StandardError
from openapi_server.models.test_step import TestStep
from openapi_server import util


async def buckets_bucket_key_tests_test_id_steps_get(request: web.Request, bucket_key, test_id) -> web.Response:
    """List test steps for a test.

    

    :param bucket_key: Unique identifier for a bucket
    :type bucket_key: str
    :param test_id: Unique identifier for a test
    :type test_id: str

    """
    return web.Response(status=200)


async def buckets_bucket_key_tests_test_id_steps_post(request: web.Request, bucket_key, test_id, test_step) -> web.Response:
    """Add new test step.

    

    :param bucket_key: Unique identifier for a bucket
    :type bucket_key: str
    :param test_id: Unique identifier for a test
    :type test_id: str
    :param test_step: 
    :type test_step: dict | bytes

    """
    test_step = TestStep.from_dict(test_step)
    return web.Response(status=200)


async def buckets_bucket_key_tests_test_id_steps_step_id_delete(request: web.Request, bucket_key, test_id, step_id) -> web.Response:
    """Delete a step from a test.

    

    :param bucket_key: Unique identifier for a bucket
    :type bucket_key: str
    :param test_id: Unique identifier for a test
    :type test_id: str
    :param step_id: Unique identifier for a test step
    :type step_id: str

    """
    return web.Response(status=200)


async def buckets_bucket_key_tests_test_id_steps_step_id_put(request: web.Request, bucket_key, test_id, step_id, test_step) -> web.Response:
    """Update the details of a single test step.

    

    :param bucket_key: Unique identifier for a bucket
    :type bucket_key: str
    :param test_id: Unique identifier for a test
    :type test_id: str
    :param step_id: Unique identifier for a test step
    :type step_id: str
    :param test_step: 
    :type test_step: dict | bytes

    """
    test_step = TestStep.from_dict(test_step)
    return web.Response(status=200)
