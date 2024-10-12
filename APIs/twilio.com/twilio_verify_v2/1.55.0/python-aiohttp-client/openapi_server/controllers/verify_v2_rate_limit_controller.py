from typing import List, Dict
from aiohttp import web

from openapi_server.models.list_rate_limit_response import ListRateLimitResponse
from openapi_server.models.verify_v2_service_rate_limit import VerifyV2ServiceRateLimit
from openapi_server import util


async def create_rate_limit(request: web.Request, service_sid, unique_name, description=None) -> web.Response:
    """create_rate_limit

    Create a new Rate Limit for a Service

    :param service_sid: The SID of the [Service](https://www.twilio.com/docs/verify/api/service) the resource is associated with.
    :type service_sid: str
    :param unique_name: Provides a unique and addressable name to be assigned to this Rate Limit, assigned by the developer, to be optionally used in addition to SID. **This value should not contain PII.**
    :type unique_name: str
    :param description: Description of this Rate Limit
    :type description: str

    """
    return web.Response(status=200)


async def delete_rate_limit(request: web.Request, service_sid, sid) -> web.Response:
    """delete_rate_limit

    Delete a specific Rate Limit.

    :param service_sid: The SID of the [Service](https://www.twilio.com/docs/verify/api/service) the resource is associated with.
    :type service_sid: str
    :param sid: The Twilio-provided string that uniquely identifies the Rate Limit resource to fetch.
    :type sid: str

    """
    return web.Response(status=200)


async def fetch_rate_limit(request: web.Request, service_sid, sid) -> web.Response:
    """fetch_rate_limit

    Fetch a specific Rate Limit.

    :param service_sid: The SID of the [Service](https://www.twilio.com/docs/verify/api/service) the resource is associated with.
    :type service_sid: str
    :param sid: The Twilio-provided string that uniquely identifies the Rate Limit resource to fetch.
    :type sid: str

    """
    return web.Response(status=200)


async def list_rate_limit(request: web.Request, service_sid, page_size=None, page=None, page_token=None) -> web.Response:
    """list_rate_limit

    Retrieve a list of all Rate Limits for a service.

    :param service_sid: The SID of the [Service](https://www.twilio.com/docs/verify/api/service) the resource is associated with.
    :type service_sid: str
    :param page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
    :type page_size: int
    :param page: The page index. This value is simply for client state.
    :type page: int
    :param page_token: The page token. This is provided by the API.
    :type page_token: str

    """
    return web.Response(status=200)


async def update_rate_limit(request: web.Request, service_sid, sid, description=None) -> web.Response:
    """update_rate_limit

    Update a specific Rate Limit.

    :param service_sid: The SID of the [Service](https://www.twilio.com/docs/verify/api/service) the resource is associated with.
    :type service_sid: str
    :param sid: The Twilio-provided string that uniquely identifies the Rate Limit resource to fetch.
    :type sid: str
    :param description: Description of this Rate Limit
    :type description: str

    """
    return web.Response(status=200)
