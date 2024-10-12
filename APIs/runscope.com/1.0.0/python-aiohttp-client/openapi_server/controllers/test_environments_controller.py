from typing import List, Dict
from aiohttp import web

from openapi_server.models.buckets_bucket_key_tests_test_id_environments_get200_response import BucketsBucketKeyTestsTestIdEnvironmentsGet200Response
from openapi_server.models.environment import Environment
from openapi_server import util


async def buckets_bucket_key_tests_test_id_environments_environment_id_put(request: web.Request, bucket_key, test_id, environment_id, modified_environment) -> web.Response:
    """Update the details of a test environment.

    

    :param bucket_key: Unique identifier for a bucket
    :type bucket_key: str
    :param test_id: Unique identifier for a test
    :type test_id: str
    :param environment_id: Unique identifier for a test environment
    :type environment_id: str
    :param modified_environment: 
    :type modified_environment: dict | bytes

    """
    modified_environment = Environment.from_dict(modified_environment)
    return web.Response(status=200)


async def buckets_bucket_key_tests_test_id_environments_get(request: web.Request, bucket_key, test_id) -> web.Response:
    """Return details of the test&#39;s environments (only those that belong to the specified test)

    

    :param bucket_key: Unique identifier for a bucket
    :type bucket_key: str
    :param test_id: Unique identifier for a test
    :type test_id: str

    """
    return web.Response(status=200)


async def buckets_bucket_key_tests_test_id_environments_post(request: web.Request, bucket_key, test_id, new_environment) -> web.Response:
    """Create new test environment.

    

    :param bucket_key: Unique identifier for a bucket
    :type bucket_key: str
    :param test_id: Unique identifier for a test
    :type test_id: str
    :param new_environment: 
    :type new_environment: dict | bytes

    """
    new_environment = Environment.from_dict(new_environment)
    return web.Response(status=200)
