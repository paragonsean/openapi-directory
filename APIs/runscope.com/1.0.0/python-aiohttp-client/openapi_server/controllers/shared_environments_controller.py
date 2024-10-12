from typing import List, Dict
from aiohttp import web

from openapi_server.models.environment import Environment
from openapi_server import util


async def buckets_bucket_key_environments_environment_id_put(request: web.Request, bucket_key, environment_id, modified_environment) -> web.Response:
    """Update the details of a shared environment.

    

    :param bucket_key: Unique identifier for a bucket
    :type bucket_key: str
    :param environment_id: Unique identifier for a test environment
    :type environment_id: str
    :param modified_environment: 
    :type modified_environment: dict | bytes

    """
    modified_environment = Environment.from_dict(modified_environment)
    return web.Response(status=200)


async def buckets_bucket_key_environments_get(request: web.Request, bucket_key) -> web.Response:
    """Returns list of shared environments for a specified bucket.

    

    :param bucket_key: Unique identifier for a bucket
    :type bucket_key: str

    """
    return web.Response(status=200)


async def buckets_bucket_key_environments_post(request: web.Request, bucket_key, new_environment) -> web.Response:
    """Create new shared environment.

    

    :param bucket_key: Unique identifier for a bucket
    :type bucket_key: str
    :param new_environment: 
    :type new_environment: dict | bytes

    """
    new_environment = Environment.from_dict(new_environment)
    return web.Response(status=200)
