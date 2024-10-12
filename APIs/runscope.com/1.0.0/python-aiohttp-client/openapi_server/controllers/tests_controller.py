from typing import List, Dict
from aiohttp import web

from openapi_server.models.buckets_bucket_key_tests_get200_response import BucketsBucketKeyTestsGet200Response
from openapi_server.models.error import Error
from openapi_server.models.metrics import Metrics
from openapi_server.models.test import Test
from openapi_server.models.test_detail import TestDetail
from openapi_server import util


async def buckets_bucket_key_tests_get(request: web.Request, bucket_key) -> web.Response:
    """Returns a list of tests.

    

    :param bucket_key: Unique identifier for a bucket
    :type bucket_key: str

    """
    return web.Response(status=200)


async def buckets_bucket_key_tests_post(request: web.Request, bucket_key, new_test) -> web.Response:
    """Create a test.

    

    :param bucket_key: Unique identifier for a bucket
    :type bucket_key: str
    :param new_test: 
    :type new_test: dict | bytes

    """
    new_test = Test.from_dict(new_test)
    return web.Response(status=200)


async def buckets_bucket_key_tests_test_id_delete(request: web.Request, bucket_key, test_id) -> web.Response:
    """Delete a test, including all steps, schedules, test-specific environments and results.

    

    :param bucket_key: Unique identifier for a bucket
    :type bucket_key: str
    :param test_id: Unique identifier for a test
    :type test_id: str

    """
    return web.Response(status=200)


async def buckets_bucket_key_tests_test_id_get(request: web.Request, bucket_key, test_id) -> web.Response:
    """Retrieve the details of a given test by ID.

    

    :param bucket_key: Unique identifier for a bucket
    :type bucket_key: str
    :param test_id: Unique identifier for a test
    :type test_id: str

    """
    return web.Response(status=200)


async def buckets_bucket_key_tests_test_id_metrics_get(request: web.Request, bucket_key, test_id) -> web.Response:
    """Return details of the test metrics for the specified timeframe.

    

    :param bucket_key: Unique identifier for a bucket
    :type bucket_key: str
    :param test_id: Unique identifier for a test
    :type test_id: str

    """
    return web.Response(status=200)


async def buckets_bucket_key_tests_test_id_put(request: web.Request, bucket_key, test_id) -> web.Response:
    """Modify a test&#39;s name, description, default environment and its steps. To modify other individual properties of a test, make requests to the steps, environments, and schedules subresources of the test.

    

    :param bucket_key: Unique identifier for a bucket
    :type bucket_key: str
    :param test_id: Unique identifier for a test
    :type test_id: str

    """
    return web.Response(status=200)
