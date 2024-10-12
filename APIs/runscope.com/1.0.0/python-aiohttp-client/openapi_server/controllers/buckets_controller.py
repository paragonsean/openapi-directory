from typing import List, Dict
from aiohttp import web

from openapi_server.models.bucket import Bucket
from openapi_server.models.buckets_get200_response import BucketsGet200Response
from openapi_server.models.error import Error
from openapi_server.models.new_bucket import NewBucket
from openapi_server import util


async def buckets_bucket_key_delete(request: web.Request, bucket_key) -> web.Response:
    """Delete a single bucket resource.

    

    :param bucket_key: Unique identifier for a bucket
    :type bucket_key: str

    """
    return web.Response(status=200)


async def buckets_bucket_key_get(request: web.Request, bucket_key) -> web.Response:
    """Returns a single bucket resource.

    

    :param bucket_key: Unique identifier for a bucket
    :type bucket_key: str

    """
    return web.Response(status=200)


async def buckets_get(request: web.Request, ) -> web.Response:
    """Returns a list of buckets.

    


    """
    return web.Response(status=200)


async def buckets_post(request: web.Request, new_bucket) -> web.Response:
    """Create a new bucket

    

    :param new_bucket: 
    :type new_bucket: dict | bytes

    """
    new_bucket = NewBucket.from_dict(new_bucket)
    return web.Response(status=200)
