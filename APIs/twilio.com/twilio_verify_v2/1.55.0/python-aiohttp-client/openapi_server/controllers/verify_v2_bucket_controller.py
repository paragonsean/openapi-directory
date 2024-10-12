from typing import List, Dict
from aiohttp import web

from openapi_server.models.list_bucket_response import ListBucketResponse
from openapi_server.models.verify_v2_service_rate_limit_bucket import VerifyV2ServiceRateLimitBucket
from openapi_server import util


async def create_bucket(request: web.Request, service_sid, rate_limit_sid, interval, max) -> web.Response:
    """create_bucket

    Create a new Bucket for a Rate Limit

    :param service_sid: The SID of the [Service](https://www.twilio.com/docs/verify/api/service) the resource is associated with.
    :type service_sid: str
    :param rate_limit_sid: The Twilio-provided string that uniquely identifies the Rate Limit resource.
    :type rate_limit_sid: str
    :param interval: Number of seconds that the rate limit will be enforced over.
    :type interval: int
    :param max: Maximum number of requests permitted in during the interval.
    :type max: int

    """
    return web.Response(status=200)


async def delete_bucket(request: web.Request, service_sid, rate_limit_sid, sid) -> web.Response:
    """delete_bucket

    Delete a specific Bucket.

    :param service_sid: The SID of the [Service](https://www.twilio.com/docs/verify/api/service) the resource is associated with.
    :type service_sid: str
    :param rate_limit_sid: The Twilio-provided string that uniquely identifies the Rate Limit resource.
    :type rate_limit_sid: str
    :param sid: A 34 character string that uniquely identifies this Bucket.
    :type sid: str

    """
    return web.Response(status=200)


async def fetch_bucket(request: web.Request, service_sid, rate_limit_sid, sid) -> web.Response:
    """fetch_bucket

    Fetch a specific Bucket.

    :param service_sid: The SID of the [Service](https://www.twilio.com/docs/verify/api/service) the resource is associated with.
    :type service_sid: str
    :param rate_limit_sid: The Twilio-provided string that uniquely identifies the Rate Limit resource.
    :type rate_limit_sid: str
    :param sid: A 34 character string that uniquely identifies this Bucket.
    :type sid: str

    """
    return web.Response(status=200)


async def list_bucket(request: web.Request, service_sid, rate_limit_sid, page_size=None, page=None, page_token=None) -> web.Response:
    """list_bucket

    Retrieve a list of all Buckets for a Rate Limit.

    :param service_sid: The SID of the [Service](https://www.twilio.com/docs/verify/api/service) the resource is associated with.
    :type service_sid: str
    :param rate_limit_sid: The Twilio-provided string that uniquely identifies the Rate Limit resource.
    :type rate_limit_sid: str
    :param page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
    :type page_size: int
    :param page: The page index. This value is simply for client state.
    :type page: int
    :param page_token: The page token. This is provided by the API.
    :type page_token: str

    """
    return web.Response(status=200)


async def update_bucket(request: web.Request, service_sid, rate_limit_sid, sid, interval=None, max=None) -> web.Response:
    """update_bucket

    Update a specific Bucket.

    :param service_sid: The SID of the [Service](https://www.twilio.com/docs/verify/api/service) the resource is associated with.
    :type service_sid: str
    :param rate_limit_sid: The Twilio-provided string that uniquely identifies the Rate Limit resource.
    :type rate_limit_sid: str
    :param sid: A 34 character string that uniquely identifies this Bucket.
    :type sid: str
    :param interval: Number of seconds that the rate limit will be enforced over.
    :type interval: int
    :param max: Maximum number of requests permitted in during the interval.
    :type max: int

    """
    return web.Response(status=200)
